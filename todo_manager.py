import tkinter as tk
from tkinter import Listbox, END, messagebox, StringVar, OptionMenu
from datetime import datetime
import json
import os

class TodoManager:
    def __init__(self, root):
        """
        Initialize the To-Do Manager.
        """
        self.tasks_file = "tasks.json"
        self.tasks = []
        self.load_tasks()

    def open_todo_list(self):
        """
        Create a new window for the To-Do List and add related components.
        """
        self.todo_window = tk.Toplevel()
        self.todo_window.title("To-Do List")
        self.todo_window.geometry("600x600")
        self.todo_window.configure(bg="#e6f7ff")

        self.task_entry = tk.Entry(self.todo_window, width=30, font=("Arial", 12))
        self.task_entry.pack(pady=5)
        self.task_entry.insert(0, "Enter Task")

        self.description_entry = tk.Entry(self.todo_window, width=30, font=("Arial", 12))
        self.description_entry.pack(pady=5)
        self.description_entry.insert(0, "Enter Description")

        self.date_entry = tk.Entry(self.todo_window, width=30, font=("Arial", 12))
        self.date_entry.pack(pady=5)
        self.date_entry.insert(0, "Enter Due Date (YYYY-MM-DD)")

        self.category_var = StringVar(self.todo_window)
        self.category_var.set("Select Category")
        categories = ["Work", "Personal", "School"]
        self.category_menu = OptionMenu(self.todo_window, self.category_var, *categories)
        self.category_menu.pack(pady=5)

        self.priority_var = StringVar(self.todo_window)
        self.priority_var.set("Select Priority")
        priorities = ["High", "Medium", "Low"]
        self.priority_menu = OptionMenu(self.todo_window, self.priority_var, *priorities)
        self.priority_menu.pack(pady=5)

        add_button = tk.Button(self.todo_window, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white", font=("Arial", 12))
        add_button.pack(pady=10)

        self.task_list = Listbox(self.todo_window, width=50, height=15, font=("Arial", 12), bg="#f9f9f9", selectbackground="#a6c8ff")
        self.task_list.pack(pady=10)

        tick_button = tk.Button(self.todo_window, text="✓ Complete", command=self.toggle_status, bg="#FFD700", font=("Arial", 12))
        tick_button.pack(side=tk.LEFT, padx=20)

        delete_button = tk.Button(self.todo_window, text="Delete", command=self.delete_task, bg="#f44336", fg="white", font=("Arial", 12))
        delete_button.pack(side=tk.RIGHT, padx=20)

        self.update_task_list()

    def add_task(self):
        """
        Add a new task to the To-Do list, save it, and update the display.
        """
        task = self.task_entry.get()
        description = self.description_entry.get()
        date = self.date_entry.get()
        category = self.category_var.get()
        priority = self.priority_var.get()
        
        try:
            datetime.strptime(date, "%Y-%m-%d")
            if task and description and date:
                self.tasks.append({
                    "task": task,
                    "description": description,
                    "date": date,
                    "category": category,
                    "priority": priority,
                    "status": False
                })
                self.sort_tasks_by_date()
                self.update_task_list()
                self.save_tasks()
                self.task_entry.delete(0, END)
                self.description_entry.delete(0, END)
                self.date_entry.delete(0, END)
            else:
                messagebox.showwarning("Incomplete Information", "Please fill in all fields.")
        except ValueError:
            messagebox.showwarning("Invalid Date", "Please enter a valid date in YYYY-MM-DD format.")

    def load_tasks(self):
        """
        Load tasks from a JSON file if it exists.
        """
        if os.path.exists(self.tasks_file):
            with open(self.tasks_file, "r") as file:
                self.tasks = json.load(file)

    def save_tasks(self):
        """
        Save tasks to a JSON file.
        """
        with open(self.tasks_file, "w") as file:
            json.dump(self.tasks, file)

    def update_task_list(self):
        """
        Update the visual task list displayed in the To-Do window.
        """
        self.task_list.delete(0, END)
        for idx, task in enumerate(self.tasks):
            status = "✓" if task['status'] else "✗"
            self.task_list.insert(END, f"{task['task']} | {task['description']} | {task['date']} | {task['category']} | {task['priority']} [{status}]")

    def toggle_status(self):
        """
        Toggle the status of a selected task (completed/incomplete).
        """
        selected = self.task_list.curselection()
        if selected:
            idx = selected[0]
            self.tasks[idx]["status"] = not self.tasks[idx]["status"]
            self.update_task_list()
            self.save_tasks()

    def delete_task(self):
        """
        Delete the selected task from the list.
        """
        selected = self.task_list.curselection()
        if selected:
            idx = selected[0]
            del self.tasks[idx]
            self.update_task_list()
            self.save_tasks()

    def sort_tasks_by_date(self):
        """
        Sort tasks by their due date.
        """
        self.tasks.sort(key=lambda x: datetime.strptime(x['date'], "%Y-%m-%d"))
