import tkinter
root=tkinter.Tk()

root.title("Aditya Pawar")
root.geometry("1580x780+0+0")




#frame


main_frame=tkinter.Frame(root,bg="pink",bd=3,relief="ridge")
main_frame.place(x=5,y=55,width=1518,height=720  )




frame1=tkinter.Frame(main_frame,bd=3,relief="ridge",bg="lightpink")
frame1.place(x=0,y=10,width=216,height=340)

frame2=tkinter.Frame(main_frame,bd=3,relief="ridge")
frame2.place(x=216,y=10,width=216,height=340)

frame3=tkinter.Frame(main_frame,bd=3,relief="ridge")
frame3.place(x=432,y=10,width=216,height=340)

frame4=tkinter.Frame(main_frame,bd=3,relief="ridge")
frame4.place(x=648,y=10,width=216,height=340)

frame5=tkinter.Frame(main_frame,bd=3,relief="ridge")
frame5.place(x=864,y=10,width=216,height=340)

frame6=tkinter.Frame(main_frame,bd=3,relief="ridge")
frame6.place(x=1080,y=10,width=216,height=340)

frame7=tkinter.Frame(main_frame,bd=3,relief="ridge")
frame7.place(x=1296,y=10,width=216,height=340)

framed1=tkinter.Frame(main_frame,bd=3,relief="ridge")
framed1.place(x=0,y=360,width=216,height=340)

framed2=tkinter.Frame(main_frame,bd=3,relief="ridge")
framed2.place(x=216,y=360,width=216,height=340)

framed3=tkinter.Frame(main_frame,bd=3,relief="ridge")
framed3.place(x=432,y=360,width=216,height=340)

framed4=tkinter.Frame(main_frame,bd=3,relief="ridge")
framed4.place(x=648,y=360,width=216,height=340)

framed5=tkinter.Frame(main_frame,bd=3,relief="ridge")
framed5.place(x=864,y=360,width=216,height=340)

framed6=tkinter.Frame(main_frame,bd=3,relief="ridge")
framed6.place(x=1080,y=360,width=216,height=340)

framed7=tkinter.Frame(main_frame,bd=3,relief="ridge")
framed7.place(x=1296,y=700,width=216,height=340)

#heading
heading=tkinter.Label(root,width=570,text="KOMAL DRESSES",font=("arial",30,"bold"),bg="light blue",fg="white")
heading.pack()



#label

imagepath=tkinter.PhotoImage(file=r"C:\Users\91774\OneDrive\Desktop\70.png")
image1=tkinter.Label(frame1,image=imagepath,width=215,height=339)
image1.place(x=0,y=0,relwidth=1,relheight=1)

#scroll
scrollx=tkinter.Scrollbar(main_frame,orient="horizontal")           
scrolly=tkinter.Scrollbar(main_frame,orient="vertical")

scrollx.pack(side="bottom",fill="x")
scrolly.pack(side="right",fill="y")



root.mainloop() 