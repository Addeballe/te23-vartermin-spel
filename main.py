from time import sleep

sleep(0.5)
print("Welcome to The (not so) Great Adventure!")
input("Press 'enter' to continue")
sleep(0.5)

Act_1 = False
Act_2 = False
Act_3 = False
Secret = False

# main menu

while True:
    if Act_1 == True or Act_2 == True or Act_3 == True or Secret == True:
        break

    else:
        print("[1] Start Game\n[2] Level Select (spoilers)\n[3] Quit Game")
        main_menu_choice = int(input())
        sleep(0.3)

        if main_menu_choice == 1:
            Act_1 = True
            print("Begun Act 1!")
            break

        elif main_menu_choice == 2:
            
            while True:
                print("[1] Act_1\n[2] Act_2\n[3] Act_3\n[4] Secrets\n[5] Go back")
                print("Warning! If this is your first time playing, character dialouge won't make sense.")
                level_select_choice = int(input())
                sleep(0.3)

                if level_select_choice == 1:
                    Act_1 = True
                    print("Begun Act 1!")
                    break
                elif level_select_choice == 2:
                    Act_2 = True
                    print("Begun Act 2!")
                    break
                elif level_select_choice == 3:
                    Act_3 = True
                    print("Begun Act 3!")
                    break
                elif level_select_choice == 4:
                    Secret = False
                    print("Ew")
                    break
                elif level_select_choice == 5:
                    break
                else:
                    print("Try again!")

        elif main_menu_choice == 3:
            print("Quitting Game.")
            sleep(0.7)
            print("Quitting Game..")
            sleep(0.7)
            print("Quitting Game...")
            sleep(0.7)
            print("Game Quit!")
            exit()
            

        else: 
            print("Try again!")

# Intermission

sleep(0.7)
name = input("What is your name?")
sleep(0.8)
print(".")
sleep(0.8)
print("..")
sleep(0.8)
print("...")
sleep(1.4)

money = 0
inventory = []

# Act 1

if Act_1 == True:
    
    