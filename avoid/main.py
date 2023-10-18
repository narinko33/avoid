import tkinter as tk
import comment as co
from random import randint as ri

mouse_x, mouse_y = 0, 0
mouse_button = 0

makes = []


# ランダム生成
def comment_make():
    global makes
    size = ("Arial", ri(25, 100))
    make = cvs.create_text(
        ri(50, 900),
        ri(50, 800),
        text=co.comment[ri(0, 20)],
        fill=co.fill_list[ri(0, 9)],
        tag=f"text1",
        font=size,
    )
    cvs.after(ri(800, 1000), comment_make)


# テキストブロック左から右に動く！
def left():
    cvs.move("text1", 5, 0)
    # speed = ri(20, 20)
    # for make in makes:
    #     print(make["fill"])
    #     if make["fill"] == "white":
    #         speed = ri(10, 30)

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
    global mouse_button
    if mouse_button == 0:
        mouse_button = e.num


#  テキストを消す


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
comment_make()


root.bind("<Motion>", mouse)
root.bind("<Button>", mouse_click)


root.mainloop()
