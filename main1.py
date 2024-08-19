import tkinter 

root= tkinter.Tk()
root.geometry("500x500")

def square_root():
    number=int(entry.get(),)
    square_root = number ** 0.5
    print("squareroot of {} is {}".format(number, square_root))


    




label=tkinter.Label(text="square root finder")
label.place(x=250,y=250)

label1=tkinter.Label(text=print)
label1.place(x=250,y=230)
entry=tkinter.Entry()
entry.place(x=250,y=270)

button=tkinter.Button(text="find",command=square_root)
button.place(x=250,y=290)


root.mainloop()