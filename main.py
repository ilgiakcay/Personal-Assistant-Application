import tkinter as tk
from todo_manager import TodoManager
from journal_manager import JournalManager

class PersonalAssistantApp:
    def __init__(self, root):
        """
        Initialize the main application window and its components.
        """
        self.root = root
        self.root.title("Personal Assistant")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f8ff")  # Set background color
        
        # Display welcome message
        self.label = tk.Label(root, text="Welcome to Your Personal Assistant!", font=("Arial", 16, "bold"), bg="#f0f8ff")
        self.label.pack(pady=20)

        # Initialize buttons for To-Do list, Journal, and Exit
        self.todo_manager = TodoManager(self.root)
        self.journal_manager = JournalManager(self.root)

        todo_button = tk.Button(root, text="To-Do List", command=self.todo_manager.open_todo_list, width=20, bg="#4CAF50", fg="white", font=("Arial", 12))
        todo_button.pack(pady=10)

        journal_button = tk.Button(root, text="Journal", command=self.journal_manager.open_calendar, width=20, bg="#4CAF50", fg="white", font=("Arial", 12))
        journal_button.pack(pady=10)

        exit_button = tk.Button(root, text="Exit", command=root.quit, width=20, bg="#f44336", fg="white", font=("Arial", 12))
        exit_button.pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = PersonalAssistantApp(root)
    root.mainloop()
