from tkinter import messagebox
from tkinter.constants import END

from Models.Customers import Customers
from Core.Controller import Controller


class AddController(Controller):
    def __init__(self):
        self.addView = self.loadView("add")
        self.customers = Customers()
        
    def main(self):
        self.addView.main()
        
    def btn_clear(self, fields):
        for field in fields:
            field.delete(0, END)
            
    def btn_add(self, fields):
        response = self.customers.add(fields)
        
        if response > 0:
            messagebox.showinfo("Add customer", "Customer successfully added!")
        else:
            messagebox.showerror("Add customer", "Error while adding customer")
            
        self.addView.close()