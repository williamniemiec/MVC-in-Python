# -*- encoding:utf-8 -*-
from Core.Controller import Controller
from Core.Core import Core

class HomeController(Controller):
    def __init__(self):
        self.homeView = self.loadView("Home")
    
    def main(self):
        self.homeView.main()
        
    def btnClicked(self, caption):
        if caption == "Open Customers DB":
            c = Core.openController("show")
            c.main()
        elif caption == "Add customer":
            c = Core.openController("add")
            c.main()
        elif caption == "Show customers with TreeView":
            c = Core.openController("showTreeView")
            c.main()