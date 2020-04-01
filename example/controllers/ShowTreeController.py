from core.Core import Core
from models.Customers import Customers
from core.Controller import Controller
from tkinter import messagebox


"""
    Responsible for ShowTreeView behavior.
"""
class ShowTreeController(Controller):
    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------
    def __init__(self):
        self.customers = Customers()
        self.showView = self.loadView("showTree")
        
    
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    """
        @return All customers in database
    """
    def getCustomers(self):
        data = self.customers.getAll()
        return data
    
    """
        Opens EditController
        
        @param id_customer Customer id that will be edited
    """
    def btnEdit(self, id_customer):
        customer = self.customers.get(id_customer)
        c = Core.openController("edit")
        c.main(customer, self.showView)
        
    """
        Deletes the chosen customer and updates the ShowView
        
        @param id_customer Customer id that will be edited
    """ 
    def btnDel(self, id_customer):
        self.customers.delete(id_customer)
        self.showView.update()
        messagebox.showinfo("Delete customer", "Customer deleted with success!")
        
    """
        @Override
    """
    def main(self):
        self.showView.main()
