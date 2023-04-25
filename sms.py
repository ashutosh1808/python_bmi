from tkinter import *
import requests

main_window=Tk()
main_window.title("Student Management System")
main_window.geometry("800x500+100+30")
main_window.iconbitmap("edu.ico")
f=("Arial",20,"bold")

def f1():
	add_window.deiconify()
	main_window.withdraw()
def f2():
	main_window.deiconify()
	add_window.withdraw()

btnAdd=Button(main_window,text="Add",font=f,bd=3,command=f1)
btnAdd.pack(pady=10)
btnView=Button(main_window,text="View",font=f,bd=3)
btnView.pack(pady=10)
btnUpdate=Button(main_window,text="Update",font=f,bd=3)
btnUpdate.pack(pady=10)
btnDelete=Button(main_window,text="Delete",font=f,bd=3)
btnDelete.pack(pady=10)
btnPlot=Button(main_window,text="Plot",font=f,bd=3)
btnPlot.pack(pady=10)


add_window=Toplevel(main_window)
add_window.title("Add")
add_window.geometry("800x500+100+30")
add_window.iconbitmap("edu.ico")
f=("Arial",20,"bold")
btnBack=Button(add_window,text="Back",font=f,bd=3,command=f2)
btnBack.pack(pady=10)
add_window.withdraw()


main_window.mainloop()