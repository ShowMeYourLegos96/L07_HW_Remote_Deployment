class Menu:
    def __init__(self):
        self.options = []
    
    def addOption(self,option):
        self._options.append(option)
    
    def getInput(self):
        self.input = input
    