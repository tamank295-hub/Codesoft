from tkinter import *
from tkinter import messagebox

def newtask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0,"end")
    else:
        messagebox.showwarning("ALERT", "first enter some task")

def deletetask():
    lb.delete(ANCHOR)

root =Tk()
root.geometry('500x400+500+200')
root.title('to do app')
root.configure(bg= '#E3CF57')
root.resizable(width= FALSE, height= FALSE)

Frame1 = Frame(root)
Frame1.pack(pady=10)

lb= Listbox(Frame1, width=25,height=8,font=('Times',18),bd=0,fg='#C1CDCD',highlightthickness=0,selectbackground='#7FFFD4',activestyle="none",)
lb.pack(side=LEFT, fill=BOTH)

task_list = ['eat breakfast','go college','study','have lunch','assignment','dinner','nap']
for item in task_list:
    lb.insert(END, item)


sb = Scrollbar(Frame1)
sb.pack(side=RIGHT, fill=BOTH)
lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)
my_entry = Entry(root,font=('Times',24))
my_entry.pack(pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)
addTask_button= Button(button_frame,text='Add New Task',font=('Times 14'),bg='#c5f776',padx=20,pady=10,command=newtask)
addTask_button.pack(fill=BOTH,expand=True,side=LEFT)

deleteTask_button= Button(button_frame,text='Delete Task',font=('Times 14'),bg='#ff8b61',padx=20,pady=10,command=deletetask)
deleteTask_button.pack(fill=BOTH,side=LEFT,expand=True)

root.mainloop()
