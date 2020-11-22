from pygame import *
from tkinter import *
import smtplib
def mail():
    try:
        message=message_box.get()
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.ehlo()
        s.starttls()#for secuority issue
        s.login(email_id.get(),password.get())
        s.sendmail(email_id.get(),email_id_ri.get(),message)
        s.close()
    except EXCEPTION as e:
        print((e))
def walki():
    mixer.init()
    mixer.music.load("walki.ogg")
    mixer.music.play()
def pirat():
    mixer.init()
    mixer.music.load("pirates_of_the_caribbean_-_soundtrack.ogg")
    mixer.music.play()
def soul():
    mixer.init()
    mixer.music.load("krishna.ogg")
    mixer.music.play()
def sp():
    mixer.init()
    mixer.music.load("kgf.ogg")
    mixer.music.play()
def stop():
    mixer.init()
    mixer.music.stop()


root=Tk()

root.title("Third party_mail...")
root.geometry("1000x600")
f1=Frame(root,bg="black",width=100)
f1.pack(side=LEFT,fill=Y)
lab1=Label(f1,bg="black",fg="red",
           text="WELCOME_in_THird Party",font="chiller 20 italic").pack(side=TOP,fill=X)


b5=Button(f1,bg="black",text="Stop The Song",padx=30,
       cursor="arrow",font="impact 10 italic",command=stop,bd =3 ,relief=RAISED,
          fg="white",

      activebackground="green",)
b5.pack(side=BOTTOM,fill=X)
b1=Button(f1,bg="blue",text="K. G. F",
          cursor="arrow",font="impact 10 italic",command=sp,bd =3 ,relief=SUNKEN,
          activebackground="green")
b1.pack(side=BOTTOM,fill=X)
b2=Button(f1,bg="yellow",text="Pirate of caribbean",
         cursor="pirate",font="impact 10 italic",command=pirat,bd =3 ,relief=RAISED,

         activebackground="green",)
b2.pack(side=BOTTOM,fill=X)
b3=Button(f1,bg="brown",text="Instrument",
       cursor="arrow",font="impact 10 italic",command=soul,bd =3 ,relief=RAISED,

      activebackground="green",)
b3.pack(side=BOTTOM,fill=X)

b4=Button(f1,bg="green",text="RoBo",
     cursor="arrow",font="impact 10 italic",command=walki,bd =3 ,relief=RAISED,

    activebackground="green",)
b4.pack(side=BOTTOM,fill=X)
lab2=Label(f1,text="Click bellow the\n Buttons for\nSongs",font=" chiller 20 bold italic",bg="black",fg="blue"
          ).pack(padx=10,fill=X,side=BOTTOM)
"""making another frame """
name=StringVar()
email_id=StringVar()
email_id_ri=StringVar()
password=StringVar()
message_box=StringVar()


f2=Frame(root,bg="grey",width=100,height=40,
         bd=2,relief=SUNKEN)
f2.pack(side=TOP,fill=X)
lab3=Label(root,text="Name " ,font=" arial 18",padx=10,
           fg="green").pack(fill=X,anchor="ne")
labentry=Entry(bd=3,relief=SOLID,textvariable=name,width=70,
               font="arial 15 italic",justify=CENTER,bg="white"
               ,selectbackground="green",selectforeground="blue").pack(pady=10)
lab4=Label(root,text="Email id " ,font=" arial 18",padx=10,
           fg="green").pack(fill=X,anchor="ne")

labentry1=Entry(bd=3,relief=SOLID,textvariable=email_id,width=70,
               font="arial 15 italic",justify=CENTER,bg="white"
                ,selectbackground="green",selectforeground="blue").pack(pady=10)
lab5=Label(root,text="Password " ,font=" arial 18",
           padx=10,
           fg="green").pack(fill=X,anchor="ne")

labentry2=Entry(bd=3,relief=SOLID,textvariable=password,width=70,show="*",
               font="arial 15 italic",justify=CENTER,bg="white",
                selectbackground="green",selectforeground="blue").pack(pady=10)

lab6=Label(root,text=" Email.id (Receiver)" ,font=" arial 18",padx=10,
           fg="green").pack(fill=X,anchor="ne")
labentry3=Entry(bd=3,relief=SOLID,textvariable=email_id_ri,width=70,
               font="arial 15 italic",justify=CENTER,bg="white"
                ,selectbackground="green",selectforeground="blue").pack(pady=10)


a="(MAKE SURE THAT YOU HAVE ENTERED CORRECT Email_Id AND THE PASSWORD) "
labwarnig=Label(text=a,fg="black",bd=3,relief=GROOVE).pack(pady=10)

"""buttons"""
lab8=Label(text="WRITE THE MESSAGE IN THE BOX",fg="red",font="arial 18").pack()
massage_box=Entry(textvariable=message_box,width=60,bd=3,relief=
              "solid",selectbackground="green",selectforeground="blue",
                  selectborderwidth=20,
                  font="arial 18",justify=LEFT
                  ).pack()
sign_button=Button(text="Send",bg="green",font="ariel 16 italic",padx=10
                   ,activebackground="red",command=mail).pack(pady=10)
k=name.get()

root.mainloop()