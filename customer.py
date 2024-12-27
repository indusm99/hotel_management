from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox


class Cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #====== variables===========
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()


        #=========== title =================
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="grey",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

         #================ logo===============
        img2=Image.open(r"C:\Users\INDIRA S\OneDrive\Desktop\pro\images\logo1.jpg")
        img2=img2.resize((100,40),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)


        #====== label frame ==================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer details",font=("times new roman",12,"bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=400,height=490)

        #=========== label and entries==================
        #custref
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,width=29,textvariable=self.var_ref,font=("times new roman",13,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)

        #cust name
        ename=Label(labelframeleft,text="Name:",font=("times new roman",12,"bold"),padx=2,pady=6)
        ename.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width=29,font=("times new roman",13,"bold"))
        txtcname.grid(row=1,column=1)

        #mother name
        lblmname=Label(labelframeleft,text="Mother Name:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)
        txtmname=ttk.Entry(labelframeleft,width=29,textvariable=self.var_mother,font=("times new roman",13,"bold"))
        txtmname.grid(row=2,column=1)

        #gender comabox
        label_gender=Label(labelframeleft,text="Gender:",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,width=29,font=("times new roman",12,"bold"),state="readonly")
        combo_gender["values"]=("Male","Female","Others")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        #postcode
        lblPostCode=Label(labelframeleft,text="PostCode:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)
        txtPostCode=ttk.Entry(labelframeleft,textvariable=self.var_post,width=29,font=("times new roman",13,"bold"))
        txtPostCode.grid(row=4,column=1)

        #mobile number
        lblMobile=Label(labelframeleft,text="Mobile Number:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile=ttk.Entry(labelframeleft,width=29,textvariable=self.var_mobile,font=("times new roman",13,"bold"))
        txtMobile.grid(row=5,column=1)

        #email
        lblEmail=Label(labelframeleft,text="Email:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)
        txtEmail=ttk.Entry(labelframeleft,width=29,textvariable=self.var_email,font=("times new roman",13,"bold"))
        txtEmail.grid(row=6,column=1)

        #nationality
        lblNationality=Label(labelframeleft,text="Nationality:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)
        
        combo_Nationality=ttk.Combobox(labelframeleft,width=27,textvariable=self.var_nationality,font=("times new roman",12,"bold"),state="readonly")
        combo_Nationality["values"]=("Indian","American","British")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)

        #idproof type combobox
        lblIdProof=Label(labelframeleft,text="Id Proof type:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblIdProof.grid(row=8,column=0,sticky=W)

        combo_id=ttk.Combobox(labelframeleft,width=27,textvariable=self.var_id_proof,font=("times new roman",12,"bold"),state="readonly")
        combo_id["values"]=("Aadhaar Card","DrivingLicence","Passport")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)
        

        #id number
        lblIdNumber=Label(labelframeleft,text="Id Number:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,width=29,textvariable=self.var_id_number,font=("times new roman",13,"bold"))
        txtIdNumber.grid(row=9,column=1)

         #address
        lblAddress=Label(labelframeleft,text="Address:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)
        txtAddress=ttk.Entry(labelframeleft,width=29,textvariable=self.var_address,font=("times new roman",13,"bold"))
        txtAddress.grid(row=10,column=1)

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

        #========= table frame ============
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="VIEW DETAILS AND SEARCH SYSTEM",font=("times new roman",12,"bold"),padx=2,)
        table_frame.place(x=420,y=50,width=800,height=490)

        lblSearchBy=Label(table_frame,text="SearchBy",font=("times new roman",12,"bold"),bg="grey",fg="gold")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_Search=ttk.Combobox(table_frame,width=20,textvariable=self.search_var,font=("times new roman",12,"bold"),state="readonly")
        combo_Search["values"]=("Mobile","Ref")
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
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.cust_details_table = ttk.Treeview(
            details_table, 
            columns=("ref", "name", "mother", "post", "mobile", "email", "nationality", "idproof", "idnumber", "address"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)

        # Your other code here to setup columns, headings, etc.
        self.cust_details_table.heading("ref", text="Ref")
        self.cust_details_table.heading("name", text="Name")
        self.cust_details_table.heading("mother", text="Mother")
        self.cust_details_table.heading("post", text="Post")
        self.cust_details_table.heading("mobile", text="Mobile")
        self.cust_details_table.heading("email", text="Email")
        self.cust_details_table.heading("nationality", text="Nationality")
        self.cust_details_table.heading("idproof", text="IDproof")
        self.cust_details_table.heading("idnumber", text="IDnumber")
        self.cust_details_table.heading("address", text="Address")

        self.cust_details_table['show'] = 'headings'
        


        # Set column widths if desired
        self.cust_details_table.column("ref", width=100)
        self.cust_details_table.column("name", width=100)
        self.cust_details_table.column("mother", width=100)
        self.cust_details_table.column("post", width=100)
        self.cust_details_table.column("mobile", width=100)
        self.cust_details_table.column("email", width=100)
        self.cust_details_table.column("nationality", width=100)
        self.cust_details_table.column("idproof", width=100)
        self.cust_details_table.column("idnumber", width=100)
        self.cust_details_table.column("address", width=100)

        self.cust_details_table.pack(fill=BOTH, expand=1)
        self.cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_mobile.get()==" " or self.var_mother.get()==" ":
            messagebox.showerror("error","All fields are reduired")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="rujusmitha@99",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_ref.get(),
                                                                                self.var_cust_name.get(),
                                                                                self.var_mother.get(),
                                                                                self.var_gender.get(),
                                                                                self.var_post.get(),
                                                                                self.var_mobile.get(),
                                                                                self.var_email.get(),
                                                                                self.var_nationality.get(),
                                                                                self.var_id_proof.get(),
                                                                                self.var_id_number.get(),
                                                                                self.var_address.get()
                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("sucess","customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="rujusmitha@99",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=" "):
        cursor_row=self.cust_details_table.focus()
        content=self.cust_details_table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("error","please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="rujusmitha@99",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s",(
                                                                                                                                                                    
                                                                                                                                                                    self.var_cust_name.get(),
                                                                                                                                                                    self.var_mother.get(),
                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                    self.var_post.get(),
                                                                                                                                                                    self.var_mobile.get(),
                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                    self.var_nationality.get(),
                                                                                                                                                                    self.var_id_proof.get(),
                                                                                                                                                                    self.var_id_number.get(),
                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                    self.var_ref.get()
                                                                                                                                                                ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("update","customer details has been updated successfully",parent=self.root)

    def mdelete(self):
        mdelete=messagebox.askyesno("Hotel management system","do u want delete this customer",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="rujusmitha@99",database="management")
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        #self.var_ref.set(" "),
        self.var_cust_name.set(" "),
        self.var_mother.set(" "),
        #self.var_gender.set(" "),
        self.var_post.set(" "),
        self.var_mobile.set(" "),
        self.var_email.set(" "),
        #self.var_nationality.set(" "),
        #self.var_id_proof.set(" "),
        self.var_id_number.set(" "),
        self.var_address.set(" ")

        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="rujusmitha@99",database="management")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        #query = f"SELECT * FROM customer WHERE {search_column} LIKE %s"
        #value = f"%{search_value}%"
        #my_cursor.execute(query, (value,))
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
                print(i)
        else:
            messagebox.showinfo("No Results", "No matching records found.")
            conn.commit()
        conn.close()

if __name__=="__main":
    root=Tk()
    obj=Cust_win(root)
    root.mainloop()