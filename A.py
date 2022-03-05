from tkinter import *

def click():
    password=input.get()
    title = Label(frame, text = password, bg="white", font=40)
    title.pack()

root = Tk()

root["bg"] = 'black'
root.title("калькулятор 2.0")
root.wm_attributes("-alpha", 0.9)
root.geometry("300x500")

root.resizable(width=False, height=False)

canvas = Canvas(root, height=300, width=500)
canvas.pack()

frame = Frame(root, bg="black")
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

# title = Label(frame, text = "Hi", bg="white", font=40)
# title.pack()
btn= Button(frame,text="click", bg = "green", command=click)
btn.pack()
input= Entry(frame, bg="blue", show="#")
input.pack()

root.mainloop()
