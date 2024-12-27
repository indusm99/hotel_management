from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import os
from hotel import HotelManagementSystem

def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # Variables
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_securityq = StringVar()
        self.var_securityA = StringVar()  

        # Load the image file
        self.bg_image = Image.open(r"C:\Users\INDIRA S\OneDrive\Desktop\pro\images\bg1.jpg")
        self.bg = ImageTk.PhotoImage(self.bg_image)
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="Light Gray")
        frame.place(x=500, y=150, width=340, height=400)

        img1 = Image.open(r"C:\Users\INDIRA S\OneDrive\Desktop\pro\images\frame.jpeg")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=620, y=175, width=100, height=70)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="gold")
        get_str.place(x=95, y=108)

        # Username Label and Entry
        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="black")
        username.place(x=75, y=155)
        self.txtuser = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=188, width=270)

        # Password Label and Entry
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="black")
        password.place(x=75, y=223)
        self.txtpass = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=255, width=270)

        # Icon images
        img2 = Image.open(r"C:\Users\INDIRA S\OneDrive\Desktop\pro\images\user.jpeg")
        img2 = img2.resize((25, 25), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=545, y=307, width=25, height=25)

        img3 = Image.open(r"C:\Users\INDIRA S\OneDrive\Desktop\pro\images\password.png")
        img3 = img3.resize((25, 25), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=545, y=375, width=25, height=25)

        # Login button
        loginbtn = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # Register button
        registerbtn = Button(frame, text="New User Register", command=self.register_window, font=("times new roman", 10, "bold"), borderwidth=0, fg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=15, y=350, width=150)

        # Forgot password button
        forgotbtn = Button(frame, text="Forgot Password", command=self.forgot_password_window, font=("times new roman", 10, "bold"), borderwidth=0, fg="black", activeforeground="white", activebackground="black")
        forgotbtn.place(x=180, y=350, width=150)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.var_email.get() == "" or self.var_pass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_email.get() == "dbms" and self.var_pass.get() == "1234":
            messagebox.showinfo("Success", "Welcome to our Hotel Website")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="rujusmitha@99", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s", (self.var_email.get(), self.var_pass.get()))
            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid username and password")
            else:
                open_main = messagebox.askyesno("Yes/No", "Access only for admin")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)

                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    # ============= forgot password window ==============
    def forgot_password_window(self):
        if self.var_email.get() == "":
            messagebox.showerror("Error", "Please enter the email address to reset the password")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="rujusmitha@99", database="management")
            my_cursor = conn.cursor()
            query = "select * from register where email=%s"
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Please enter a valid email address")
            else:
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("400x400")

                l = Label(self.root2, text="Forgot Password", font=("times new roman", 20, "bold"), fg="red", bg="white")
                l.place(x=0, y=10, relwidth=1)

                security_q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white", fg="black")
                security_q.place(x=50, y=80)
                self.combo_security_q = ttk.Combobox(self.root2, textvariable=self.var_securityq, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_q["values"] = ("Select", "Your Birth Place", "Your Pet Name", "Your Girlfriend's Name")
                self.combo_security_q.place(x=50, y=110, width=250)
                self.combo_security_q.current(0)

                security_a = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
                security_a.place(x=50, y=150)
                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_security.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), fg="black")
                new_password.place(x=50, y=220)
                self.txt_newpass = ttk.Entry(self.root2,font=("times new roman", 15, "bold"), show="*")
                self.txt_newpass.place(x=50, y=250, width=250)

                submit_btn = Button(self.root2, command=self.reset_pass, text="Reset", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
                submit_btn.place(x=130, y=300)

    def reset_pass(self):
        if self.combo_security_q.get() == "Select" or self.txt_security.get() == "" or self.txt_newpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="rujusmitha@99", database="management")
            my_cursor = conn.cursor()
            query = "select * from register where email=%s and securityq=%s and securityA=%s"
            value = (self.var_email.get(), self.combo_security_q.get(), self.txt_security.get())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Please enter correct security answer")
            else:
                query = "update register set password=%s where email=%s"
                value = (self.txt_newpass.get(), self.var_email.get())
                my_cursor.execute(query, value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Your password has been reset, please login with new password")

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        # Variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityq = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confirmpass = StringVar()
        self.var_check = IntVar()

        # Left image
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\INDIRA S\OneDrive\Desktop\pro\images\images.jpeg")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=700, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="green")
        register_lbl.place(x=20, y=20)

        # Labels and Entries
        Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=100)
        self.fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        self.fname_entry.place(x=50, y=130, width=250)

        Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=370, y=100)
        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.txt_lname.place(x=370, y=130, width=250)

        Label(frame, text="Contact", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=50, y=170)
        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=200, width=250)

        Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=370, y=170)
        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=370, y=200, width=250)

        Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=50, y=240)
        self.combo_security_q = ttk.Combobox(frame, textvariable=self.var_securityq, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_q["values"] = ("Select", "Your Birth Place", "Your Pet Name", "Your Girlfriend's Name")
        self.combo_security_q.place(x=50, y=270, width=250)
        self.combo_security_q.current(0)

        Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=370, y=240)
        self.txt_security = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)

        Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=50, y=310)
        self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15, "bold"), show="*")
        self.txt_pswd.place(x=50, y=340, width=250)

        Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=370, y=310)
        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_confirmpass, font=("times new roman", 15, "bold"), show="*")
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        # Checkbutton
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I agree to the terms and conditions", font=("times new roman", 15, "bold"), onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=380)

        # Buttons
        self.photoimage_list = []  # To hold image references

        img_path = r"C:\Users\INDIRA S\OneDrive\Desktop\pro\images\hi.jpeg"
        if os.path.exists(img_path):
            img = Image.open(img_path)
            img = img.resize((200, 55), Image.LANCZOS)
            self.photoimage1 = ImageTk.PhotoImage(img)
            self.photoimage_list.append(self.photoimage1)
            b1 = Button(frame, image=self.photoimage1, command=self.register_data, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"))
            b1.place(x=60, y=420, width=200)
        else:
            print(f"Image not found at path: {img_path}")

        img1_path = r"C:\Users\INDIRA S\OneDrive\Desktop\pro\images\login2.jpeg"
        if os.path.exists(img1_path):
            img1 = Image.open(img1_path)
            img1 = img1.resize((200, 55), Image.LANCZOS)
            self.photoimage2 = ImageTk.PhotoImage(img1)
            self.photoimage_list.append(self.photoimage2)
            b2 = Button(frame, image=self.photoimage2, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"), fg="white")
            b2.place(x=360, y=420, width=200)
        else:
            print(f"Image not found at path: {img1_path}")

    # Function to handle registration data
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityq.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confirmpass.get():
            messagebox.showerror("Error", "Password and Confirm Password must be the same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to our terms and conditions")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="rujusmitha@99", database="management")
            my_cursor = conn.cursor()
            query = "select * from register where email=%s"
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row is not None:
                messagebox.showerror("Error", "User already exists, please try another email")
            else:
                my_cursor.execute("insert into register (fname, lname, contact, email, securityq, securityA, password) values (%s, %s, %s, %s, %s, %s, %s)",
                                  (
                                      self.var_fname.get(),
                                      self.var_lname.get(),
                                      self.var_contact.get(),
                                      self.var_email.get(),
                                      self.var_securityq.get(),
                                      self.var_securityA.get(),
                                      self.var_pass.get(),
                                  ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Registration successful")

if __name__ == "__main__":
    main()
