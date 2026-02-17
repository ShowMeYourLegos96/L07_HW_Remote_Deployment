import menu 

mainMenu = menu()

mainMenu.addOption("Check available memory")
mainMenu.addOption("View Network Connections")
mainMenu.addOption("Display free ram and swap")
mainMenu.addOption("Quit")

choice = mainMenu.getInput()
