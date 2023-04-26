from tkinter import *
import requests

main_window=Tk()
main_window.title("Student Management System")
main_window.geometry("900x600+100+30")
main_window.iconbitmap("edu.ico")
main_window.configure(bg="pink")
f=("Arial",20,"bold")

def f1():
	add_window.deiconify()
	main_window.withdraw()
def f2():
	main_window.deiconify()
	add_window.withdraw()

btnAdd=Button(main_window,text="Add",font=f,bd=3,command=f1)
btnAdd.place(x=350,y=10)
btnView=Button(main_window,text="View",font=f,bd=3)
btnView.place(x=350,y=110)
btnUpdate=Button(main_window,text="Update",font=f,bd=3)
btnUpdate.place(x=350,y=210)
btnDelete=Button(main_window,text="Delete",font=f,bd=3)
btnDelete.place(x=350,y=310)
btnPlot=Button(main_window,text="Plot",font=f,bd=3)
btnPlot.place(x=350,y=410)


res=requests.get("https://ipinfo.io/")
data=res.json()
city=data['city']
state=data['region']
loc=city+","+state
lblCity=Label(main_window,text="Location:"+loc,font=f,bg="pink")
lblCity.place(x=100,y=500)

add_window=Toplevel(main_window)
add_window.title("Add")
add_window.geometry("900x600+100+30")
add_window.iconbitmap("add.ico")
add_window.configure(bg="pink")
f=("Arial",20,"bold")
aw_lbl_rno=Label(add_window,text="enter rno",font=f,bg="pink")
aw_lbl_rno.place(x=30,y=20)
aw_lbl_rno=Label(add_window,text="enter name",font=f,bg="pink")
aw_lbl_rno.place(x=30,y=120)
aw_lbl_rno=Label(add_window,text="enter marks",font=f,bg="pink")
aw_lbl_rno.place(x=30,y=220)
aw_ent_rno=Entry(add_window,font=f)
aw_ent_rno.place(x=230,y=20)
aw_ent_name=Entry(add_window,font=f)
aw_ent_name.place(x=230,y=120)
aw_ent_marks=Entry(add_window,font=f)
aw_ent_marks.place(x=230,y=220)
aw_btn_save=Button(add_window,text="Save",font=f,bd=3)
aw_btn_save.place(x=300,y=400)
aw_btn_save=Button(add_window,text="Back",font=f,bd=3,command=f2)
aw_btn_save.place(x=300,y=500)
add_window.withdraw()


main_window.mainloop()