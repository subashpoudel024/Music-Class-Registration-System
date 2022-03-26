


from tkinter import*
from PIL  import Image, ImageTk
root = Tk()


root.title('Registration Form')
root.geometry('1350x700')
root.config(bg='black')

def nextpage_2():
    root.destroy()
    import interface_3


image2 = Image.open('E:\\Guitar_for_GUI')
photo2 = ImageTk.PhotoImage(image2)
l4 = Label(root,image=photo2)
l4.place(x=0,y=0,width=600,height=800)

l5 = Label(root, text='Want to register?',font=("times new roman",25),fg='white',bg='black')
l5.place(x=650,y=200)


l6 = Label(root, text='Already have an account?',font=("times new roman",25),fg='white',bg='black')
l6.place(x=650,y=300)


reg_button = Button(root,text='Register',font=('times new roman',18),fg='dark blue',bg='white',borderwidth=6,relief=SUNKEN,
                            cursor='hand2',width=15,height=1,command=nextpage_2)
reg_button.place(x=1050,y=200)

sign_button = Button(root,text='Sign in',font=('times new roman',18),fg='dark blue',bg='white',borderwidth=6,relief=SUNKEN,
                            cursor='hand2',width=15,height=1)
sign_button.place(x=1050,y=300)




root.mainloop()
