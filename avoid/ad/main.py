import tkinter as tk
import comment as co
from random import randint as ri

mouse_x, mouse_y = 0, 0
mouse_button = 0

makes = []
comment_list = []  # 追加：コメント管理リスト


# ランダム生成
# 修正：関数名は動詞を先に記述
# def comment_make():
def make_comment():
    # 修正前
    # global makes
    size = ("Arial", ri(25, 100))
    # make = cvs.create_text(
    #     ri(50, 900),
    #     ri(50, 800),
    #     text=co.comment[ri(0, 20)],
    #     fill=co.fill_list[ri(0, 9)],
    #     tag=f"text1",
    #     font=size,
    # )
    # 修正前ここまで

    # 修正後
    # コメントのオブジェクト１つ生成
    comment = co.Comment(
        ri(50, 900),
        ri(50, 800),
        tag="comment",
    )

    # 生成したコメントをキャンバスに描画後、コメント管理リストに追加
    # cvs.create_textの戻り値（キャンバスID）を生成したコメントのidに渡してます
    comment.id = cvs.create_text(
        comment.start_posx,
        comment.start_posy,
        text=comment.text,
        fill=comment.color,
        tag=comment.tag,
        font=size,
    )
    comment_list.append(comment)
    # 修正後ここまで
    cvs.after(ri(800, 1000), make_comment)


# テキストブロック左から右に動く！
def left():
    # 修正前
    # cvs.move("text1", 5, 0)
    # speed = ri(20, 20)
    # for make in makes:
    #     print(make["fill"])
    #     if make["fill"] == "white":
    #         speed = ri(10, 30)
    # 修正前ここまで

    # 修正後
    # 色ごとに移動スピードに変化加える
    speed = 0
    for comment in comment_list:
        if comment.color == "white":
            speed = 5
        elif comment.color == "red":
            speed = 20
        elif comment.color == "yellow":
            speed = 15
        elif comment.color == "green":
            speed = 10
        cvs.move(comment.id, speed, 0)
        # 画面外に行ったら削除される
        delete_comment()
    # 修正後ここまで

    cvs.after(ri(-10, 25), left)


# マウスでの操作
def mouse(e):
    global mouse_x, mouse_y
    cvs.delete("SCREEN")
    mouse_x = e.x
    mouse_y = e.y
    cvs.create_image(e.x, e.y, image=img, tag="SCREEN")


# マウスクリック
def mouse_click(e):
    # 修正前
    # global mouse_button
    # if mouse_button == 0:
    #     mouse_button = e.num
    # 修正前ここまで

    # 修正後
    delete_comment(e)
    # 修正後ここまで


#  テキストを消す
def delete_comment(mouse=None):
    for comment in comment_list:
        # コメントの座標取得
        pos = cvs.bbox(comment.id)

        # mouseがNoneなら画面外判定、Noneでなければクリック判定
        if mouse != None:
            # テキストをクリックされたら
            if pos[0] <= mouse.x <= pos[2] and pos[1] <= mouse.y <= pos[3]:
                cvs.delete(comment.id)
                comment_list.remove(comment)
                print(comment.text)
                break
        else:
            # 画面(右端)から出たら
            if pos[0] >= 1300:
                cvs.delete(comment.id)
                comment_list.remove(comment)
                print(comment.text)
                break


root = tk.Tk()
root.geometry("1280x720")
frame = tk.Frame(root)
frame.pack()
font_size = ("Arial", ri(25, 100))


# キャンパス描画
cvs = tk.Canvas(frame, width=1300, height=800, bg="black")
cvs.pack()

# 自機描画
img = tk.PhotoImage(file="avoid/star.png").subsample(2)
cvs.create_image(50, 50, image=img, tag="SCREEN")

# テキストブロック描画
cvs.create_text(50, 100, text="わあ", fill="white", tag=f"text1", font=font_size)

left()
make_comment()


root.bind("<Motion>", mouse)
root.bind("<Button>", mouse_click)


root.mainloop()