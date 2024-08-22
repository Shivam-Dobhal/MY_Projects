# TASK 1 : Calendar Application 
# %%
import tkinter as tk # for provide GUI
from tkinter import messagebox # messagebox is used to display pop up window
from tkcalendar import Calendar # calendar for calendar widget
import datetime

class CalendarApp: # class which manage the all behaviour of application
    def __init__(self, root): # constructor method of class
        self.root = root
        self.root.title("Monthly Calendar with Reminders") # title for calendar application
        self.root.geometry("600x400")  # Initial size of the window

        # the rows and columns of the grid to expand or shrink when the window is resized.
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=0)
        self.root.grid_columnconfigure(1, weight=1)

        self.calendar = Calendar(
            root,
            selectmode='day', # that allow the user select single day
            # intialing the calendar to current date
            year=datetime.datetime.now().year,
            month=datetime.datetime.now().month,
            day=datetime.datetime.now().day,

            showothermonthdays=False, # days from other months are not shown , default value is True 
            showweeknumbers=False, # week number are hidden , default value is True
            background='orangered',
            foreground='lightpink',
            selectbackground='crimson',
            selectforeground='white',
            normalbackground="lightpink",
            weekendbackground="white",
            weekendforeground="red",
            font=("Arial", 16)
        )
        
        self.calendar.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=20, pady=20)

        self.reminders = {} # intializing a empty dictionary which store remainder , where key wiil date and value wiil remainder text

        self.reminder_text = tk.StringVar()

        tk.Label(root, text="Reminder:").grid(row=1, column=0, sticky="e", pady=5, padx=10)
        
        self.reminder_entry = tk.Entry(root, textvariable=self.reminder_text)
        self.reminder_entry.grid(row=1, column=1, sticky="ew", pady=5, padx=10)
        self.reminder_entry.insert(0, "Enter reminder for yyyy/mm/dd") # creating an placeholder
        self.reminder_entry.config(fg='grey')
        self.reminder_entry.bind("<FocusIn>", self.on_entry_click)
        self.reminder_entry.bind("<FocusOut>", self.on_focus_out)

        tk.Button(root, text="Set Reminder", command=self.set_reminder, bg='green', fg='white').grid(row=2, column=0, sticky="ew", pady=5, padx=10)
        tk.Button(root, text="Show Reminder", command=self.show_reminder, bg='blue', fg='white').grid(row=2, column=1, sticky="ew", pady=5, padx=10)

        # make the entry and buttons expand with the window
        self.root.grid_rowconfigure(1, weight=0)
        self.root.grid_rowconfigure(2, weight=0)
        self.root.grid_columnconfigure(1, weight=1)

    def on_entry_click(self, event):
        if self.reminder_entry.get() == "Enter reminder for yyyy/mm/dd":
            self.reminder_entry.delete(0, "end")  # delete all the text in the entry
            self.reminder_entry.config(fg='black')  # change text color to black

    def on_focus_out(self, event):
        if self.reminder_entry.get() == "":
            self.reminder_entry.insert(0, "Enter reminder for yyyy/mm/dd")
            self.reminder_entry.config(fg='grey') # change text color to grey

    def set_reminder(self):
        date = self.calendar.get_date()
        reminder = self.reminder_text.get()
        
        if reminder and reminder != "Enter reminder for yyyy/mm/dd":
            if self.is_valid_date(date):
                formatted_date = self.format_date(date)
                self.reminders[formatted_date] = reminder
                self.reminder_text.set("")
                self.reminder_entry.insert(0, "Enter reminder for yyyy/mm/dd")
                self.reminder_entry.config(fg='grey')  # change text color to grey
                messagebox.showinfo("Reminder Set", f"Reminder for {formatted_date}: {reminder}")
            else:
                messagebox.showwarning("Date Error", "Invalid date. Please select a valid date from the calendar.")
        else:
            messagebox.showwarning("Input Error", "Please enter a reminder.")

    def show_reminder(self):
        date = self.calendar.get_date()
        formatted_date = self.format_date(date)
        reminder = self.reminders.get(formatted_date, "No reminders for this date.")
        messagebox.showinfo("Reminder", f"Reminder for {formatted_date}: {reminder}")

    def is_valid_date(self, date_str):
        try:
            date = datetime.datetime.strptime(date_str, "%m/%d/%y").date()
            mindate = datetime.date(2024, 1, 1)
            maxdate = datetime.date(2024, 12, 31)
            return mindate <= date <= maxdate
        except ValueError:
            return False

    def format_date(self, date_str):
        date = datetime.datetime.strptime(date_str, "%m/%d/%y").date()
        return date.strftime("%Y/%m/%d")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()

# %%
