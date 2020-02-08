import os
import importlib
from config import APP_PATH

class Core:   
    @staticmethod
    def openController(controller):
        response = None
        controller = controller[0].upper()+controller[1:]
        controllerName = controller+"Controller"
        
        # Check if file exists
        if os.path.exists(APP_PATH+"/Controllers/"+controllerName+".py"):
            module = importlib.import_module("Controllers."+controllerName)
            class_ = getattr(module, controllerName)
            response = class_()
        
        return response