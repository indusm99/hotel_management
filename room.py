from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strptime
from datetime import datetime
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
class roombooking:
    def __init__ (self,root):
        self.root=root
        self.root.title("hotel management system")
        self.root.geometry("1100x500+190+180")

        #========== variables============
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()

        #=========== title =================
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),bg="grey",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

         #================ logo===============
        img2=Image.open(r"C:\Users\INDIRA S\OneDrive\Desktop\pro\images\logo1.jpg")
        img2=img2.resize((100,40),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        #====== label frame ==================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="ROOM BOOKING",font=("times new roman",12,"bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=400,height=490)

        #=========== label and entries==================
        #custref
        lbl_cust_contact=Label(labelframeleft,text="Customer contact:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(labelframeleft,width=20,textvariable=self.var_contact,font=("times new roman",13,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)

        #fetch data button
        btnfetchdata=Button(labelframeleft,text="Fetch data",command=self.fetch_contact,font=("times new roman",8,"bold"),bg="grey",fg="gold",width=8)
        btnfetchdata.place(x=320,y=4)

        #check-in -date
        check_in_date=Label(labelframeleft,text="Check_in date:",font=("times new roman",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)

        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=29,font=("times new roman",13,"bold"))
        txtcheck_in_date.grid(row=1,column=1)

        #check_out date
        lbl_chech_out=Label(labelframeleft,text="Check_out date:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_chech_out.grid(row=2,column=0,sticky=W)

        txtcheck_out_date=ttk.Entry(labelframeleft,width=29,textvariable=self.var_checkout,font=("times new roman",13,"bold"))
        txtcheck_out_date.grid(row=2,column=1)

        #room type
        label_roomtype=Label(labelframeleft,text="Room type:",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_roomtype.grid(row=3,column=0,sticky=W)

        combo_roomtype=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,width=27,font=("times new roman",13,"bold"),state="readonly")
        combo_roomtype["value"]=("single","double","laxary")
        combo_roomtype.current(0)
        combo_roomtype.grid(row=3,column=1)

        #Available room
        lblroomavailable=Label(labelframeleft,text="Available room:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblroomavailable.grid(row=4,column=0,sticky=W)

        txtroomavailable=ttk.Entry(labelframeleft,width=29,textvariable=self.var_roomavailable, font=("times new roman",13,"bold"))
        txtroomavailable.grid(row=4,column=1)

        #Meal
        lblMeal=Label(labelframeleft,text="Meal:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)

        txtmeal=ttk.Entry(labelframeleft,width=29,textvariable=self.var_meal,font=("times new roman",13,"bold"))
        txtmeal.grid(row=5,column=1)

        #no of days
        lblnoofdays=Label(labelframeleft,text="No of Days:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblnoofdays.grid(row=6,column=0,sticky=W)

        txtnoofdays=ttk.Entry(labelframeleft,width=29,textvariable=self.var_noofdays,font=("times new roman",13,"bold"))
        txtnoofdays.grid(row=6,column=1)

        #Mpaid tax
        lblnoofdays=Label(labelframeleft,text="paid tax:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblnoofdays.grid(row=7,column=0,sticky=W)

        lblnoofdays=ttk.Entry(labelframeleft,width=29,textvariable=self.var_paidtax,font=("times new roman",13,"bold"))
        lblnoofdays.grid(row=7,column=1)

        #sub tax
        lblnoofdays=Label(labelframeleft,text="Sub total:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblnoofdays.grid(row=8,column=0,sticky=W)

        lblnoofdays=ttk.Entry(labelframeleft,width=29,textvariable=self.var_actualtotal,font=("times new roman",13,"bold"))
        lblnoofdays.grid(row=8,column=1)

        #total cost
        lblidnumber=Label(labelframeleft,text="Total tax:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblidnumber.grid(row=9,column=0,sticky=W)

        lblnoofdays=ttk.Entry(labelframeleft,width=29,textvariable=self.var_total,font=("times new roman",13,"bold"))
        lblnoofdays.grid(row=9,column=1)

        #======= bill button ===
        btnbill=Button(labelframeleft,text="bill",command=self.total,font=("times new roman",11,"bold"),bg="grey",fg="gold",width=10)
        btnbill.grid(row=10,column=0,padx=1,sticky=W)

        #================= btns ============
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="ADD",command=self.add_data,font=("times new roman",11,"bold"),bg="grey",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("times new roman",11,"bold"),bg="grey",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mdelete,font=("times new roman",11,"bold"),bg="grey",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("times new roman",11,"bold"),bg="grey",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        #=================== rightside image==============
        img3=Image.open(r"C:\Users\INDIRA S\OneDrive\Desktop\pro\images\ima.jpeg")
        img3=img3.resize((300,300),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=760,y=55,width=300,height=300)


        #========= table frame ============
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="VIEW DETAILS AND SEARCH SYSTEM",font=("times new roman",12,"bold"),padx=2,)
        table_frame.place(x=420,y=280,width=800,height=260)

        lblSearchBy=Label(table_frame,text="SearchBy",font=("times new roman",12,"bold"),bg="grey",fg="gold")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_Search=ttk.Combobox(table_frame,width=20,textvariable=self.search_var,font=("times new roman",12,"bold"),state="readonly")
        combo_Search["values"]=("Contact","Roomavailable")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(table_frame,width=20,textvariable=self.txt_search,font=("times new roman",13,"bold"))
        txtSearch.grid(row=0,column=2,padx=1)

        btnSearch=Button(table_frame,text="Search",command=self.search,font=("times new roman",11,"bold"),bg="grey",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowall=Button(table_frame,text="ShowAll",command=self.fetch_data,font=("times new roman",11,"bold"),bg="grey",fg="gold",width=10)
        btnShowall.grid(row=0,column=4,padx=1)


        #=========== data table ==============
        details_table=Frame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=170)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table = ttk.Treeview(
            details_table, 
            columns=("contact", "checkin", "checkout", "roomtype", "roomavailable", "meal", "noofdays"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        # Your other code here to setup columns, headings, etc.
        self.room_table.heading("contact", text="Contact")
        self.room_table.heading("checkin", text="Checkin")
        self.room_table.heading("checkout", text="Checkout")
        self.room_table.heading("roomtype", text="Room type")
        self.room_table.heading("roomavailable", text="Room Available")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noofdays", text="NoOfDays")
        
        self.room_table['show'] = 'headings'
        
        # Set column widths if desired
        self.room_table.column("contact", width=100)
        self.room_table.column("checkin", width=100)
        self.room_table.column("checkout", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("noofdays", width=100)

        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    # ====== add data ========
    def add_data(self):
        if self.var_contact.get()==" " or self.var_checkin.get()==" ":
            messagebox.showerror("error","All fields are reduired",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="rujusmitha@99",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_contact.get(),
                                                                                self.var_checkin.get(),
                                                                                self.var_checkout.get(),
                                                                                self.var_roomtype.get(),
                                                                                self.var_roomavailable.get(),
                                                                                self.var_meal.get(),
                                                                                self.var_noofdays.get()
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("sucess","room booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong:{str(es)}",parent=self.root)

    #============ fetch data ==========
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="rujusmitha@99",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=" "):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])

    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("error","please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="rujusmitha@99",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set checkin=%s,checkout=%s,roomtype=%s,roomavailable=%s,meal=%s,noofdays=%s where contact=%s",(
                                                                                                                        self.var_checkin.get(),
                                                                                                                        self.var_checkout.get(),
                                                                                                                        self.var_roomtype.get(),
                                                                                                                        self.var_roomavailable.get(),
                                                                                                                        self.var_meal.get(),
                                                                                                                        self.var_noofdays.get(),
                                                                                                                        self.var_contact.get(),
                                                                                                                                                                    
                                                                                                                                                                ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("update","room details has been updated successfully",parent=self.root)

    def mdelete(self):
        mdelete=messagebox.askyesno("Hotel management system","do u want delete this room",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="rujusmitha@99",database="management")
            my_cursor=conn.cursor()
            query="delete from room where contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_contact.set(" ")
        self.var_checkin.set(" ")
        self.var_checkout.set(" ")
        self.var_roomtype.set(" ")
        self.var_roomavailable.set(" ")
        self.var_meal.set(" ")
        self.var_noofdays.set(" ")
        self.var_paidtax.set(" ")
        self.var_actualtotal.set(" ")
        self.var_total.set(" ")

    #============ all data fetch==========
    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("error","please enter contact number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="rujusmitha@99",database="management")
            my_cursor=conn.cursor()
            query=("select name from customer where mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("error","this number not found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showdataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showdataframe.place(x=430,y=70,width=300,height=180)

                lblname=Label(showdataframe,text="Name:",font=("times new roman",12,"bold"))
                lblname.place(x=0,y=0)

                lbl=Label(showdataframe,text=row,font=("times new roman",12,"bold"))
                lbl.place(x=90,y=0)
                #=============gender===========
                conn=mysql.connector.connect(host="localhost",username="root",password="rujusmitha@99",database="management")
                my_cursor=conn.cursor()
                query=("select gender from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblgender=Label(showdataframe,text="Gender:",font=("times new roman",12,"bold"))
                lblgender.place(x=0,y=30)

                lbl2=Label(showdataframe,text=row,font=("times new roman",12,"bold"))
                lbl2.place(x=90,y=30)

                #============= email ===========
                conn=mysql.connector.connect(host="localhost",username="root",password="rujusmitha@99",database="management")
                my_cursor=conn.cursor()
                query=("select email from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblemail=Label(showdataframe,text="Email:",font=("times new roman",12,"bold"))
                lblemail.place(x=0,y=60)

                lbl3=Label(showdataframe,text=row,font=("times new roman",12,"bold"))
                lbl3.place(x=90,y=60)

                #============= nationality===========
                conn=mysql.connector.connect(host="localhost",username="root",password="rujusmitha@99",database="management")
                my_cursor=conn.cursor()
                query=("select nationality from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblnationality=Label(showdataframe,text="Nationality:",font=("times new roman",12,"bold"))
                lblnationality.place(x=0,y=90)

                lbl4=Label(showdataframe,text=row,font=("times new roman",12,"bold"))
                lbl4.place(x=90,y=90)

                #============ address ===========
                conn=mysql.connector.connect(host="localhost",username="root",password="rujusmitha@99",database="management")
                my_cursor=conn.cursor()
                query=("select address from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lbladdress=Label(showdataframe,text="Address:",font=("times new roman",12,"bold"))
                lbladdress.place(x=0,y=120)

                lbl5=Label(showdataframe,text=row,font=("times new roman",12,"bold"))
                lbl5.place(x=90,y=120)

    #==========search =====
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="rujusmitha@99",database="management")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        #query = f"SELECT * FROM customer WHERE {search_column} LIKE %s"
        #value = f"%{search_value}%"
        #my_cursor.execute(query, (value,))
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
                print(i)
        else:
            messagebox.showinfo("No Results", "No matching records found.")
            conn.commit()
        conn.close()

    # === total ==========
    def total(self):
        indate=self.var_checkin.get()
        outdate=self.var_checkout.get()
        indate=datetime.strptime(indate,"%d/%m/%Y")
        outdate=datetime.strptime(outdate,"%d/%m/%Y")

        self.var_noofdays.set(abs(outdate-indate).days)
        
        if self.var_meal.get() == "breakfast" and self.var_roomtype.get() == "laxary":
            q1 = 300.0
            q2 = 700.0
            q3 = float(self.var_noofdays.get())
            q4 = q1 + q2
            q5 = q4 * q3  # Adjust this line to calculate the total for the number of days
            tax_amount = q5 * 0.1
            total_amount = q5 + tax_amount
            Tax = "Rs. {:.2f}".format(tax_amount)
            ST = "Rs. {:.2f}".format(q5)
            TT = "Rs. {:.2f}".format(total_amount)
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif self.var_meal.get() == "lunch" and self.var_roomtype.get() == "single":
            q1 = 300.0
            q2 = 700.0
            q3 = float(self.var_noofdays.get())
            q4 = q1 + q2
            q5 = q4 * q3  # Adjust this line to calculate the total for the number of days
            tax_amount = q5 * 0.1
            total_amount = q5 + tax_amount
            Tax = "Rs. {:.2f}".format(tax_amount)
            ST = "Rs. {:.2f}".format(q5)
            TT = "Rs. {:.2f}".format(total_amount)
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        



    

    

if __name__=="__main__":
    root=Tk()
    obj= roombooking(root)
    root.mainloop()
