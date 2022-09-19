from tkinter import *
from tkinter import messagebox
import time
from plyer import notification

root = Tk()
root.geometry("300x180")
root.title("Countdown timer")
root.resizable(0,0)

def h_click(event):
    hour_entry.delete(0, 'end')        
def m_click(event):
    min_entry.delete(0, 'end')
def s_click(event):         
    sec_entry.delete(0, 'end')

def timer():
   try:
       user_time = int(hour_entry.get())*3600 + int(min_entry.get())*60 + int(sec_entry.get())
      
   except:
       messagebox.showerror(message="Enter Valid Time")
      
   if user_time >0:
       hour = 0
       min = 0
       sec = 0   
       while user_time >= 0:
           min, sec = divmod(user_time,60)
           if min > 60:
               hour, min = divmod(min,60)
                         
           hours.set(hour)
           mins.set(min)
           secs.set(sec)

           time.sleep(1)  
           root.update()
           user_time -= 1
       
       notification.notify(title = "TIMER ALERT",message = "Times up !", timeout  = 30)
       messagebox.showinfo(message="Times up!")

label1 = Label(root,text="Countdown timer", font=("times new roman",17,"bold"),fg="purple").pack()
label2 = Label(root, text="Put 0 in the fields you do not use", font=("times new roman", 9)).pack()

hours = IntVar()
mins = IntVar()
secs = IntVar()
 
hour_entry=Entry(root,width=3,textvariable=hours,font=("times new roman",15))
min_entry=Entry(root,width=3,textvariable=mins,font=("times new roman",15))
sec_entry=Entry(root,width=3,textvariable=secs,font=("times new roman",15))
 
hour_entry.insert(0,00)
min_entry.insert(0,00)
sec_entry.insert(0,00)
 
hour_entry.place(x=100,y=60)
min_entry.place(x=140,y=60)
sec_entry.place(x=180,y=60)
 
hour_entry.bind("<1>", h_click)
min_entry.bind("<1>", m_click)
sec_entry.bind("<1>", s_click)

button = Button(root,text='Activate Timer',bg='green', command=timer).pack(pady=50)

root.mainloop()