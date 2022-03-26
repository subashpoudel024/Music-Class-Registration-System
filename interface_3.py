
# ----------Importing the modules-------    PART_1
from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import pymysql

root = Tk()

# ----Creating a root window-------          PART_2
root.title('Registration Form')
root.geometry('1350x700')
root.config(bg='black')



# -------------Creating a function to clear the data if one user is registered.------ PART_16
def clear():
    txt_fname.delete(0,END)
    txt_lname.delete(0,END)
    txt_cnumber.delete(0,END)
    txt_address.delete(0,END)
    txt_email_name.delete(0,END)
    txt_password.delete(0,END)
    txt_confirm.delete(0,END)
    answer.current(0)
    agreement.set(0)
    # This function is called in line number 77.


# ---------Creating a function to fetch the data-------------- PART_15
def show():
        if f_value.get()==''or l_value.get()== '' or a_value.get()=='' or c_value.get()==''or e_value.get()=='' or answer.get()=='Select':
            messagebox.showerror("Error" ,"All fields  are required.",parent=root)

        elif p_value.get()=='' or con_value.get()=='':
            messagebox.showerror("Error" ,"All fields  are required.",parent=root)
        
        elif p_value.get() != con_value.get():
            messagebox.showerror('Error','Password did not match.',parent = root)

        
        elif agreement.get()==0:
            messagebox.showwarning('Unfair','Please agree to our terms and conditions',parent = root)
        
        else:
            try:
                con = pymysql.connect(
                      host="localhost",
                      user="root",
                      password="",
                      database="music",
                      port=3306
                      )
                
                cur = con.cursor()

                cur.execute("select * from students where email=%s",txt_email_name.get())
                row = cur.fetchone()
                # print(row)

                if row!=None:
                    messagebox.showerror("Error","Email already exists.",parent = root)

                else:
                    cur.execute("insert into students (f_name,l_name,contact,email,address,attend,password) values(%s,%s,%s,%s,%s,%s,%s)",
                            (txt_fname.get(),
                            txt_lname.get(),
                            txt_cnumber.get(),
                            txt_email_name.get(),
                            txt_address.get(),
                            answer.get(),
                            txt_confirm.get()))
                    con.commit()
                    con.close()     
                    messagebox.showinfo('Success','Registration Successful',parent = root)
                    clear()


                            
            except Exception as es:
                messagebox.showerror("Error",f"Error due to :{str(es)}",parent = root)





# -----Creating side image-------        PART_3
image1 = Image.open('E:\\Guitar_for_GUI')
photo1 = ImageTk.PhotoImage(image1)
l2 = Label(root,image=photo1)
l2.place(x=0,y=0,width=600,height=800)




# ---------This the title above the form-------- PART_4
l3 = Label(root, text='Register Here.',font=("times new roman",25),fg='dark orange',bg='black')
l3.place(x=800,y=40)

# -------First name----------------- PART_5
f_name = Label(root, text='First name:',font='comiscans 15 bold',fg='white',bg='black')
f_name.place(x=620,y=130)

f_value = StringVar()
txt_fname = Entry(root,borderwidth=4,relief=SUNKEN,font='comiscanms 10 bold',textvariable=f_value)
txt_fname.place(x=620,y=160)

# ------Last name----------   PART_6
l_name = Label(root, text='Last name:',font='comiscans 15 bold',fg='white',bg='black')
l_name.place(x=1000,y=130)

l_value = StringVar()
txt_lname = Entry(root,borderwidth=4,relief=SUNKEN,font='comiscanms 10 bold',textvariable=l_value)
txt_lname.place(x=1000,y=160)


# ---------------contact number----------  PART_7

c_number = Label(root, text='Contact number:',font='comiscans 15 bold',fg='white',bg='black')
c_number.place(x=620,y=230)

c_value = StringVar()
txt_cnumber = Entry(root,borderwidth=4,relief=SUNKEN,font='comiscanms 10 bold',textvariable=c_value)
txt_cnumber.place(x=620,y=260)

# ---------------email-------    PART_8
email_name = Label(root, text='Email ID:',font='comiscans 15 bold',fg='white',bg='black')
email_name.place(x=1000,y=230)

e_value = StringVar()
txt_email_name = Entry(root,borderwidth=4,relief=SUNKEN,font='comiscanms 10 bold',textvariable=e_value)
txt_email_name.place(x=1000,y=260)

# ----------address-------------  PART_9
address  = Label(root, text='Address:',font='comiscans 15 bold',fg='white',bg='black')
address.place(x=620,y=330)

a_value = StringVar()
txt_address = Entry(root,borderwidth=4,relief=SUNKEN,font='comiscanms 10 bold',textvariable=a_value)
txt_address.place(x=620,y=360)

# --------- Create Password-----------   PART_10
password = Label(root, text='Set password:',font='comiscans 15 bold',fg='white',bg='black')
password.place(x=620,y=430)

p_value = StringVar()
txt_password = Entry(root,borderwidth=4,relief=SUNKEN,font='comiscanms 10 bold',textvariable=p_value)
txt_password.place(x=620,y=460)

# --------Confirm Password---------   PART_11
confirm = Label(root, text='Confirm password:',font='comiscans 15 bold',fg='white',bg='black')
confirm.place(x=1000,y=430)

con_value = StringVar()
txt_confirm = Entry(root,borderwidth=4,relief=SUNKEN,font='comiscanms 10 bold',textvariable=con_value)
txt_confirm.place(x=1000,y=460)



# --------text above combobox------------- PART_12
attend  = Label(root, text='Class to attend:',font='comiscans 15 bold',fg='white',bg='black')
attend.place(x=1000,y=330)

# ans_value = StringVar()
answer = ttk.Combobox(root,font='comiscans 15 bold',state='readonly',justify=CENTER)
answer['values'] = ('Select','Guitar','Vocals','Bass','Drums','Harmonium','Piano')
answer.place(x=1000,y=360)
answer.current(0)



# --------Check Button----------- PART_13
agreement = IntVar()
c_agreement = Checkbutton(root, text='I agree to all terms and conditions.',borderwidth=4,relief=SUNKEN,
                        cursor='hand2',font='comiscanms 15 bold', variable=agreement)
c_agreement.place(x=620,y=530)


# --------Submit button---------------- PART_14
submit = Button(root,text='Submit',font=('times new roman',20),fg='dark orange',bg='black',command=show,borderwidth=8,relief=SUNKEN,
                            cursor='hand2')
submit.place(x=880,y=600)



root.mainloop()








