import os
class Menu:
    def __init__(self):
        self.options = []
    
    def addOption(self,option):
        self._options.append(option)

    
    def getInput(self):
        GI = input(f'{len(self.options)}')
        while GI == True:
            GI = input(f'{len(self.options)}')
            if GI != 1 or 2 or 3 or 4:
             print("Please enter the correct value")
            elif GI == 4:
                break
            else:
                GI.system()
        #self.input = input(self.options)
        #self.input = int(input)
    