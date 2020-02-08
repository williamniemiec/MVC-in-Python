# -*- encoding:utf-8 -*-
from Views.home import Home
from Core.Core import Core

class HomeController:
    def __init__(self):
        self.homeView = Home(self)
    
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