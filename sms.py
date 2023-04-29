from tkinter import *
import requests
from tkinter.scrolledtext import *
from tkinter.messagebox import *
from sqlite3 import *
from datetime import *

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
def f3():
	update_window.deiconify()
	main_window.withdraw()
def f4():
	main_window.deiconify()
	update_window.withdraw()
def f5():
	delete_window.deiconify()
	main_window.withdraw()
def f6():
	main_window.deiconify()
	delete_window.withdraw()
def f7():
	view_window.deiconify()
	main_window.withdraw()
	con=None
	try:
		con=connect("sms.db")
		cursor=con.cursor()
		sql="select * from student"
		cursor.execute(sql)
		msg=""
		data=cursor.fetchall()
		for d in data:	
			msg=msg+"rno: "+str(d[0])+", name: "+str(d[1])+", marks: "+str(d[2])+"\n"
		st_data.insert(INSERT,msg)
	except Exception as e:
		showerror("Failure",str(e))
	finally:
		if con is not None:
			con.close()
def f8():
	main_window.deiconify()
	view_window.withdraw()
def f9():
	con=None
	try:
		con=connect("sms.db")
		cursor=con.cursor()
		rno=int(aw_ent_rno.get());	name=aw_ent_name.get();	marks=int(aw_ent_marks.get());
		if rno<=0:
			showwarning("Wrong input","rno should be +ve")
			con.rollback()
		elif len(name)<2 or not(name.isalpha()):
			showwarning("Wrong input","name should be letters only")
			con.rollback()
		elif marks<0 or marks>100:
			showwarning("Wrong input","marks should be b/w 0 and 100")
			con.rollback()	
		else:
			sql="insert into student values('%d','%s','%d')"
			cursor.execute(sql%(rno,name,marks))
			con.commit()
			showinfo("Success","Record created")
	except ValueError:
		con.rollback()
		showerror("Wrong input","invalid rno/marks")
	except Exception as e:
		con.rollback()
		showerror("Failure",str(e))
	finally:
		if con is not None:
			con.close()
	aw_ent_rno.delete(0,END)
	aw_ent_name.delete(0,END)
	aw_ent_marks.delete(0,END)
	aw_ent_rno.focus()
def f10():
	con=None
	try:
		con=connect("sms.db")
		cursor=con.cursor()
		sql="delete from student where rno='%d'"
		rno=int(dw_ent_rno.get())
		if rno<=0:
			showwarning("Wrong input","rno should be +ve")
			con.rollback()
		else:
			cursor.execute(sql%(rno))
			if cursor.rowcount==1:
				con.commit()
				showinfo("Success","Record deleted")
			else:
				showinfo("No record","Record dne")
	except ValueError:
		con.rollback();
		showerror("Wrong input","Invalid rno")
	except Exception as e:
		con.rollback()
		showerror("Failure",str(e))
	finally:
		if con is not None:
			con.close()
	dw_ent_rno.delete(0,END)
def f11():
	con=None
	try:
		con=connect("sms.db")
		cursor=con.cursor()
		sql="update student set name='%s', marks='%d' where rno='%d'"
		rno=int(uw_ent_rno.get());	
		name=uw_ent_name.get();		
		marks=int(uw_ent_marks.get())
		if rno<=0:
			showwarning("Wrong input","rno should be +ve")
			con.rollback()
		elif len(name)<2 or not(name.isalpha()):
			showwarning("Wrong input","Name should have letters only")
			con.rollback()
		elif marks<0 or marks>100:
			showwarning("Wrong input","Marks should be between 0 and 100 only")
		else:
			cursor.execute(sql%(name,marks,rno))
			if cursor.rowcount==1:
				con.commit()
				showinfo("Success","Record updated")
			else:
				showinfo("No record","Record dne")
	except ValueError:
		con.rollback()
		showerror("Wrong input","Invalid rno/marks")
	except Exception as e:
		con.rollback()
		showerror("Failure",str(e))
	finally:
		if con is not None:
			con.close()
	uw_ent_rno.delete(0,END)
	uw_ent_name.delete(0,END)
	uw_ent_marks.delete(0,END)



btnAdd=Button(main_window,text="Add",font=f,bd=3,command=f1)
btnAdd.place(x=350,y=10)
btnView=Button(main_window,text="View",font=f,bd=3,command=f7)
btnView.place(x=350,y=110)
btnUpdate=Button(main_window,text="Update",font=f,bd=3,command=f3)
btnUpdate.place(x=350,y=210)
btnDelete=Button(main_window,text="Delete",font=f,bd=3,command=f5)
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

d=datetime.now()
dt=str(d.day)+" "+d.strftime("%B")+" "+str(d.year)
lblDate=Label(main_window,text="Date:"+dt,font=f,bg="pink")
lblDate.place(x=600,y=500)

add_window=Toplevel(main_window)
add_window.title("Add")
add_window.geometry("900x600+100+30")
add_window.iconbitmap("add.ico")
add_window.configure(bg="lightyellow")
f=("Arial",20,"bold")
aw_lbl_rno=Label(add_window,text="enter rno",font=f,bg="lightyellow")
aw_lbl_rno.place(x=100,y=20)
aw_lbl_rno=Label(add_window,text="enter name",font=f,bg="lightyellow")
aw_lbl_rno.place(x=100,y=120)
aw_lbl_rno=Label(add_window,text="enter marks",font=f,bg="lightyellow")
aw_lbl_rno.place(x=100,y=220)
aw_ent_rno=Entry(add_window,font=f)
aw_ent_rno.place(x=300,y=20)
aw_ent_name=Entry(add_window,font=f)
aw_ent_name.place(x=300,y=120)
aw_ent_marks=Entry(add_window,font=f)
aw_ent_marks.place(x=300,y=220)
aw_btn_save=Button(add_window,text="Save",font=f,bd=3,command=f9)
aw_btn_save.place(x=360,y=400)
aw_btn_back=Button(add_window,text="Back",font=f,bd=3,command=f2)
aw_btn_back.place(x=360,y=500)
add_window.withdraw()

view_window=Toplevel(main_window)
view_window.title("View")
view_window.geometry("900x600+100+30")
view_window.iconbitmap("view.ico")
view_window.configure(bg="violet")
f=("Arial",20,"bold")
vw_btn_back=Button(view_window,text="Back",font=f,bd=3,command=f8)
st_data=ScrolledText(view_window,width=45,height=15,font=f)
st_data.place(x=100,y=10)
#st_data.configure(state='disabled')
vw_btn_back.place(x=360,y=500)
view_window.withdraw()

update_window=Toplevel(main_window)
update_window.title("Update")
update_window.geometry("900x600+100+30")
update_window.iconbitmap("add.ico")
update_window.configure(bg="lightgreen")
f=("Arial",20,"bold")
uw_lbl_rno=Label(update_window,text="enter rno",font=f,bg="lightgreen")
uw_lbl_rno.place(x=100,y=20)
uw_lbl_rno=Label(update_window,text="enter name",font=f,bg="lightgreen")
uw_lbl_rno.place(x=100,y=120)
uw_lbl_rno=Label(update_window,text="enter marks",font=f,bg="lightgreen")
uw_lbl_rno.place(x=100,y=220)
uw_ent_rno=Entry(update_window,font=f)
uw_ent_rno.place(x=300,y=20)
uw_ent_name=Entry(update_window,font=f)
uw_ent_name.place(x=300,y=120)
uw_ent_marks=Entry(update_window,font=f)
uw_ent_marks.place(x=300,y=220)
uw_btn_save=Button(update_window,text="Save",font=f,bd=3,command=f11)
uw_btn_save.place(x=360,y=400)
uw_btn_back=Button(update_window,text="Back",font=f,bd=3,command=f4)
uw_btn_back.place(x=360,y=500)
update_window.withdraw()

delete_window=Toplevel(main_window)
delete_window.title("Delete")
delete_window.geometry("900x600+100+30")
delete_window.iconbitmap("delete.ico")
delete_window.configure(bg="lightgrey")
f=("Arial",20,"bold")
dw_lbl_rno=Label(delete_window,text="enter rno",font=f,bg="lightgrey")
dw_lbl_rno.place(x=100,y=20)
dw_ent_rno=Entry(delete_window,font=f)
dw_ent_rno.place(x=300,y=20)
dw_btn_save=Button(delete_window,text="Delete",font=f,bd=3,command=f10)
dw_btn_save.place(x=360,y=400)
dw_btn_back=Button(delete_window,text="Back",font=f,bd=3,command=f6)
dw_btn_back.place(x=360,y=500)
delete_window.withdraw()

main_window.mainloop()