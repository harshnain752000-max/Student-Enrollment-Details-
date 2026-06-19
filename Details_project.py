from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import mysql.connector as myc
import smtplib
root=Tk()
root.title("Details")
root.geometry("1050x650+45+50")
root.configure(bg="#55C91F")
root.resizable(False,False)

root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1,weight=1)

label=Label(root,text="Student Details",anchor="center",font=("Arial",50,'bold'))
label.grid(row=0,column=0,sticky="ew",columnspan=2,padx=30,pady=20)

lbl=Label(root,text="Name",font=("times new roman",20,'italic'))
lbl.grid(row=1,column=0,sticky="e",padx=10,pady=5)
e=Entry(root,width=30,font=20)
e.grid(row=1,column=1,sticky="w",padx=10,pady=5)

lbl2=Label(root,text="Course",font=("times new roman",20,'italic'))
lbl2.grid(row=2,column=0,sticky="e",padx=10,pady=5)
c=Entry(root,width=30,font=20)
c.grid(row=2,column=1,sticky="w",padx=10,pady=5)

style=Style()
style.theme_use('clam')
style.configure('TCombobox',foreground="#5613E8")
lbl3=Label(root,text="Hobbies",font=("times new roman",20,"italic"))
lbl3.grid(row=3,column=0,sticky="e",padx=10,pady=5)
hob=Combobox(root,width=30,font=20)
hob['values']=('Reading','Playing','Watching Movies','Coding')
hob.current(3)
hob.grid(row=3,column=1,sticky="w",padx=10,pady=5)

var=IntVar()
lab=Label(root,text="Gender",font=("times new roman",20,"italic"))
lab.grid(row=4,column=0,sticky="e",padx=10,pady=5)

gender_frame=Frame(root)
gender_frame.grid(row=4,column=1,sticky="w",padx=10,pady=5)

rad1=Radiobutton(gender_frame,text="Male",variable=var,value=1)
rad1.grid(row=4,column=1,padx=5,pady=5,sticky="w")
rad2=Radiobutton(gender_frame,text="Female",variable=var,value=2)
rad2.grid(row=4,column=1,padx=60,pady=5,sticky="w")
rad3=Radiobutton(gender_frame,text="Others",variable=var,value=3)
rad3.grid(row=4,column=1,padx=130,pady=5,sticky="w")

lbl4=Label(root,text="Father's name",font=("times new roman",20,'italic'))
lbl4.grid(row=5,column=0,sticky="e",padx=10,pady=5)
fat=Entry(root,width=30,font=20)
fat.grid(row=5,column=1,sticky="w",padx=10,pady=5)

lbl5=Label(root,text="Mother's name",font=("times new roman",20,'italic'))
lbl5.grid(row=6,column=0,sticky="e",padx=10,pady=5)
mat=Entry(root,width=30,font=20)
mat.grid(row=6,column=1,sticky="w",padx=10,pady=5)

lbl6=Label(root,text="Email",font=("times new roman",20,"italic"))
lbl6.grid(row=7,column=0,padx=10,pady=5,sticky="e")
email=Entry(root,width=30,font=20)
email.grid(row=7,column=1,sticky="w",padx=10,pady=5)

chk_var=BooleanVar()
chk=Checkbutton(root,text="I Agree",variable=chk_var,onvalue=True,offvalue=False,width=20)
chk.grid(row=8,column=0,columnspan=2,padx=10,pady=10)

def me():
    if e.get()=="":
        messagebox.showerror("Error","Name Required")
    elif c.get()=="":
        messagebox.showerror("Error","Course required")
    elif fat.get()=="":
        messagebox.showerror("Error","Father's name required")
    elif mat.get()=="":
        messagebox.showerror("Error","Mother's name required")
    elif email.get()=="":
        messagebox.showerror("Error","Email required")
    elif e.get()=="" and course.get()=="" and fat.get()=="" and mat.get()=="" and email.get()=="":
        messagebox.showerror("Error","All fields are required")
    elif var.get()==0:
        messagebox.showerror("Error","Tell Your Gender")
    elif chk_var.get()==False:
        messagebox.showerror("Error","Accept Terms and Aggrement")
    else:
        messagebox.showinfo("Success",f"{e.get()} enrolled in {c.get()}")
    
    Name=e.get()
    course=c.get()
    hobby=hob.get()
    Gender=var.get()
    Father=fat.get()
    Mother=mat.get()
    Email=email.get()
    print(Name,course,hobby,Gender,Father,Mother,Email)

    con=myc.connect(host="localhost",user="root",passwd="",database="test")
    cursor=con.cursor()
    sql="insert into student(Name,Course,hobby,Gender,Father_name,Mother_name,Email) values(%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql,(Name,course,hobby,Gender,Father,Mother,Email))
    con.commit()
    cursor.close()
    con.close()

    sender_email="harshnain752000@gmail.com"
    receiver_email="harshnain752000@gmail.com"
    sender_email_passwd="ijtw gtjj ljyg sxdc"
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(user=sender_email,password=sender_email_passwd)
    subject="Course Enrollment"
    message="You are successfully enrolled in the course"
    s.sendmail(from_addr=sender_email,to_addrs=receiver_email,msg=f"Subject:{subject}\n\n{message}")
    s.quit()
    print(f"Mail sent having")
    print(f"Subject={subject}")
    print(f"Content={message}")

def reset():
    e.delete(0,END)
    c.delete(0,END)
    hob.delete(0,END)
    fat.delete(0,END)
    mat.delete(0,END)
    email.delete(0,END)

style.configure('large.TButton',font=("Arial",12,"bold"))
b=Button(root,text="SUBMIT",command=me,style='large.TButton')
b.grid(row=9,column=0,pady=20,columnspan=2,padx=60)

but=Button(root,text="RESET",command=reset,style='large.TButton')
but.grid(row=9,column=0,pady=20,padx=20,sticky="e")

bat=Button(root,command=root.quit,text="Exit",style='large.TButton')
bat.grid(row=10,column=0,columnspan=2,pady=10)

root.mainloop()