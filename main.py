import tkinter as tk
from tkinter import messagebox, ttk
from models import CompanyRecord
from database import initialize_database, add_record, get_records, update_record

class CompanyRecordsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Company Records Management")
        self.root.geometry("600x400")
        
        # Styling
        self.root.configure(bg="#f0f0f0")
        
        # Title Label
        self.title_label = tk.Label(root, text="Company Records Management", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Labels and Entries for the form
        self.name_label = tk.Label(root, text="Company Name", bg="#f0f0f0")
        self.name_label.grid(row=1, column=0, sticky=tk.E, padx=10, pady=5)
        self.name_entry = tk.Entry(root, width=30)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        self.role_label = tk.Label(root, text="Role", bg="#f0f0f0")
        self.role_label.grid(row=2, column=0, sticky=tk.E, padx=10, pady=5)
        self.role_entry = tk.Entry(root, width=30)
        self.role_entry.grid(row=2, column=1, padx=10, pady=5)

        self.package_label = tk.Label(root, text="Package", bg="#f0f0f0")
        self.package_label.grid(row=3, column=0, sticky=tk.E, padx=10, pady=5)
        self.package_entry = tk.Entry(root, width=30)
        self.package_entry.grid(row=3, column=1, padx=10, pady=5)

        self.shortlisted_label = tk.Label(root, text="Shortlisted (y/n)", bg="#f0f0f0")
        self.shortlisted_label.grid(row=4, column=0, sticky=tk.E, padx=10, pady=5)
        self.shortlisted_entry = tk.Entry(root, width=30)
        self.shortlisted_entry.grid(row=4, column=1, padx=10, pady=5)

        self.given_interview_label = tk.Label(root, text="Given Interview (y/n)", bg="#f0f0f0")
        self.given_interview_label.grid(row=5, column=0, sticky=tk.E, padx=10, pady=5)
        self.given_interview_entry = tk.Entry(root, width=30)
        self.given_interview_entry.grid(row=5, column=1, padx=10, pady=5)

        self.final_result_label = tk.Label(root, text="Selected in Final Result (y/n)", bg="#f0f0f0")
        self.final_result_label.grid(row=6, column=0, sticky=tk.E, padx=10, pady=5)
        self.final_result_entry = tk.Entry(root, width=30)
        self.final_result_entry.grid(row=6, column=1, padx=10, pady=5)

        # Buttons for actions
        self.add_button = tk.Button(root, text="Add Record", command=self.add_record, bg="#4CAF50", fg="white", width=15)
        self.add_button.grid(row=7, column=0, pady=10, padx=10)

        self.view_button = tk.Button(root, text="View Records", command=self.view_records, bg="#2196F3", fg="white", width=15)
        self.view_button.grid(row=7, column=1, pady=10, padx=10)

        self.update_button = tk.Button(root, text="Update Record", command=self.update_record, bg="#FF9800", fg="white", width=15)
        self.update_button.grid(row=8, column=0, pady=10, padx=10)

        self.delete_button = tk.Button(root, text="Delete Record", command=self.delete_record, bg="#F44336", fg="white", width=15)
        self.delete_button.grid(row=8, column=1, pady=10, padx=10)

        self.search_label = tk.Label(root, text="Search by Name", bg="#f0f0f0")
        self.search_label.grid(row=9, column=0, sticky=tk.E, padx=10, pady=5)
        self.search_entry = tk.Entry(root, width=30)
        self.search_entry.grid(row=9, column=1, padx=10, pady=5)
        self.search_button = tk.Button(root, text="Search", command=self.search_record, bg="#009688", fg="white", width=15)
        self.search_button.grid(row=10, column=1, pady=10, padx=10)

        self.exit_button = tk.Button(root, text="Exit", command=root.quit, bg="#9E9E9E", fg="white", width=15)
        self.exit_button.grid(row=10, column=0, pady=10, padx=10)

        self.records_text = tk.Text(root, width=60, height=10)
        self.records_text.grid(row=11, column=0, columnspan=2, padx=10, pady=10)

        initialize_database()

    def add_record(self):
        name = self.name_entry.get()
        role = self.role_entry.get()
        try:
            package = float(self.package_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Package must be a number.")
            return
        shortlisted = self.shortlisted_entry.get().lower() == 'y'
        given_interview = self.given_interview_entry.get().lower() == 'y'
        final_result = self.final_result_entry.get().lower() == 'y'

        record = CompanyRecord(name, role, package, shortlisted, given_interview, final_result)
        add_record(record)
        messagebox.showinfo("Info", "Record added successfully!")
        self.clear_entries()
        self.view_records()

    def view_records(self):
        records = get_records()
        self.records_text.delete(1.0, tk.END)
        self.records_text.insert(tk.END, records.to_string())

    def update_record(self):
        name = self.name_entry.get()
        role = self.role_entry.get()
        try:
            package = float(self.package_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Package must be a number.")
            return
        shortlisted = self.shortlisted_entry.get().lower() == 'y'
        given_interview = self.given_interview_entry.get().lower() == 'y'
        final_result = self.final_result_entry.get().lower() == 'y'

        updated_record = CompanyRecord(name, role, package, shortlisted, given_interview, final_result)
        update_record(name, updated_record)
        messagebox.showinfo("Info", "Record updated successfully!")
        self.clear_entries()
        self.view_records()

    def delete_record(self):
        name = self.name_entry.get()
        records = get_records()
        if name in records['name'].values:
            records = records[records['name'] != name]
            records.to_csv('company_records.csv', index=False)
            messagebox.showinfo("Info", "Record deleted successfully!")
            self.clear_entries()
            self.view_records()
        else:
            messagebox.showerror("Error", "Record not found.")

    def search_record(self):
        name = self.search_entry.get()
        records = get_records()
        result = records[records['name'] == name]
        self.records_text.delete(1.0, tk.END)
        if not result.empty:
            self.records_text.insert(tk.END, result.to_string())
        else:
            self.records_text.insert(tk.END, "No records found.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.role_entry.delete(0, tk.END)
        self.package_entry.delete(0, tk.END)
        self.shortlisted_entry.delete(0, tk.END)
        self.given_interview_entry.delete(0, tk.END)
        self.final_result_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CompanyRecordsApp(root)
    root.mainloop()
