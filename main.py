import tkinter as tk

mouse_x, mouse_y = 0, 0


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

cvs = tk.Canvas(frame, width=1000, height=600)
cvs.pack()

img = tk.PhotoImage(file="avoid/star.png")
cvs.create_image(100, 100, image=img, tag="SCREEN")


root.bind("<Motion>", mouse)


root.mainloop()
