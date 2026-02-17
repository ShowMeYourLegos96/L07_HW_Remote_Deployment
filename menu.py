import run_bash_cmd_function
class Menu:
    def __init__(self):
        self.options = []
    
    def addOption(self, option):
        self.options.append(option)
        
    
    def getInput(self):
        
        for GI in self.options:
            #print(f'{self.options}')
            GI = int(input(f'{self.options}')) #makes this string into integer
            print("GI type is ", type(GI)) #type is now an integer

            if GI == 1 or 2 or 3:#checks if the input is 1,2, or 3 
             run_bash_cmd_function(GI)#will run the function 
             continue #will repeat the prompt for the user to enter again

            elif GI == 4: #if user press quit
                break
            else: #if the user picks an invalid input
                print("Please enter the correct value")
                continue
        #self.input = input(self.options)
        #self.input = int(input)
    