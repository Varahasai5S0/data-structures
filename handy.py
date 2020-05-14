import tkinter as tk
import time 
import random as rand
from tkinter import filedialog  
from PIL import ImageTk, Image
score=0 
global start
global m1
global m2 
global bat
global bowl 
global app  
global abc
def har(): 
    f.config(background="gray")
    try:
        f.after(0,msg1.destroy)
        f.after(0,msg2.destroy)
        f.after(0,msg3.destroy)
        f.after(0,ab.destroy)
        f.after(0,app.destroy)
        f.after(0,tar.destroy) 
        f.after(0,abc.destroy)
        f.after(0,ms1.destroy)
        f.after(0,ms2.destroy) 
        f.after(0,click1.destroy) 
        f.after(0,abcd4.destroy) 
        f.after(0,abc6.destroy)
    except:
        pass 
    global chas
    sa="Select ur run to chase target==="
    chas=tk.Label(f,text=sa,width=30,font=30,fg="red")
    global c1
    c1=tk.Button(f,text="1",width="6",font=10,bd=8,command=lambda: scoreboard2(1))
    global c2
    c2=tk.Button(f,text="2",width="6",font=10,bd=8,command=lambda: scoreboard2(2))
    global c3 
    c3=tk.Button(f,text="3",width="6",font=10,bd=8,command=lambda: scoreboard2(3))
    global c4
    c4=tk.Button(f,text="4",width="6",font=10,bd=8,command=lambda: scoreboard2(4))
    global c5 
    c5=tk.Button(f,text="5",width="6",font=10,bd=8,command=lambda: scoreboard2(5))
    global c6
    c6=tk.Button(f,text="6",width="6",font=10,bd=8,command=lambda: scoreboard2(6))  
    chas.place(relx=0.2,x=10,y=10)
    c1.place(relx=0.1,x=60,y=60)
    c2.place(relx=0.1,x=180,y=60)
    c3.place(relx=0.1,x=60,y=130)
    c4.place(relx=0.1,x=180,y=130)
    c5.place(relx=0.1,x=60,y=200)
    c6.place(relx=0.1,x=180,y=200)  

def summary(): 
    f.config(background="black")
    try:
        f.after(0,ms1.destroy)
        f.after(0,ms2.destroy) 
        f.after(0,click1.destroy)
    except:
        pass 
    try:
        f.after(0,abcd4.destroy)  
        f.after(0,abc6.destroy) 
    except:
        pass
    try:
        f.after(0,abcd.destroy)
        f.after(0,abcd1.destroy)  
    except:
        pass 
    try:
        f.after(0,abcd2.destroy)  
        f.after(0,abcd3.destroy)
    except:
        pass
    s8="Bad luck about the result\n\n..NO PROBLEM!!! HOPE for another match "
    global abc1
    abc1=tk.Label(f,text=s8,font=10,fg="green")
    abc2=tk.Button(f,text="Tap to Quit",width=20,font=20,fg="red",bd=10,command=quit)
    abc1.place(relx=0.1,x=50,y=50)
    abc2.place(relx=0.2,x=30,y=250)

def present():  
    f.config(background="magenta")
    try:
        f.after(0,ms1.destroy)
        f.after(0,ms2.destroy) 
        f.after(0,click1.destroy)
    except:
        pass 
    try:
        f.after(0,abcd4.destroy)  
        f.after(0,abc6.destroy) 
    except:
        pass
    try:
        f.after(0,abcd.destroy)
        f.after(0,abcd1.destroy)  
    except:
        pass 
    try:
        f.after(0,abcd2.destroy)  
        f.after(0,abcd3.destroy)
    except:
        pass
    s8="Good Match for u .....\n Keep it up high and get better results for future gamess!!!"
    global abc3
    abc3=tk.Message(f,text=s8,font=20,width=30,fg="green")
    abc4=tk.Button(f,text="Tap to Quit",width=20,font=20,fg="red",bd=10,command=quit)
    abc3.place(relx=0.1,x=50,y=50)
    abc4.place(relx=0.2,x=30,y=250)

def quit():
    f.destroy()
      
def scoreboard2(g): 
    f.config(background="cyan")
    f.after(0,chas.destroy)
    f.after(0,c1.destroy)
    f.after(0,c2.destroy)
    f.after(0,c3.destroy)
    f.after(0,c4.destroy)
    f.after(0,c5.destroy)
    f.after(0,c6.destroy)
    global score
    global target
    s="Your runs for this turn "+str(g)
    opp1=rand.randrange(6,100000)%6+1
    y="Opponent for this turn "+str(opp1)  
    global ms1
    ms1=tk.Label(f,text=s,width=20,fg="red",font=20,bd=4)
    ms1.place(relx=0.1,x=50,y=50)
    global ms2
    ms2=tk.Label(f,text=y,width=20,fg="darkblue",font=20,bd=4)
    ms2.place(relx=0.1,x=50,y=100)
    score+=g 
    global target 
    global click1 
    global abcd 
    global abcd1 
    global abcd2 
    global abcd3 
    global abc6 
    global abcd4 
    if g==opp1:
        s5="ohhh@@ It's out!!! \nYou lost the match"
        abcd=tk.Label(f,text=s5,width=40,font=20,fg="purple")
        abcd1=tk.Button(f,text="Move to Summary",width=30,font=40,fg="blue",bd=10,command=summary)
        abcd.place(relx=0.1,x=50,y=150)
        abcd1.place(relx=0.1,x=50,y=250) 
    elif score>=target:
        s6="@@ U chased down the target..\n##CONGRATS##" 
        abcd2=tk.Label(f,text=s6,width=40,font=10,fg="purple")
        abcd3=tk.Button(f,text="Move to presentation Ceremony",width=40,font=20,fg="blue",bd=10,command=present)
        abcd2.place(relx=0.1,x=50,y=150)
        abcd3.place(relx=0.1,x=50,y=250) 
    else:
        s7="Score is: "+str(score) 
        s10="Still need "+str(target-score)+" to win this game"
        abc6=tk.Label(f,text=s10,width="30",font=20,fg='purple')
        abcd4=tk.Label(f,text=s7,width="20",font=20,fg='blue')
        click1=tk.Button(f,text="Click for next turn",width=30,font=30,bd=10,fg="red",command=har) 
        abcd4.place(relx=0.1,x=50,y=150) 
        abc6.place(relx=0.1,x=50,y=190)
        click1.place(relx=0.1,x=50,y=240)
               
def scoreboard1(g):  
    f.config(background="brown")
    f.after(0,msg.destroy)
    f.after(0,h1.destroy)
    f.after(0,h2.destroy)
    f.after(0,h3.destroy)
    f.after(0,h4.destroy)
    f.after(0,h5.destroy)
    f.after(0,h6.destroy)
    global score
    s="Your runs for this turn "+str(g)
    opp=rand.randrange(6,100000)%6+1
    y="Opponent runs for this turn "+str(opp)  
    global msg1
    msg1=tk.Label(f,text=s,width=20,fg="red",font=20,bd=4)
    msg1.place(relx=0.1,x=50,y=50)
    global msg2
    msg2=tk.Label(f,text=y,width=30,fg="darkblue",font=20,bd=4)
    msg2.place(relx=0.1,x=50,y=100) 
    global msg3
    global app 
    global click
    if g==opp:  
        s1="!!!!!  U r out  !!!!!"
        s2="Score is=="+str(score) 
        global ab
        ab=tk.Label(f,text=s2,width=20,fg="green",bd=5,font=10)
        ab.place(relx=0.1,x=50,y=140) 
        msg3=tk.Label(f,text=s1,width=20,fg="blue",bd=5,font=10) 
        msg3.place(relx=0.1,x=50,y=180)   
        global tar  
        global target
        target=score+1 
        score=0
        s4="::::Chase the Target:::"+str(target)
        tar=tk.Label(f,text=s4,width=30,fg="magenta",font=20) 
        tar.place(relx=0.1,x=50,y=230)
        app=tk.Button(f,text="Click here to start second innings",width=40,font=20,bd=10,fg="orange",command=har) 
        app.place(relx=0.1,x=0,y=300)
    else:
        score+=int(g)
        s3="Score is=="+str(score) 
        global abc
        abc=tk.Label(f,text=s3,width=20,fg="red",font=10,bd=5)
        abc.place(relx=0.1,x=50,y=150)
        click=tk.Button(f,text="Click for next turn",width=20,fg="gray",bd=10,font=30,command=hello)
        click.place(relx=0.1,x=100,y=220) 
    
def hello(): 
    f.config(background="pink")
    global abc  
    try:
        f.after(0,start.destroy)        
        f.after(0,m1.destroy)
        f.after(0,m2.destroy)
    except:
        pass  
    try:
        f.after(0,mesg.destroy)
        f.after(0,first.destroy)
    except:
        pass 
    try: 
        f.after(0,abc.destroy)
        f.after(0,msg1.destroy)
        f.after(0,msg2.destroy) 
        f.after(0,click.destroy) 
        f.after(0,tar.destroy) 
        f.after(0,msg3.destroy) 
    except:
        pass 
    global msg
    msg=tk.Label(f,text="Select ur Run==",width="20",fg="red",font=30) 
    global h1
    h1=tk.Button(f,text="1",width="6",fg="blue",bd="7",font=10,command=lambda: scoreboard1(1))
    global h2
    h2=tk.Button(f,text="2",width="6",fg="blue",bd="7",font=10,command=lambda: scoreboard1(2))
    global h3 
    h3=tk.Button(f,text="3",width="6",fg="blue",bd="7",font=10,command=lambda: scoreboard1(3))
    global h4
    h4=tk.Button(f,text="4",width="6",fg="blue",bd="7",font=10,command=lambda: scoreboard1(4))
    global h5 
    h5=tk.Button(f,text="5",width="6",fg="blue",bd="7",font=10,command=lambda: scoreboard1(5))
    global h6
    h6=tk.Button(f,text="6",width="6",fg="blue",bd="7",font=10,command=lambda: scoreboard1(6))   
    msg.place(relx=0.2,x=10,y=10)
    h1.place(relx=0.1,x=60,y=60)
    h2.place(relx=0.1,x=170,y=60)
    h3.place(relx=0.1,x=60,y=130)
    h4.place(relx=0.1,x=170,y=130)
    h5.place(relx=0.1,x=60,y=200)
    h6.place(relx=0.1,x=170,y=200) 

def sri(g): 
    f.config(background="purple")
    f.after(0,bat.destroy)
    f.after(0,bowl.destroy)
    f.after(0,m1.destroy) 
    if g==0:
        s='You choose to bat first@@@@'
    else:
        s='You choose to bowl first@@@@'
    global mesg
    mesg=tk.Message(f,text=s,width=400,font=10,fg="blue")
    mesg.place(relx=0.1,x=50,y=50) 
    global first
    first=tk.Button(f,text="Start the first innings",bd=10,font=30,width=30,command=hello)
    first.place(relx=0.1,x=50,y=100)
        
def toss(g): 
    f.config(background="red")
    d={0:"heads",1:"tails"} 
    pro={0:"bat",1:"bowl"}
    k=0
    ra=rand.randint(0,1000000)%2
    f.after(0,b1.destroy)
    f.after(0,b2.destroy)
    f.after(0,m.destroy)
    f.after(0,a.destroy)  
    if g==ra:
        s="###  It\'s "+d[ra]+" Hurray!!!! You won the toss ###" 
        k=1 
    else:
        s="->Ouchhh! Opponent won the toss->"  
    global m1
    m1=tk.Message(f,text=s,width="350",font=15,fg="red")
    m1.place(relx=0.25,x=0,y=50)
    if k==1: 
        global bat
        bat=tk.Button(f,text="bat",bd=10,font=20,command=lambda: sri(0))
        bat.place(relx=0.2,x=90,y=100) 
        global bowl
        bowl=tk.Button(f,text="bowl",bd=10,font=20,command=lambda: sri(1))
        bowl.place(relx=0.2,x=190,y=100) 
    else:
        pro_1=rand.randint(0,10000)%2
        s1="Opponent elected to "+pro[pro_1]+" first" 
        global m2
        m2=tk.Message(f,text=s1,width=350,fg="green",font=20,bd=5)
        m2.pack()    
    if k==0:
        global start
        start=tk.Button(f,text="Start the First Innings",width=20,bd=10,font=20,fg="red",command=hello)
        start.place(relx=0.1,x=90,y=100) 
 
           
if __name__=="__main__": 
    f=tk.Tk() 
    f.title("HAND-CRICKET") 
    f.config(background="blue") 
    f.geometry("500x500") 
    path="ch.jpg"    
    load=pil.Image("ch.jpg")
    img=ImageTk.PhotoImage(Image.open(path))
    m=tk.Label(f,text="*****Welcome to the game*****",fg="gray",font=50,width=300,bd=4) 
    m.place(relx=0.1,x=50,y=30)  
    panel=tk.Label(f,image=img).pack()
    a=tk.Label(f, text="Select your Toss :",width="20",fg="green",font=15,bd=5) 
    a.place(relx=0,x=0,y=100) 
    b1=tk.Button(f,text="Heads",width="10",fg="blue",bd=10,command=lambda :toss(0))
    b2=tk.Button(f,text="Tails",width="10",fg="red",bd=10,command=lambda: toss(1)) 
    b1.place(relx=0.2,x=120,y=100)
    b2.place(relx=0.3,x=180,y=100)  
    f.mainloop()
