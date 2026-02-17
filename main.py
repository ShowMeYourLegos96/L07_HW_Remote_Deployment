from menu import Menu


mainMenu = Menu()

mainMenu.addOption("Check available memory")
mainMenu.addOption("View Network Connections")
mainMenu.addOption("Display free ram and swap")
mainMenu.addOption("Quit")

choice = mainMenu.getInput()
