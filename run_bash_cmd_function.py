#import os
#def run_bash_cmd(some_choice):
    #print('-' * 80, '\n')
    #print('You entered #', some_choice)
    #if (some_choice == 1):
        #print('The available memory is ')
        #os.system('free -tmh')
    #elif (some_choice == 2):
        #print('The current network connections include: ')
        #os.system('netstat -an | grep -i Estab | cut -d \':\' -f 2,3 | gawk \'{print $2}\' | grep [0-9] | uniq')
    #elif (some_choice == 3):
        #print('Available file space is: ')
        #os.system('df -h | grep \"Filesystem\|root\"')
    #return

import subprocess #a better built in library then os
#create dictionary that would hold in the 3 options, each options has a number to define it
Commands = { 
            1:{"description": "The available memory is:", "command":["free","-tmh"],},
            2:{"description": "The current networks connections include:", "command": "netstat -an | grep -i Estab | cut -d ':' -f 2,3 |" "gawk '{print $2}' | grep [0-9] | uniq",
                },
            3:{"description": "Available file space is:","command":"df -h | grep 'Filesystem\\|root'",
               },
             }
#create a function that would hold the choice that you have made
def run_bash_cmd(some_choice ):
    print("-" * 80)
    print(f"You entered {some_choice}")

    com = Commands.get(some_choice) #will get the one of the 3 choices from the dictionary
    #incase the user doesn't pick the correct choice
    if not com:
        print("Invalid choice")
        return
    
    print(com["description"]) #used to print out the description of the given choice

    #will raise an exception if the given command fails
    try:
        #create a conditonal that will check if the given object is a list type
        if isinstance(com["command"],list):
            result = subprocess.run(com["command"],check=True)
        else:
            # Needed for pipelines
            result = subprocess.run(com["command"], shell=True, check=True)

    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")