import json
import os
import tkinter as tk  # Import tkinter as tk for using tkinter functions
from tkinter import Toplevel, Text, END, messagebox
from tkcalendar import Calendar

class JournalManager:
    """
    Manages journal entries by allowing the user to create, view, and save journal entries by date.
    Entries are stored in a JSON file for persistence.
    """

    def __init__(self, root):
        """
        Initializes the JournalManager class with necessary file paths and loads journal data if available.
        
        Parameters:
        root (Tk): The main window instance of the application.
        """
        self.root = root
        self.journal_file = "journals.json"
        self.journals = self.load_journals()

    def open_calendar(self):
        """
        Opens a calendar window for selecting a date. After selecting the date, it opens the journal entry window for that date.
        """
        calendar_window = Toplevel(self.root)
        calendar_window.title("Select Date for Journal")
        calendar_window.geometry("300x300")
        calendar_window.configure(bg="#e6f7ff")

        cal = Calendar(calendar_window, selectmode='day', date_pattern='yyyy-mm-dd')
        cal.pack(pady=20)

        select_button = tk.Button(calendar_window, text="Write Journal", command=lambda: self.open_journal_entry(cal.get_date(), calendar_window), bg="#4CAF50", fg="white", font=("Arial", 12))
        select_button.pack(pady=10)

    def open_journal_entry(self, selected_date, calendar_window):
        """
        Opens a new window to create or view a journal entry for the selected date.
        
        Parameters:
        selected_date (str): The date selected from the calendar in 'YYYY-MM-DD' format.
        calendar_window (Toplevel): The calendar window instance that is closed after the date is selected.
        """
        calendar_window.destroy()

        journal_window = Toplevel(self.root)
        journal_window.title(f"Journal Entry for {selected_date}")
        journal_window.geometry("400x400")
        journal_window.configure(bg="#e6f7ff")

        journal_text = Text(journal_window, width=50, height=15, font=("Arial", 12), bg="#f9f9f9")
        journal_text.pack(pady=10)

        # If a journal entry for the selected date exists, load it into the text box
        if selected_date in self.journals:
            journal_text.insert(END, self.journals[selected_date])

        save_button = tk.Button(journal_window, text="Save Journal", command=lambda: self.save_journal(selected_date, journal_text.get("1.0", END), journal_window), bg="#4CAF50", fg="white", font=("Arial", 12))
        save_button.pack(pady=10)

    def save_journal(self, date, entry, journal_window):
        """
        Saves the journal entry for the selected date to the JSON file. 
        
        Parameters:
        date (str): The date for which the journal entry is being saved.
        entry (str): The text content of the journal entry.
        journal_window (Toplevel): The window instance of the journal entry that is closed after saving.
        """
        if entry.strip():
            self.journals[date] = entry.strip()  # Save the journal entry
            self.save_journals()
            journal_window.destroy()
            messagebox.showinfo("Success", f"Journal entry for {date} saved.")
        else:
            messagebox.showwarning("Empty Entry", "Journal entry cannot be empty.")

    def load_journals(self):
        """
        Loads journal entries from the JSON file if it exists. Returns an empty dictionary if the file doesn't exist.
        
        Returns:
        dict: A dictionary of journal entries with the date as the key and the entry text as the value.
        """
        if os.path.exists(self.journal_file):
            with open(self.journal_file, "r") as file:
                return json.load(file)
        return {}

    def save_journals(self):
        """
        Saves the current journal entries to the JSON file.
        """
        with open(self.journal_file, "w") as file:
            json.dump(self.journals, file, ensure_ascii=False, indent=4)
