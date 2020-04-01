import unittest
from core.Core import Core
from controllers.HomeController import HomeController


class CoreTest(unittest.TestCase):    
    def testName(self):
        controller = Core.openController("Home")
        self.assertIsInstance(controller, HomeController)
        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()