import os
import importlib
from config import APP_PATH

class Controller:   
    def loadView(self, viewName):
        response = None
        
        # Set view name
        viewName = viewName[0].upper()+viewName[1:]
        
        # Check if file exists
        if os.path.exists(APP_PATH+"/Views/"+viewName+".py"):
            module = importlib.import_module("Views."+viewName)
            class_ = getattr(module, viewName)
            response = class_(self)
        
        return response