import tkinter.messagebox 
from tkinter import  * 
import pymysql as sqlcon 
import random as rd 
 
con=sqlcon.connect(host="localhost",user="root",password="bhuva2004",database="project"
 )#connection to mysql 
cur=con.cursor() 
#cur = con.cursor(buffered=True) 
if (con): 
    # Carry out normal procedure 
    print ("Connection successful") 
else: 
    print ("Connection unsuccessful") 
 
 
 
#  Message for registration 
def entry(): 
global e1,e2,e3,e4,e5,e6 
p1=e1.get() 
p2=e2.get() 
p3=e3.get() 
p4=e4.get()  
p5=e5.get() 
p6=e6.get() 
query="insert into booking values('"+p1+"','"+p2+"','"+p3+"','"+p4+"','"+p5+"','"+p6+"')" 
con.commit() 
cur.execute(query) 
cur.execute("commit") 
tkinter.messagebox.showinfo("DONE", "YOU HAVE BEEN BOOKED FOR MOVIE") 
#  For registration 
def register(): 
global e1,e2,e3,e4,e5,e6 
root1=Tk() 
label=Label(root1,text="BOOKING FORM",font='arial 25 bold') 
label.pack() 
frame=Frame(root1,height=500,width=200) 
frame.pack() 
l1=Label(root1,text="ID_NO.") 
l1.place(x=10,y=130) 
e1=tkinter.Entry(root1) 
e1.place(x=100,y=130) 
l2=Label(root1,text="NAME") 
l2.place(x=10,y=170) 
e2=tkinter.Entry(root1) 
e2.place(x=100,y=170) 
l3=Label(root1,text="AGE") 
l3.place(x=10,y=210) 
e3=tkinter.Entry(root1) 
e3.place(x=100,y=210) 
l4=Label(root1,text="GENDER M\F") 
l4.place(x=10,y=250) 
e4=tkinter.Entry(root1) 
e4.place(x=100,y=250) 
l5=Label(root1,text="PHONE") 
l5.place(x=10,y=290) 
e5=tkinter.Entry(root1) 
49 
e5.place(x=100,y=290) 
l6=Label(root1,text="MOVIE_NAME") 
l6.place(x=10,y=330) 
e6=tkinter.Entry(root1) 
e6.place(x=100,y=330) 
b1=Button(root1,text="SUBMIT",command=entry) 
b1.place(x=150,y=370) 
root.resizable(False,False) 
root1.mainloop() 
#  Message for registration 
def entry1(): 
global a1,a2,a3,a4 
p1=a1.get() 
p2=a2.get() 
p3=a3.get() 
p4=a4.get() 
query="insert into showdetails values('"+p1+"','"+p2+"','"+p3+"','"+p4+"')" 
con.commit() 
cur.execute(query) 
cur.execute("commit") 
tkinter.messagebox.showinfo("DONE", "SHOW DETAILS HAVE BEEN INSERTED!:) 
") 
#  For theatre_details 
def theatre_details(): 
global a1,a2,a3,a4 
root1=Tk() 
label=Label(root1,text="SHOW FACILITY",font='arial 25 bold') 
label.pack() 
frame=Frame(root1,height=500,width=200) 
frame.pack() 
l1=Label(root1,text="SHOW TIME.") 
l1.place(x=10,y=130) 
a1=tkinter.Entry(root1) 
a1.place(x=150,y=130) 
l2=Label(root1,text="SHOW DATE") 
l2.place(x=10,y=170) 
a2=tkinter.Entry(root1) 
50 
a2.place(x=150,y=170) 
l3=Label(root1,text="FACILITY:AC/NAC") 
l3.place(x=10,y=210) 
a3=tkinter.Entry(root1) 
a3.place(x=150,y=210) 
l4=Label(root1,text="SNACKS") 
l4.place(x=10,y=250) 
a4=tkinter.Entry(root1) 
a4.place(x=150,y=250) 
b1=Button(root1,text="SUBMIT",command=entry1) 
b1.place(x=150,y=370) 
root.resizable(False,False) 
root1.mainloop() 
#  Message for registration 
def entry2(): 
global e1,e2,e3,e4,e5,e6,e7 
p1=e1.get() 
p2=e2.get() 
p3=e3.get() 
p4=e4.get() 
p5=e5.get() 
p6=e6.get() 
p7=e7.get() 
query="insert into movie 
values('"+p1+"','"+p2+"','"+p3+"','"+p4+"','"+p5+"','"+p6+"','"+p7+"')" 
con.commit() 
cur.execute(query) 
cur.execute("commit") 
tkinter.messagebox.showinfo("DONE", "MOVIE DETAILS HAVE BEEN INSERTED 
SUCCESSFULLY!!!") 
#  For registration 
def movie(): 
global e1,e2,e3,e4,e5,e6,e7 
root1=Tk() 
51 
label=Label(root1,text="MOVIE DETAILS",font='arial 25 bold') 
label.pack() 
frame=Frame(root1,height=500,width=200) 
frame.pack() 
l1=Label(root1,text="MOVIE_ID") 
l1.place(x=10,y=130) 
e1=tkinter.Entry(root1) 
e1.place(x=100,y=130) 
l2=Label(root1,text="HERO") 
l2.place(x=10,y=170) 
e2=tkinter.Entry(root1) 
e2.place(x=100,y=170) 
l3=Label(root1,text="HEROINE") 
l3.place(x=10,y=210) 
e3=tkinter.Entry(root1) 
e3.place(x=100,y=210) 
l4=Label(root1,text="DIRECTOR") 
l4.place(x=10,y=250) 
e4=tkinter.Entry(root1) 
e4.place(x=100,y=250) 
l5=Label(root1,text="SINGER") 
l5.place(x=10,y=290) 
e5=tkinter.Entry(root1) 
e5.place(x=100,y=290) 
l6=Label(root1,text="MOVIE_NAME") 
l6.place(x=10,y=330) 
e6=tkinter.Entry(root1) 
e6.place(x=100,y=330) 
l7=Label(root1,text="GENRE") 
l7.place(x=10,y=370) 
e7=tkinter.Entry(root1) 
e7.place(x=100,y=370) 
b1=Button(root1,text="SUBMIT",command=entry2) 
b1.place(x=150,y=450) 
root.resizable(False,False) 
root1.mainloop() 
#  Message for appointment 
def apo_details(): 
global x1,x2,h,p1,p2,p3,o,x4,x3 
p1=x2.get() 
p2=x3.get() 
52 
53 
 
    p3=x4.get() 
    if int(p1)==1: 
        i=("ANJAAN \nRoom no:- 10") 
        j=("MASTER \nRoom no:- 11") 
        q=(i,j) 
        h=rd.choice(q) 
        u=(23,34,12,67,53,72) 
        o=rd.choice(u) 
        det=("Your movie booking details",h, 
             "\nDate:-",p2, 
             "\nShow_Time:-",p3, 
             '\nFacility:-',o) 
 
        query='insert into booking_details values("{}", "{}", "{}", "{}", 
"{}")'.format(p1,h,p2,p3,o) 
        cur.execute(query) 
        tkinter.messagebox.showinfo("BOOKING DETAILS",det) 
 
    elif int(p1)==2: 
        i=("VISWASAM \nRoom no. 16") 
        j=("PETTA \nRoom no. 17") 
        q=(i,j) 
        h=rd.choice(q) 
        u=(23,34,12,67,53,72) 
        o=rd.choice(u) 
        det=("Your movie booking details",h, 
             "\nDate:-",p2, 
             "\nShow_Time:-",p3, 
             '\nFacility:-',o) 
        query='insert into booking_details values("{}", "{}", "{}", "{}", 
"{}")'.format(p1,h,p2,p3,o) 
        cur.execute(query) 
        tkinter.messagebox.showinfo("BOOKING DETAILS",det) 
 
    elif int(p1)==3: 
        i=("DON \nRoom no. 12") 
        j=("96 \nRoom no. 13") 
        q=(i,j) 
        h=rd.choice(q) 
        u=(23,34,12,67,53,72) 
        o=rd.choice(u) 
        det=("Your movie booking details",h, 
             "\nDate:-",p2, 
             "\nShow_Time:-",p3, 
'\nFacility:-',o) 
query='insert into booking_details  values("{}", "{}", "{}", "{}", 
"{}")'.format(p1,h,p2,p3,o) 
cur.execute(query) 
tkinter.messagebox.showinfo("BOOKING DETAILS",det) 
elif int(p1)==4: 
i=("NGK, \nRoom no. 18") 
j=(" MAYA\nRoom no. 19") 
q=(i,j) 
h=rd.choice(q) 
u=(23,34,12,67,53,72) 
o=rd.choice(u) 
et=("Your movie booking details",h, 
"\nDate:-",p2, 
"\nShow_Time:-",p3, 
'\nFacility:-',o) 
query='insert into booking_details values("{}", "{}", "{}", "{}", 
"{}")'.format(p1,h,p2,p3,o) 
cur.execute(query) 
tkinter.messagebox.showinfo("BOOKING DETAILS",det) 
elif int(p1)==5: 
i=("LOVE TODAY \nRoom no. 14") 
j=("VIKRAM VEDHA \nRoom no. 15") 
q=(i,j) 
h=rd.choice(q) 
u=(23,34,12,67,53,72) 
o=rd.choice(u) 
det=("Your movie booking details",h, 
"\nDate:-",p2, 
"\nShow_Time:-",p3, 
'\nFacility:-',o) 
query='insert into booking_details values("{}", "{}", "{}", "{}", 
"{}")'.format(p1,h,p2,p3,o) 
cur.execute(query) 
tkinter.messagebox.showinfo("BOOKING DETAILS",det) 
elif int(p1)==6: 
i=("SARKAR \nRoom no. 001") 
j=("D BLOCK \nRoom no. 002") 
k=("ET \nRoom no. 003") 
l=("THUPPARIVALAN \nRoom no. 004") 
q=(i,j,k,l) 
h=rd.choice(q) 
u=(23,34,12,67,53,72) 
54 
o=rd.choice(u) 
det=("Your movie booking details",h, 
"\nDate:-",p2, 
"\nShow_Time:-",p3, 
'\nFacility:-',o) 
query='insert into booking_details values("{}", "{}", "{}", "{}", 
"{}")'.format(p1,h,p2,p3,o) 
cur.execute(query) 
tkinter.messagebox.showinfo("BOOKING DETAILS",det) 
else: 
tkinter.messagebox.showwarning('WRONG INPUT','PLEASE ENTER VALID 
VALUE') 
#  For appointment 
def get_apoint(): 
global x1,x2,x3,x4 
p1=x1.get() 
cur.execute('select * from booking where idno=(%s)',(p1,)) 
dat=cur.fetchall() 
a=[] 
for i in dat: 
a.append(i) 
if len(a)==0: 
tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!") 
else: 
root3=Tk() 
label=Label(root3,text="APPOINTMENT",font='arial 25 bold') 
label.pack() 
frame=Frame(root3,height=500,width=300) 
frame.pack() 
if i[3]=='M' or i[3]=='m': 
x="Mr." 
name2=Label(root3,text=i[1]) 
name2.place(x=140,y=80) 
else: 
x="Mrs\Ms." 
name2=Label(root3,text=i[1]) 
name2.place(x=170,y=80) 
for i in dat: 
name=Label(root3,text='WELCOME') 
name.place(x=50,y=80) 
name1=Label(root3,text=x) 
name1.place(x=120,y=80) 
age=Label(root3,text='AGE:-') 
55 
age.place(x=50,y=100) 
age1=Label(root3,text=i[2]) 
age1.place(x=100,y=100) 
phone=Label(root3,text='PHONE:-') 
phone.place(x=50,y=120) 
phone1=Label(root3,text=i[4]) 
phone1.place(x=100,y=120) 
bg=Label(root3,text='MOVIE_NAME:-') 
bg.place(x=50,y=140) 
bg1=Label(root3,text=i[5]) 
bg1.place(x=150,y=140) 
root3.resizable(False,False) 
root3.mainloop() 
#  For ID_NO input 
def apoint(): 
global x1 
root2=Tk() 
label=Label(root2,text="BOOKING",font='arial 25 bold') 
label.pack() 
frame=Frame(root2,height=200,width=200) 
frame.pack() 
l1=Label(root2,text="ID_NO.") 
l1.place(x=10,y=130) 
x1=tkinter.Entry(root2) 
x1.place(x=100,y=130) 
b1=Button(root2,text='Submit',command=get_apoint) 
b1.place(x=100,y=160) 
root2.resizable(False,False) 
root2.mainloop() 
#  List of movies 
def lst_doc(): 
root4=Tk() 
l=["ANJAAN","MASTER","VISWASAM","PETTA","DON","96","NGK","MAYA","LOV
 E TODAY","VIKRAM VEDHA","SARKAR","D BLOCK","ET","THUPPARIVAALAN"] 
56 
m=["Action","Action","Action","Action","Comedy","Love","Politics","Horror","Love","Acti
 on","Politics","Horror","Crime","Crime"] 
n=[10,11,12,13,14,15,16,17,18,19,20,21,22,23] 
frame=Frame(root4,height=500,width=500) 
frame.pack() 
l1=Label(root4,text='NAME OF MOVIE') 
l1.place(x=20,y=10) 
count=20 
for i in l: 
count=count+20 
l=Label(root4,text=i) 
l.place(x=20,y=count) 
l2=Label(root4,text='GENRE') 
l2.place(x=140,y=10) 
count1=20 
for i in m: 
count1=count1+20 
l3=Label(root4,text=i) 
l3.place(x=140,y=count1) 
l4=Label(root4,text='ROOM NO') 
l4.place(x=260,y=10) 
count2=20 
for i in n: 
count2=count2+20 
l5=Label(root4,text=i) 
l5.place(x=260,y=count2) 
root.resizable(False,False) 
root4.mainloop() 
def ser_avail(): 
root5=Tk() 
frame=Frame(root5,height=500,width=500) 
frame.pack() 
l1=Label(root5,text='SERVICES AVAILABLE') 
l1.place(x=20,y=10) 
f=["AC","NON-AC","NON-AC","AC","NON-AC + HD DISPLAY","AC + 
ADJUSTABLE SEATS","AC + FREE SNACKS","AC + HD DISPLAY","NON-AC + 
57 
FREE SNACKS","NON-AC + ADJUSTABLE SEATS","NON-AC + HD DISPLAY","AC + 
ADJUSTABLE SEATS","AC + FREE SNACKS","AC + HD DISPLAY"] 
count1=20 
for i in f: 
count1=count1+20 
l3=Label(root5,text=i) 
l3.place(x=20,y=count1) 
l2=Label(root5,text='ROOM NO.') 
l2.place(x=180,y=10) 
g=[10,11,12,13,14,15,16,17,18,19,20,21,22,23] 
count2=20 
for i in g: 
count2=count2+20 
l4=Label(root5,text=i) 
l4.place(x=180,y=count2) 
l5=Label(root5,text='To avail any of these please contact on our no.:- 7042****55') 
l5.place(x=20,y=350) 
root5.resizable(False,False) 
root5.mainloop() 
def modify(): 
global x3,x4,choice,new,x5,root6 
p1=x3.get() 
cur.execute('select * from booking where idno=(%s)',(p1,)) 
dat=cur.fetchall() 
a=[] 
for i in dat: 
a.append(i) 
if len(a)==0: 
tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!") 
else: 
root6=Tk() 
frame=Frame(root6,height=500,width=500) 
frame.pack() 
l1=Label(root6,text='DATA MODIFICATION',font="arial 15 bold") 
l1.place(x=75,y=10) 
l2=Label(root6,text='WHAT YOU WANT TO CHANGE') 
l2.place(x=50,y=200) 
l3=Label(root6,text='1.NAME') 
l3.place(x=50,y=220) 
l4=Label(root6,text='2.AGE') 
l4.place(x=50,y=240) 
l5=Label(root6,text='3.GENDER') 
58 
l5.place(x=50,y=260) 
l6=Label(root6,text='4.PHONE') 
l6.place(x=50,y=280) 
l7=Label(root6,text='5.SEAT_no') 
l7.place(x=50,y=300) 
x2=Label(root6,text='Enter') 
x2.place(x=50,y=330) 
x4=tkinter.Entry(root6) 
choice=x4.get() 
x4.place(x=100,y=330) 
for i in dat: 
name=Label(root6,text='NAME:-') 
name.place(x=50,y=80) 
name1=Label(root6,text=i[1]) 
name1.place(x=150,y=80) 
age=Label(root6,text='AGE:-') 
age.place(x=50,y=100) 
age1=Label(root6,text=i[2]) 
age1.place(x=150,y=100) 
gen=Label(root6,text='GENDER:-') 
gen.place(x=50,y=120) 
gen1=Label(root6,text=i[3]) 
gen1.place(x=150,y=120) 
pho=Label(root6,text='PHONE:-') 
pho.place(x=50,y=140) 
pho1=Label(root6,text=i[4]) 
pho1.place(x=150,y=140) 
bg=Label(root6,text='SEAT_NO:-') 
bg.place(x=50,y=160) 
bg1=Label(root6,text=i[5]) 
bg1.place(x=150,y=160) 
b=Button(root6,text='Submit',command=do_modify) 
b.place(x=50,y=400) 
L1=Label(root6,text='OLD DETAILS') 
L1.place(x=50,y=50) 
L2=Label(root6,text='ENTER NEW DETAIL') 
L2.place(x=50,y=360) 
x5=tkinter.Entry(root6) 
new=x5.get() 
x5.place(x=160,y=360) 
root6.resizable(False,False) 
root6.mainloop() 
59 
def do_modify(): 
global ad,x3,x4,x5 
ad=x3.get() 
choice=x4.get() 
new=x5.get() 
if choice=='1': 
cur.execute('update booking set name=%s where idno=%s',(x4,x5)) 
elif choice=='2': 
cur.execute('update booking set age={} where idno={}'.format(new,ad)) 
elif choice=='3': 
cur.execute('update booking set gender={} where idno={}'.format(new,ad)) 
elif choice=='4': 
cur.execute('update booking set phone={} where idno={}'.format(new,ad)) 
elif choice=='5': 
cur.execute('update booking set movie_name={} where idno={}'.format(new,ad)) 
else: 
pass 
root6.destroy() 
tkinter.messagebox.showinfo("DONE", "YOUR DATA HAS BEEN MODIFIED") 
choice=None 
new=None 
ad=None 
def mod_sub(): 
global x3,ad 
root7=Tk() 
label=Label(root7,text="UPDATE",font='arial 25 bold') 
label.pack() 
frame=Frame(root7,height=200,width=200) 
frame.pack() 
l1=Label(root7,text="ID_NO.") 
l1.place(x=10,y=130) 
x3=tkinter.Entry(root7) 
x3.place(x=100,y=130) 
ad=x3.get() 
b1=Button(root7,text='Submit',command=modify) 
b1.place(x=100,y=160) 
root7.resizable(False,False) 
root7.mainloop() 
def search_data(): 
global x3,ad 
root7=Tk() 
label=Label(root7,text="VIEW DATA",font='arial 25 bold') 
60 
label.pack() 
frame=Frame(root7,height=200,width=200) 
frame.pack() 
l1=Label(root7,text="MOVIE_ID") 
l1.place(x=10,y=130) 
x3=tkinter.Entry(root7) 
x3.place(x=100,y=130) 
ad=x3.get() 
b1=Button(root7,text='Submit',command=view_data) 
b1.place(x=100,y=160) 
root7.resizable(False,False) 
root7.mainloop() 
def view_data(): 
global p1,p2 
p1=x3.get() 
p2=x3.get() 
cur.execute('select * from booking where idno=(%s)',(p1,)) 
cur.execute('select * from movie where movie_id=(%s)',(p1,)) 
dat=cur.fetchall() 
print(dat) 
a=[] 
for i in dat: 
a.append(i) 
if len(a)==0: 
tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!") 
else: 
det=a 
tkinter.messagebox.showinfo("BOOKING DETAILS",det) 
root=Tk() 
#film=PhotoImage(file='C:\\Users\\bhuva\\Downloads') 
#label=ttk.Label(root,image=OIP) 
#PhotoImage(file='C:\\Users\\bhuva\bhu\Downloads') 
label=Label(root,text="FILM MANAGEMENT",bd=20,relief=RIDGE,font="STCaiyun 40 
bold",bg='grey',fg='black') 
label.pack(side=TOP,fill=X) 
b1=Button(text="Info",bd=20,relief=RIDGE,font="Magneto 20 bold",bg='sky 
blue',command=register) 
#b2=Button(text="Search",bd=20,relief=RIDGE,font="Magneto 20 bold",bg='sky 
blue',command=apoint) 
b3=Button(text="Movies List",bd=20,relief=RIDGE,font="Magneto 20 bold",bg='sky 
blue',command=lst_doc) 
61 
b4=Button(text="facility",bd=20,relief=RIDGE,font='Magneto 20 bold',bg='sky 
blue',command=ser_avail) 
b7=Button(text="View data",bd=20,relief=RIDGE,font='Magneto 20 bold',bg='sky 
blue',command=search_data) 
b5=Button(text="update",bd=20,relief=RIDGE,font='Magneto 20 bold',bg='sky 
blue',command=mod_sub) 
b6=Button(text="Exit",bd=20,relief=RIDGE,font='Broadway 18 
bold',command=root.destroy,bg='orange',fg='white') 
b8=Button(text="Show_details",bd=20,relief=RIDGE,font="Magneto 20 bold",bg='sky 
blue',command=theatre_details) 
b9=Button(text="Booking",bd=20,relief=RIDGE,font="Magneto 20 bold",bg='sky 
blue',command=movie) 
b2=Button(text="Search",bd=20,relief=RIDGE,font="Magneto 20 bold",bg='sky 
blue',command=apoint) 
label.pack() 
#b1.pack(side=LEFT,pady=2) 
#b3.pack(side=LEFT,padx=2) 
b8.pack(side=LEFT,padx=10) 
b9.place(x=670,y=150) 
b2.pack(side=LEFT,padx=10) 
b4.place(x=475,y=150) 
b6.place(x=750,y=451) 
#b8.place(x=290,y=150) 
#b9.place(x=15,y=150) 
#b2.place(x=17,y=451) 
b7.pack(side=LEFT,pady=10) 
b3.place(x=15,y=150) 
b1.place(x=290,y=150) 
b5.pack(side=LEFT,padx=10) 
frame=Frame(root,height=500,width=100) 
frame.pack() 
root.resizable(False,False) 
root.mainloop() 