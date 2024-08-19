import tkinter
root=tkinter.Tk()

root.title("Aditya Pawar")
root.geometry("580x670+100+50")

title_name=tkinter.Label(text="STUDENT ENTRY FORM",font=("arial",30,"bold"),bg="white",fg="blue")
title_name.pack(side="top")

main_frame=tkinter.Frame(root,bd=3,relief="ridge")
main_frame.place(x=20,y=70,width=550,height=580)

#function

def showdata():
    if check_var.get()=="on":
        get_data=f'Name:{name_var.get}\nEmail:{email_var.get}\nGender:{gender_var.get}'
        mydata.config(text=get_data,font=("arial",15))
    else:
        mydata.config(text="Please Accept Our Trems & Conditions")    

#lebel

name=tkinter.Label(main_frame,text="Student Name",font=("arial",15,"bold"))
name.grid(row=0,column=0,padx=10,pady=10,sticky="w")

email=tkinter.Label(main_frame,text="Student Email",font=("arial",15,"bold"))
email.grid(row=1,column=0,padx=10,pady=10,sticky="w")

gender=tkinter.Label(main_frame,text="Select Gender",font=("arial",15,"bold"))
gender.grid(row=2,column=0,padx=10,pady=10,sticky="w")

#variable

name_var=tkinter.Variable()
email_var=tkinter.Variable()
gender_var=tkinter.Variable()
check_var=tkinter.Variable()

#entry

name_entry=tkinter.Entry(main_frame,textvariable=name_var,font=("arial",15,"bold"),width=20,highlightthickness=2)
name_entry.grid(row=0,column=1,padx=10,pady=10,sticky="w")

email_entry=tkinter.Entry(main_frame,textvariable=email_var,font=("arial",15,"bold"),width=20,highlightthickness=2)
email_entry.grid(row=1,column=1,padx=10,pady=10,sticky="w")

#radio button

male=tkinter.Radiobutton(main_frame,variable=gender_var,text="Male",value="male",font=("arial",15,"bold"))
male.grid(row=2,column=1,pady=2,sticky="w")
gender_var.set("male")

female=tkinter.Radiobutton(main_frame,variable=gender_var,text="Female",value="female",font=("arial",15,"bold"))
female.grid(row=3,column=1,pady=2,sticky="w")

#check button

check_btn=tkinter.Checkbutton(main_frame,variable=check_var,onvalue="on",offvalue="off",text="Agree Terms & Conditions",font=("arial",15,"bold"))
check_btn.grid(row=4,column=1,pady=10,sticky="w")
check_var.set("off")

#button

btn=tkinter.Button(main_frame,command=showdata,text=('Save Data'),width=20,font=("arial",15,"bold"),bg="blue",fg="white")
btn.grid(row=5,column=1,pady=10,sticky="w")

mydata=tkinter.Label(main_frame,text="",font=("arial",15,"bold"))
mydata.grid(row=6,column=1,padx=10,pady=10,sticky="w")

root.mainloop()