import tkinter as tk
from random import randint as ri

mouse_x, mouse_y = 0, 0


# ランダム生成
def block_make():
    size = ("Arial", ri(25, 100))
    make = cvs.create_text(
        ri(50, 500),
        ri(100, 400),
        text="だんまくきたーーーーーーー",
        fill="white",
        tag="text",
        font=size,
    )
    move()
    cvs.after(ri(1500, 2000), block_make)


# テキストブロック左から右に動く！
def left():
    cvs.move("text", 5, 0)
    cvs.after(100, left)


# テキストブロック上から下に動く！
def up():
    cvs.move("text", 0, 5)
    cvs.after(100, up)


def move():
    num = ri(1, 2)
    if num == 1:
        left()
    elif num == 2:
        up()


# マウスでの操作
def mouse(e):
    global mouse_x, mouse_y
    cvs.delete("SCREEN")
    mouse_x = e.x
    mouse_y = e.y
    cvs.create_image(e.x, e.y, image=img, tag="SCREEN")


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
cvs.create_text(50, 100, text="わあ", fill="white", tag="text", font=font_size)
move()
# left()
# up()

block_make()


root.bind("<Motion>", mouse)


root.mainloop()
