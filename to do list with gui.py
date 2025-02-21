import tkinter as tk
from tkinter import messagebox
import json

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)
            for task in tasks:
                task_listbox.insert(tk.END, task)
    except (FileNotFoundError, json.JSONDecodeError):
        pass

def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

def mark_done():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(tk.END, f"✔ {task}")
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

# Create main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Task entry widget
task_entry = tk.Entry(root, font=("Arial", 14))
task_entry.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack()

add_button = tk.Button(button_frame, text="Add", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(button_frame, text="Delete", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

mark_done_button = tk.Button(button_frame, text="Mark Done", command=mark_done)
mark_done_button.pack(side=tk.LEFT, padx=5)

# Task listbox
task_listbox = tk.Listbox(root, font=("Arial", 14), width=40, height=10)
task_listbox.pack(pady=10)

load_tasks()

root.mainloop()

