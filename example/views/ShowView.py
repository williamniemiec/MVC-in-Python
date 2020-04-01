import tkinter as tk
from tkinter import ttk
from views.View import View


"""
    View responsible for showing registered customers.
"""
class ShowView(tk.Tk, View):
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
        self.title("Show Customers")
        self.showController = controller
    
        self._make_mainFrame()
        self._make_title()
        self._show_customers()
    
   
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    """
        Creates view's frame.
    """ 
    def _make_mainFrame(self):
        self.frame_main = ttk.Frame(self)
        self.frame_main.pack(padx=self.PAD, pady=self.PAD)
        
    """
        Sets view's title.
    """
    def _make_title(self):
        title = ttk.Label(self.frame_main, text="Customers Manager - Show", font=("Helvetica", 20))
        title.pack(padx=self.PAD, pady=self.PAD)
    
    """
        Displays customers on screen.
    """
    def _show_customers(self):
        customers = self.showController.getCustomers()
        frame_customers = tk.Frame(self.frame_main)
        frame_customers.pack(fill="x")
        self.frame_customers = frame_customers
        
        data_frame = tk.Frame(frame_customers)
        data_frame.pack()
        
        # Show header
        lbl = ttk.Label(data_frame, text="Action")
        lbl.grid(row=0, column=0, padx=self.PAD, pady=self.PAD)
        
        j = 1
        for caption in self.THEADER:
            lbl = ttk.Label(data_frame, text=caption)
            lbl.grid(row=0, column=j, padx=self.PAD, pady=self.PAD)
            j += 1
        
        
        # Show data
        for index,values in enumerate(customers):
            j = 1
            index += 1
            
            frame_actions = tk.Frame(data_frame)
            frame_actions.grid(row=index, column=0, padx=self.PAD, pady=5)
            
            # Make edit button
            btn_edit = ttk.Button(frame_actions, text="Edit", command=lambda id=values[0]: self.showController.btnEdit(id))
            btn_edit.pack(side="left")
            
            # Make delete button
            btn_exc = ttk.Button(frame_actions, text="Delete", command=lambda id=values[0]: self.showController.btnDel())
            btn_exc.pack(side="left")
            
            # Put customer data on screen
            for item in values:
                lbl = tk.Label(data_frame, text=item)
                lbl.grid(row=index, column=j, padx=self.PAD, pady=5)
                j += 1
        
        btn = ttk.Button(frame_customers, text="Update data", command=self.update)
        btn.pack()
        
    """
        Refreshes view.
    """
    def update(self):
        self.frame_customers.destroy()
        self._show_customers()
        
    """
    @Overrite
    """
    def main(self):
        self.mainloop()
        
    """
    @Overrite
    """
    def close(self):
        return
        