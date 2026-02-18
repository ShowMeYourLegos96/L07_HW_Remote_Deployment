import run_bash_cmd_function
def main():
 mainMenu = Menu()

 def options_constructor():
    pass
if __name__ == '__main__':
    from menu import Menu
    main()


#call the class
mainMenu = Menu()

#call the methods in the class to add in the options
mainMenu.addOption("Check available memory")
mainMenu.addOption("View Network Connections")
mainMenu.addOption("Display free ram and swap")
mainMenu.addOption("Quit")

#calling the getUserInput method to collect the user input
choice = mainMenu.getInput()
