# -*- encoding:utf-8 -*-
from Core.Core import Core

class Main:
    @staticmethod
    def run():
        try:
            app = Core.openController("home")
            app.main()
        except Exception as e:
            print(str(e))

if __name__ == '__main__':
    Main.run()