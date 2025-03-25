from tkinter import messagebox
from tkinter.constants import END
from models.Customers import Customers
from core.Controller import Controller
from src.utils import (
    seconds_to_readable_time,
    format_bytes,
    format_percentage_change,
    free_up_disk_space,
    get_start_end_of_week_by_offset,
)

"""
    Responsible for AddView behavior.
"""


class AddController(Controller):
    # -----------------------------------------------------------------------
    #        Constructor
    # -----------------------------------------------------------------------
    def __init__(self):
        self.addView = self.loadView("add")
        self.customers = Customers()

    # -----------------------------------------------------------------------
    #        Methods
    # -----------------------------------------------------------------------
    """
        Clear all fields of AddView
        
        @param fields Fields to be cleared
    """

    def btn_clear(self, fields):
        for field in fields:
            field.delete(0, END)

    """
        Adds a new customer with field data
        
        @param fields Fields with customer data
    """

    def btn_add(self, fields):
        response = self.customers.add(fields)

        if response > 0:
            messagebox.showinfo("Add customer", "Customer successfully added!")
        else:
            messagebox.showerror("Add customer", "Error while adding customer")

        self.addView.close()

    def test(self, fields):
        getAll = self.customers.getAll()
        sec = seconds_to_readable_time(1)
        format_bytes(123)
        format_percentage_change(1, 2)
        free_up_disk_space(None)
        get_start_end_of_week_by_offset(None)

    """
        @Override
    """

    def main(self):
        self.addView.main()
