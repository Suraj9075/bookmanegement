from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Manegement System")
        self.root.geometry("1350x690+0+0")

#===============================Variable====================
        self.member_var=StringVar()
        self.bookid_var=StringVar()
        self.bookname_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.rollno_var=StringVar()
        self.mobile_var=StringVar()
        self.DateBorrowed_var=StringVar()
        self.DateDue_var=StringVar()
        self.DaysonBook_var=StringVar()
        self.LateReturnFine_var=StringVar()
        self.DateOverDue_var=StringVar()
        self.FinalPrice_var=StringVar()


        lbltitle=Label(self.root,text="LIBRARY MANEMENT SYSTEM",bg="powder blue",fg="green",bd=10,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)
        
        frame=Frame(self.root, bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=100,width=1350,height=400)

#==========================Data Frame===========================

        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="green",bd=10,relief=RIDGE,font=("times new roman",12,"bold"),padx=2,pady=6)
        DataFrameLeft.place(x=0,y=3,width=800,height=350)

        lblMember=Label(DataFrameLeft,bg="powder blue",font=("Times new roman",15,"bold"),text="Member Type",padx=2,pady=3)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("Times new roman",15,),width=20,state="readonly")
        comMember["values"]=("Teachar","Student")
        comMember.grid(row=0,column=1)

        
        lblBookID=Label(DataFrameLeft,bg="powder blue",text="Book ID",font=("Times new roman",15,"bold"),padx=2,pady=3)
        lblBookID.grid(row=1,column=0,sticky=W)
        txtBookID=Entry(DataFrameLeft,textvariable=self.bookid_var,font=("times new roman",15,"bold"),width=22)
        txtBookID.grid(row=1,column=1)

        lblBookName=Label(DataFrameLeft,bg="powder blue",text="Book Name",font=("Times new roman",15,"bold"),padx=2,pady=3)
        lblBookName.grid(row=2,column=0,sticky=W)
        txtBookName=Entry(DataFrameLeft,textvariable=self.bookname_var,font=("times new roman",15,"bold"),width=22)
        txtBookName.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,bg="powder blue",text="First Name",font=("Times new roman",15,"bold"),padx=2,pady=3)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,textvariable=self.firstname_var,font=("times new roman",15,"bold"),width=22)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,bg="powder blue",text="Last Name",font=("Times new roman",15,"bold"),padx=2,pady=3)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,textvariable=self.lastname_var,font=("times new roman",15,"bold"),width=22)
        txtLastName.grid(row=4,column=1)

        lblRollNo=Label(DataFrameLeft,bg="powder blue",text="Roll NO",font=("Times new roman",15,"bold"),padx=2,pady=3)
        lblRollNo.grid(row=5,column=0,sticky=W)
        txtRollNo=Entry(DataFrameLeft,textvariable=self.rollno_var,font=("times new roman",15,"bold"),width=22)
        txtRollNo.grid(row=5,column=1)

        lblMobile=Label(DataFrameLeft,bg="powder blue",text="Mobile No",font=("Times new roman",15,"bold"),padx=2,pady=3)
        lblMobile.grid(row=6,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,textvariable=self.mobile_var,font=("times new roman",15,"bold"),width=22)
        txtMobile.grid(row=6,column=1)

        lblDateBorrowed=Label(DataFrameLeft,bg="powder blue",text="Date Borrowed",font=("Times new roman",15,"bold"),padx=2,pady=3)
        lblDateBorrowed.grid(row=7,column=0,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,textvariable=self.DateBorrowed_var,font=("times new roman",15,"bold"),width=22)
        txtDateBorrowed.grid(row=7,column=1)


        lblDateDue=Label(DataFrameLeft,bg="powder blue",text="Date Due",font=("Times new roman",15,"bold"),padx=2,pady=3)
        lblDateDue.grid(row=8,column=0,sticky=W)
        txtDateDue=Entry(DataFrameLeft,textvariable=self.DateDue_var,font=("times new roman",15,"bold"),width=22)
        txtDateDue.grid(row=8,column=1)

        lblDaysonBook=Label(DataFrameLeft,bg="powder blue",text="Days on Book",font=("Times new roman",15,"bold"),padx=2,pady=3)
        lblDaysonBook.grid(row=0,column=3,sticky=W)
        txtDaysonBook=Entry(DataFrameLeft,textvariable=self.DaysonBook_var,font=("times new roman",15,"bold"),width=22)
        txtDaysonBook.grid(row=0,column=4)

        lblLateReturnFine=Label(DataFrameLeft,bg="powder blue",text="Late Return Fine",font=("Times new roman",15,"bold"),padx=2,pady=3)
        lblLateReturnFine.grid(row=1,column=3,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,textvariable=self.LateReturnFine_var,font=("times new roman",15,"bold"),width=22)
        txtLateReturnFine.grid(row=1,column=4)

        lblDateOverDue=Label(DataFrameLeft,bg="powder blue",text="Date Over Due",font=("Times new roman",15,"bold"),padx=2,pady=3)
        lblDateOverDue.grid(row=2,column=3,sticky=W)
        txtDateOverDue=Entry(DataFrameLeft,textvariable=self.DateOverDue_var,font=("times new roman",15,"bold"),width=22)
        txtDateOverDue.grid(row=2,column=4)

        lblActualPrice=Label(DataFrameLeft,bg="powder blue",text="Actual Price",font=("Times new roman",15,"bold"),padx=2,pady=3)
        lblActualPrice.grid(row=3,column=3,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,textvariable=self.FinalPrice_var,font=("times new roman",15,"bold"),width=22)
        txtActualPrice.grid(row=3,column=4)

#===================================FrameRight=================================

        DataFrameRight=LabelFrame(frame,text="Book deatails",bg="powder blue",fg="green",bd=10,relief=RIDGE,font=("times new roman",12,"bold"),padx=2,pady=6)
        DataFrameRight.place(x=810,y=3,width=475,height=350)


        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=28,height=15,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollBar=Scrollbar(DataFrameRight)
        listScrollBar.grid(row=0,column=1,sticky="ns")


        listBooks=['COD','DBMS','programming in python','Discrete Mathematics','Computer Graphics','c++ programming',
                   'Java Programming','Database management Systems','software Engineering','c Programming']

        def Selectbook(event=""):
                value=str(listbox.get(listbox.curselection()))
                x=value
                if(x=="COD"):
                        self.bookid_var.set("Bk1001")
                        self.bookname_var.set("COD")

                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2

                        self.DateBorrowed_var.set(d1)
                        self.DateDue_var.set(d3)
                        self.DaysonBook_var.set(15)
                        self.LateReturnFine_var.set("Rs.10")
                        self.DateOverDue_var.set("NO")
                        self.FinalPrice_var.set("Rs.100")

                elif(x=="DBMS"):
                        self.bookid_var.set("Bk1002")
                        self.bookname_var.set("DBMS")

                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2

                        self.DateBorrowed_var.set(d1)
                        self.DateDue_var.set(d3)
                        self.DaysonBook_var.set(15)
                        self.LateReturnFine_var.set("Rs.10")
                        self.DateOverDue_var.set("NO")
                        self.FinalPrice_var.set("Rs.125")

                elif(x=="programming in python"):
                        self.bookid_var.set("Bk1003")
                        self.bookname_var.set("programming in python")

                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2

                        self.DateBorrowed_var.set(d1)
                        self.DateDue_var.set(d3)
                        self.DaysonBook_var.set(15)
                        self.LateReturnFine_var.set("Rs.10")
                        self.DateOverDue_var.set("NO")
                        self.FinalPrice_var.set("Rs.100")

                elif(x=="Discrete Mathematics"):
                        self.bookid_var.set("Bk1004")
                        self.bookname_var.set("Discrete Mathematics")

                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2

                        self.DateBorrowed_var.set(d1)
                        self.DateDue_var.set(d3)
                        self.DaysonBook_var.set(15)
                        self.LateReturnFine_var.set("Rs.10")
                        self.DateOverDue_var.set("NO")
                        self.FinalPrice_var.set("Rs.100")
                
                elif(x=="Computer Graphics"):
                        self.bookid_var.set("Bk1005")
                        self.bookname_var.set("Computer Graphics")

                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2

                        self.DateBorrowed_var.set(d1)
                        self.DateDue_var.set(d3)
                        self.DaysonBook_var.set(15)
                        self.LateReturnFine_var.set("Rs.10")
                        self.DateOverDue_var.set("NO")
                        self.FinalPrice_var.set("Rs.100")
                
                elif(x=="c++ programming"):
                        self.bookid_var.set("Bk1006")
                        self.bookname_var.set("c++ programming")

                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2

                        self.DateBorrowed_var.set(d1)
                        self.DateDue_var.set(d3)
                        self.DaysonBook_var.set(15)
                        self.LateReturnFine_var.set("Rs.10")
                        self.DateOverDue_var.set("NO")
                        self.FinalPrice_var.set("Rs.154")

                elif(x=="Java Programming"):
                        self.bookid_var.set("Bk1007")
                        self.bookname_var.set("Java Programming")

                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2

                        self.DateBorrowed_var.set(d1)
                        self.DateDue_var.set(d3)
                        self.DaysonBook_var.set(15)
                        self.LateReturnFine_var.set("Rs.10")
                        self.DateOverDue_var.set("NO")
                        self.FinalPrice_var.set("Rs.145")

                elif(x=="Database management Systems"):
                        self.bookid_var.set("Bk1008")
                        self.bookname_var.set("Database management Systems")

                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2

                        self.DateBorrowed_var.set(d1)
                        self.DateDue_var.set(d3)
                        self.DaysonBook_var.set(15)
                        self.LateReturnFine_var.set("Rs.10")
                        self.DateOverDue_var.set("NO")
                        self.FinalPrice_var.set("Rs.135")

                elif(x=="software Engineering"):
                        self.bookid_var.set("Bk1009")
                        self.bookname_var.set("software Engineering")

                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2

                        self.DateBorrowed_var.set(d1)
                        self.DateDue_var.set(d3)
                        self.DaysonBook_var.set(15)
                        self.LateReturnFine_var.set("Rs.10")
                        self.DateOverDue_var.set("NO")
                        self.FinalPrice_var.set("Rs.130")
                
                elif(x=="c Programming"):
                        self.bookid_var.set("Bk1010")
                        self.bookname_var.set("c Programming")

                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2

                        self.DateBorrowed_var.set(d1)
                        self.DateDue_var.set(d3)
                        self.DaysonBook_var.set(15)
                        self.LateReturnFine_var.set("Rs.10")
                        self.DateOverDue_var.set("NO")
                        self.FinalPrice_var.set("Rs.150")
                


        listbox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=18,height=15)
        listbox.bind("<<ListboxSelect>>",Selectbook)
        listbox.grid(row=0,column=0,padx=4)
        listScrollBar.config(command=listbox.yview)
        
        for items in listBooks:
                listbox.insert(END,items)
 
#================================frame buttons======================================

        framebutton=Frame(self.root, bd=10,relief=RIDGE,padx=20,bg="powder blue")
        framebutton.place(x=0,y=500,width=1350,height=70)

        btnAddData=Button(framebutton,command=self.adda_data,text="ADD DATA",font=("arial",12,"bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnShowData=Button(framebutton,command=self.showData,text="SHOW DATA",font=("arial",12,"bold"),width=20,bg="blue",fg="white")
        btnShowData.grid(row=0,column=1)

        btnUpdate=Button(framebutton,command=self.update,text="UPDATE",font=("arial",12,"bold"),width=20,bg="blue",fg="white")
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(framebutton,command=self.delete,text="DELETE",font=("arial",12,"bold"),width=20,bg="blue",fg="white")
        btnDelete.grid(row=0,column=3)

        btnReset=Button(framebutton,command=self.reset,text="RESET",font=("arial",12,"bold"),width=20,bg="blue",fg="white")
        btnReset.grid(row=0,column=4)

        btnExit=Button(framebutton,command=self.iExit,text="EXIT",font=("arial",12,"bold"),width=20,bg="blue",fg="white")
        btnExit.grid(row=0,column=5)

#================================frame information================================
        
        frameDetails=Frame(self.root, bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frameDetails.place(x=0,y=535,width=1350,height=150)

        Tableframe=Frame(frameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Tableframe.place(x=0,y=2,width=1290,height=120)

        xscroll=ttk.Scrollbar(Tableframe,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Tableframe,orient=VERTICAL)

        self.libray_Table=ttk.Treeview(Tableframe,column=("MemberType","BookID","BookName","FirstName","LastName","RollNo","Mobile","DateBorrowed","DateDue","Days","LateReturnDate","DateOverDue","ActualPrice"),
        xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)




        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.libray_Table.xview)
        yscroll.config(command=self.libray_Table.yview)

        self.libray_Table.heading("MemberType",text="Member Type")
        self.libray_Table.heading("BookID",text="Book ID")
        self.libray_Table.heading("BookName",text="Book Name")
        self.libray_Table.heading("FirstName",text="First Name")
        self.libray_Table.heading("LastName",text="Last Name")
        self.libray_Table.heading("RollNo",text="Roll No")
        self.libray_Table.heading("Mobile",text="Mobile No")
        self.libray_Table.heading("DateBorrowed",text="DateBorrowed")
        self.libray_Table.heading("DateDue",text="DateDue")
        self.libray_Table.heading("Days",text="Days on Book")
        self.libray_Table.heading("LateReturnDate",text="LateReturnDate")
        self.libray_Table.heading("DateOverDue",text="DateOverDue")
        self.libray_Table.heading("ActualPrice",text="Actual Price")
       


        self.libray_Table["show"]="headings"
        self.libray_Table.pack(fill=BOTH,expand=1)

        self.libray_Table.column("MemberType",width=100)
        self.libray_Table.column("BookID",width=100)
        self.libray_Table.column("BookName",width=100) 
        self.libray_Table.column("FirstName",width=100) 
        self.libray_Table.column("LastName",width=100)
        self.libray_Table.column("RollNo",width=100)
        self.libray_Table.column("Mobile",width=100)
        self.libray_Table.column("DateBorrowed",width=100)
        self.libray_Table.column("DateDue",width=100)
        self.libray_Table.column("Days",width=100)
        self.libray_Table.column("LateReturnDate",width=100)
        self.libray_Table.column("DateOverDue", width=100)
        self.libray_Table.column("ActualPrice", width=100)

        self.fatch_data()
        self.libray_Table.bind("<ButtonRelease-1>",self.get_cursor)

    def adda_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="project")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (self.member_var.get(),
                        self.bookid_var.get(),
                        self.bookname_var.get(),
                        self.firstname_var.get(),
                        self.lastname_var.get(), 
                        self.rollno_var.get(),
                        self.mobile_var.get(),
                        self.DateBorrowed_var.get(),
                        self.DateDue_var.get(),
                        self.DaysonBook_var.get(),
                        self.LateReturnFine_var.get(),
                        self.DateOverDue_var.get(),
                        self.FinalPrice_var.get(),

                        ))

            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Success","Member has been inserted successfully")

   


    def fatch_data(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="project")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from library")
                rows=my_cursor.fetchall()

                if len(rows)!=0:
                        self.libray_Table.delete(*self.libray_Table.get_children())
                        for i in rows:
                                self.libray_Table.insert("",END,values=i)
                        conn.commit()
                conn.close()
    def get_cursor(self,event=""):
            cursor_rows=self.libray_Table.focus()
            content=self.libray_Table.item(cursor_rows)
            row=content['values']

            self.member_var.set(row[0])
            self.bookid_var.set(row[1])
            self.bookname_var.set(row[2])
            self.firstname_var.set(row[3])
            self.lastname_var.set(row[4])
            self.rollno_var.set(row[5])
            self.mobile_var.set(row[6])
            self.DateBorrowed_var.set(row[7])
            self.DateDue_var.set(row[8])
            self.DaysonBook_var.set(row[9])
            self.LateReturnFine_var.set(row[10])
            self.DateOverDue_var.set(row[11])
            self.FinalPrice_var.set(row[12])
            
    def showData(self):
            self.txtBox.insert(END,"Member Type:\t\t"+ self.member_var.get()+"\n")
            self.txtBox.insert(END,"BookId:\t\t"+ self.bookid_var.get()+"\n")
            self.txtBox.insert(END,"BookName:\t\t"+ self.bookname_var.get()+"\n")
            self.txtBox.insert(END,"FirstName:\t\t"+ self.firstname_var.get()+"\n")
            self.txtBox.insert(END,"LastName:\t\t"+ self.lastname_var.get()+"\n")
            self.txtBox.insert(END,"RollNO:\t\t"+ self.rollno_var.get()+"\n")
            self.txtBox.insert(END,"Mobile NO:\t\t"+ self.mobile_var.get()+"\n")
            self.txtBox.insert(END,"DateBorrowed:\t\t"+ self.DateBorrowed_var.get()+"\n")
            self.txtBox.insert(END,"DateDue:\t\t"+ self.DateDue_var.get()+"\n")
            self.txtBox.insert(END,"DaysonBook:\t\t"+ self.DaysonBook_var.get()+"\n")
            self.txtBox.insert(END,"LateReturnFine:\t\t"+ self.LateReturnFine_var.get()+"\n")
            self.txtBox.insert(END,"DateOverDue:\t\t"+ self.DateOverDue_var.get()+"\n")
            self.txtBox.insert(END,"FinalPrice:\t\t"+ self.FinalPrice_var.get()+"\n")
            
    def reset(self):
            self.member_var.set("")
            self.bookid_var.set("")
            self.bookname_var.set("")
            self.firstname_var.set("")
            self.lastname_var.set("")
            self.rollno_var.set("")
            self.mobile_var.set("")
            self.DateBorrowed_var.set("")
            self.DateDue_var.set("")
            self.DaysonBook_var.set("")
            self.LateReturnFine_var.set("")
            self.DateOverDue_var.set("")
            self.FinalPrice_var.set("")
            self.txtBox.delete("1.0,",END)

    def iExit(self):
            iExit=tkinter.messagebox.askyesno("Library management System","Do You Want To exit")
            if iExit>0:
                    self.root.destroy()
                    return
    def update(self):
             conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="project")
             my_cursor=conn.cursor()
             my_cursor.execute("update library set Member=%s,BookID=%s,BookName=%s,FirstName=%s,LastName=%s,RollNo=%s,Mobile=%s,DateBorrowed=%s,DateDue=%s,DaysonBook=%s,LateReturnFine=%s,DateOverDue=%s,FinalPrice=%s",
                                                  (self.member_var.get(),
                                                  self.bookid_var.get(),
                                                  self.bookname_var.get(),
                                                  self.firstname_var.get(),
                                                  self.lastname_var.get(),
                                                  self.rollno_var.get(),
                                                  self.mobile_var.get(),
                                                  self.DateBorrowed_var.get(),
                                                  self.DateDue_var.get(),
                                                  self.DaysonBook_var.get(),
                                                  self.LateReturnFine_var.get(),
                                                  self.DateOverDue_var.get(),
                                                  self.FinalPrice_var.get(),

                                                         ))
             conn.commit()
             self.fatch_data()
             self.reset()
             conn.close()

             messagebox.showinfo("Success","Member has been Update")
    def delete(self):
            if self.bookid_var.get()=="" or self.bookname_var.get()=="":
                    messagebox.showerror("Error","First select the Member")
            else:
                    conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="project")
                    my_cursor=conn.cursor()
                    query="delete from library where BookId=%s"
                    value=(self.bookid_var.get(),)
                    my_cursor.execute(query,value)

                    conn.commit()
                    self.fatch_data()
                    self.reset()
                    conn.close()

                    messagebox.showinfo("Success","Member has been Deleted")


if __name__ =="__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()