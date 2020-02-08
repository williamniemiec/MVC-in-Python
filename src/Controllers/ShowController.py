from Core.Core import Core
from Models.Customers import Customers
from Views.show import Show
from tkinter import messagebox


class ShowController:
    def __init__(self):
        self.customers = Customers()
        self.showView = Show(self)
        self.core = Core()
        
    def main(self):
        self.showView.main()
        
    def getCustomers(self):
        data = self.customers.getAll()
        return data
    
    def btnEdit(self, id_customer):
        customer = self.customers.get(id_customer)
        c = self.core.openController("edit")
        c.main(customer, self.showView)
        
    def btnDel(self, id_customer):
        self.customers.delete(id_customer)
        self.showView.update()
        messagebox.showinfo("Delete customer", "Customer deleted with success!")
