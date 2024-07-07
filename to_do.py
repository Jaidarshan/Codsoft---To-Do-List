# Task 1: To-Do List
import tkinter as tk
from tkinter import messagebox
def add_task():
    task=task_entry.get()
    if task:
        tasks_listbox.insert(tk.END,task)
        task_entry.delete(0,tk.END)
    else:
        messagebox.showwarning("Warning","You must enter a task.")
def remove_task():
    try:
        selected_task_index=tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning","You must select a task to remove.")
window=tk.Tk()
window.title("Simple To-Do List")
window.geometry("400x430")
heading=tk.Label(window,text="To-Do List",font=("Helvetica",20,"bold"))
heading.pack(padx=10)
task_entry_label=tk.Label(window,text="Enter the task :",font=("Helvetica",11))
task_entry_label.pack(padx=10)
task_entry=tk.Entry(window, width=50)
task_entry.pack(pady=10)
add_task_button=tk.Button(window,text="Add Task",command=add_task,bg="blue",fg="white",font=("Helvetica",12,"bold"))
add_task_button.pack(pady=5)
tasks_listbox_label=tk.Label(window,text="Tasks",font=("Helvetica",11))
tasks_listbox_label.pack(pady=5)
tasks_listbox=tk.Listbox(window,width=50,height=10,font=("Helvetica",10))
tasks_listbox.pack(pady=10)
remove_task_button=tk.Button(window,text="Remove Task",command=remove_task,bg="blue",fg="white",font=("Helvetica",12,"bold"))
remove_task_button.pack(pady=5)
window.mainloop()
