from tkinter import ttk
import tkinter as tk
from views.View import View


"""
    View responsible for showing registered customers.
"""
class ShowTreeView(tk.Tk, View):
    #-----------------------------------------------------------------------
    #        Constants
    #-----------------------------------------------------------------------
    PAD = 10
    COLUMN_WIDTH = 200
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
        self.showTreeViewController = controller
    
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
        Refreshes view.
    """
    def update(self):
        self.frame_customers.destroy()
        self._show_customers()
        
    
    """
        Displays view's context menu.
    """
    def _contextMenu_display(self, event):
        self.contextMenu = tk.Menu(self.frame_main, tearoff=0)
        self.contextMenu.add_command(label="Edit", command=lambda: self.showTreeViewController.btnEdit(self.contextMenu_selectedId))
        self.contextMenu.add_command(label="Delete", command=self.showTreeViewController.btnDel)
        
        # Take data from the row that was clicked
        # Ex: tv.item(data) => {'text': 1, 'image': '', 'values': ['name', 'lastname', 3213, '321.00'], 'open': 0, 'tags': ''}
        rowSelected = self.tv.identify_row(event.y)

        # Check if some data was taken
        if rowSelected:
            # Take data selected and put them in a list
            self.contextMenu_selectedId = self.tv.item(rowSelected)['text']
            
            # Let the row that was clicked as selected
            self.tv.focus(rowSelected)
            self.tv.selection_set(rowSelected)
            
            # Open context menu
            self.contextMenu.selection = self.tv.set(rowSelected)
            self.contextMenu.post(event.x_root, event.y_root)
    

    """
        Displays customers on screen.
    """
    def _show_customers(self):
        customers = self.showTreeViewController.getCustomers()
        
        self.frame_customers = tk.Frame(self.frame_main)
        self.frame_customers.pack(fill="x")
        
        frame_customersView = tk.Frame(self.frame_customers)
        frame_customersView.pack()
        
        # Create TreeView widget
        self.tv = ttk.Treeview(frame_customersView)
        
        # Create columns and name them (so them can be referenced)
        self.tv['columns'] = self.THEADER[1:]
        
        # Put columns info
        # Header
        self.tv.heading("#0", text=self.THEADER[0], anchor=tk.W)
        self.tv.column("#0", anchor=tk.W, width=100)
        for i in range(1, len(self.THEADER)):
            self.tv.heading(self.THEADER[i], text=self.THEADER[i])
            self.tv.column(self.THEADER[i], anchor="center", width=self.COLUMN_WIDTH)
        
        # Data
        for customer in customers:
            self.tv.insert("", tk.END, text=customer[0], values=customer[1:])
        
        # Put tree view on frame
        self.tv.grid(sticky=(tk.N, tk.S, tk.W, tk.E))
        self.tv.grid_rowconfigure(0, weight=1)
        self.tv.grid_columnconfigure(0, weight=1)
        
        # Add listener for enable the context menu
        self.tv.bind("<Button-3>", self._contextMenu_display)
        
        
        btn = ttk.Button(self.frame_customers, text="Update data", command=self.update)
        btn.pack()
        
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
