# Personal-Assistant-Application

  This is a Personal Assistant Application built using Python and Tkinter, aimed at helping users organize tasks and journals efficiently. The application includes task management, journaling, and categorization features, all within an intuitive graphical user interface (GUI).

# Features
Task Management:
  Add, delete, and mark tasks as completed.
  Sort tasks by due date.
  Task categorization (e.g., Work, Personal, School) and priority levels (High, Medium, Low).
Journaling:
  Create journal entries for specific dates using a calendar.
  View, edit, and save journal entries.
User-Friendly Interface:
  Modern, intuitive UI using Tkinter with customized fonts, buttons, and layouts.
  Data is saved persistently using JSON files, ensuring that tasks and journal entries are available after restarting the application.
# Project Structure
  The project has been structured into multiple Python files for better readability and maintainability:

  main.py: Initializes the main window and handles navigation between different sections (tasks and journal).
  task_manager.py: Manages the task-related functionalities, such as adding, updating, and deleting tasks.
  journal_manager.py: Handles the journal functionality, allowing users to create and manage journal entries.
  utils.py: Contains helper functions like saving and loading data from JSON files.

# Usage
Task Manager:

  Open the "To-Do List" from the main screen.
  Add a task, description, due date, category, and priority level.
  View all tasks, mark them as complete, or delete tasks.
  
Journal:

  Open the "Journal" from the main screen.
  Pick a date from the calendar and write your journal entry.
  Save the entry for future reference.
  
# Data Persistence
  All tasks and journal entries are saved in tasks.json and journals.json files, respectively, ensuring that your data is persisted across sessions.
