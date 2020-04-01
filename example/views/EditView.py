import tkinter as tk
from tkinter import ttk
from views.View import View


"""
    View responsible for edit customers.
"""
class EditView(tk.Tk, View):
    #-----------------------------------------------------------------------
    #        Constants
    #-----------------------------------------------------------------------
    PAD = 10
    THEADER = [
        "Id", "First name", "Last name", "Zipcode", "Price paid" 
    ]

    
    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------
    """
        @param controller Controller of this view
    """
    def __init__(self, controller):
        super().__init__()
        self.editController = controller
        self.title("Customers Manager - Edit")


    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    """
        Creates view's frame.
    """
    def _make_mainFrame(self):
        self.frame_main = tk.Frame(self)
        self.frame_main.pack()
        
    """
        Sets view's title.
    """
    def _make_title(self):
        title = ttk.Label(self.frame_main, text="Customers Manager", font=("Helvetica", 20))
        title.pack(padx=self.PAD, pady=self.PAD)
        
    """
        Creates customer fields.
    """
    def _show_customerFields(self):
        customer = self.editController.getCustomer()
        frame_customer = tk.Frame(self.frame_main)
        frame_customer.pack()
        id_customer = customer[0]
        fields = []
        
        for i in range(0, len(customer)):
            # Show headers
            lbl = tk.Label(frame_customer, text=self.THEADER[i])
            lbl.grid(row=i, column=0)
            
            # Show customer data
            e = ttk.Entry(frame_customer, width=30)
            e.insert(0, customer[i])
            fields.append(e)
            
            # Let id field as read_only
            if i == 0:
                e.configure(state="readonly")
            
            e.grid(row=i, column=1)
        
        
        
        # Show clear button
        frame_customer_buttons = tk.Frame(self.frame_main)
        frame_customer_buttons.pack()
        btn_submit = ttk.Button(frame_customer_buttons, text="Save", command=lambda: self.editController.btnSave(fields))
        btn_submit.pack(side='right')
    
    """
    @Overrite
    """
    def main(self):
        self._make_mainFrame()
        self._make_title()
        self._show_customerFields()
        
        self.attributes("-topmost", True)
        self.mainloop()
    
    """
    @Overrite
    """
    def close(self):
        self.destroy()