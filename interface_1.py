
from tkinter import*
from PIL  import Image, ImageTk
root = Tk()


root.title('Registration Form')
root.geometry('1350x700')
root.config(bg='black')

def nextpage_1():
    root.destroy()
    import interface_2

    


# -----Creating side image-------        
image2 = Image.open('E:\\Guitar_for_GUI')
photo2 = ImageTk.PhotoImage(image2)
l4 = Label(root,image=photo2)
l4.place(x=0,y=0,width=600,height=800)


l5 = Label(root, text='"Chitwan-Pokhara Music Studio"',font=("times new roman",30),fg='dark orange',bg='black')
l5.place(x=700,y=40)


l6 = Label(root, text='Welcomes You To.....',font=("times new roman",25),fg='dark orange',bg='black')
l6.place(x=850,y=100)

l7 = Label(root, text=' Sharp the happiness flat the pain.',font=("times new roman",30),fg='white',bg='black')
l7.place(x=700,y=270)



l8 = Label(root, text='Press Ok to continue.',font=("times new roman",30),fg='dark orange',bg='black')
l8.place(x=800,y=500)


submit = Button(root,text='OK',font=('times new roman',20),fg='dark blue',bg='white',borderwidth=8,relief=SUNKEN,
                            cursor='hand2',command=nextpage_1)
submit.place(x=910,y=400)


root.mainloop()










