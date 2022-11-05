from tkinter import *
from tkinter import messagebox
import random
root=Tk()
root.geometry("600x600")
f_name=StringVar()
l_name=StringVar()
email=StringVar()
address=StringVar()
zip=IntVar()
state=Menubutton()
var=StringVar(root,"")
cb1_var=StringVar()
cb2_var=StringVar()
cb3_var=StringVar()
cb4_var=StringVar()

def add():
    a=f_name.get()
    b=l_name.get()
    c=email.get()
    d=address.get()
    e=zip.get()
    f=state.get()
    g=cb1_var.get()
    h=cb2_var.get()
    i=cb3_var.get()
    j=cb4_var.get()
    r=[a,b,c,d,e,f,g,h,i,j]
    li2.insert(END,r)
    
def delete():  
    li1.delete(li1.curselection)

def theme():
    root.config(background="red")  
        
messagebox.showinfo("Insertion","Name should not contain number")
messagebox.showerror("Validation","Email should contain @")
messagebox.showwarning("Deletion","Zip Code should be a number")

li1=Listbox(root,font=("Arial",16),width=30,height=25)
li1.place(x=50,y=50)

l1=Label(root,text="First Name: ",font=("Arial",10 ,'bold'))
l1.place(x=60,y=70)

lb1=Entry(root,textvariable=l1,bg="white")
lb1.place(x=150,y=70)

l2=Label(root,text="Last Name: ",font=("Arial",10 ,'bold'))
l2.place(x=60,y=100)

lb2=Entry(root,textvariable=l2,bg="white")
lb2.place(x=150,y=100)

l3=Label(root,text=("Gender: "),font=("Arial",10 ,'bold'))
l3.place(x=60,y=130)

r1=Radiobutton(root,text="Male",variable=var,value="male")
r1.place(x=150,y=130)

r2=Radiobutton(root,text="Female",variable=var,value="female")
r2.place(x=220,y=130)

l4=Label(root,text="Languages",font=("Arial",10 ,'bold')).place(x=60,y=160)

c1=Checkbutton(root,text="Telegu",variable=cb1_var,onvalue="Telegu").place(x=150,y=160)
c2=Checkbutton(root,text="English",variable=cb1_var,onvalue="English").place(x=230,y=160)
c3=Checkbutton(root,text="Hindi",variable=cb1_var,onvalue="Hindi").place(x=310,y=160)

l5=Label(root,text=("Email: "),font=("Arial",10 ,'bold')).place(x=60,y=190)
lb3=Entry(root,textvariable=l5,bg="white")
lb3.place(x=150,y=190)

l6=Label(root,text=("Address: "),font=("Arial",10 ,'bold')).place(x=60,y=220)
lb4=Entry(root,textvariable=l6,bg="white")
lb4.place(x=150,y=220)

l7=Label(root,text=("State: "),font=("Arial",10 ,'bold')).place(x=60,y=250)
m1=Menubutton(root,text="Choose State").place(x=150,y=250)

l8=Label(root,text=("Zip: "),font=("Arial",10 ,'bold')).place(x=60,y=280)
lb5=Entry(root,textvariable=l8,bg="white").place(x=150,y=280)

l9=Label(root,text="Credit: ",font=("Arial",10 ,'bold')).place(x=60,y=310)
m2=Menubutton(root,text="Choose Card Type").place(x=150,y=310)

b1=Button(root,text="Insert",font=("Arail",10,'bold'),command=add).place(x=500,y=90)

b2=Button(root,text="Delete",font=("Arail",10,'bold'),command=delete).place(x=500,y=150)

b3=Button(root,text="Theme",font=("Arail",10,'bold'),command=theme).place(x=500,y=210)



li2=Listbox(root,font=("Arial",16),width=30,height=25)
li2.place(x=600,y=50)
li2.insert(1,"BILLING RECORDS")
root.mainloop()