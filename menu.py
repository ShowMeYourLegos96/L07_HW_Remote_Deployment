import os
import run_bash_cmd_function
class Menu:
    def __init__(self):
        self.options = []
    
    def addOption(self,option):
        self.options.append(option)

    
    def getInput(self):
        GI = input(f'{len(self.options)}')
        while GI == 1 or 2 or 3 or 4:
            GI = input(f'{len(self.options)}')
            if GI != 1 or 2 or 3 or 4:
             print("Please enter the correct value")
            elif GI == 4:
                break
            else:
                run_bash_cmd_function(GI)
        #self.input = input(self.options)
        #self.input = int(input)
    