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
                print("Warning! If this is your first time playing, refrain.")
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
            print("Quitting Game...")
            sleep(0.7)
            print("Game Quit!")
            exit()
            

        else: 
            print("Try again!")

# Intermission

sleep(0.7)
name = input("Name:")
sleep(0.8)
print(".")
sleep(0.8)
print("..")
sleep(0.8)
print("...")
sleep(2)

money = 0
inventory = []

# Act 1

if Act_1 == True:
    print("Act 1 intro:\n")
    sleep(2)
    print("You're a mechant from a distant land overseas.\n")
    sleep(3)
    print("On one of your more perilous expeditions, one of the local shamen serves you some kind of spiritual drink (which of course you accept).\n")
    sleep(5)
    print("Unfortunately for you, the drink was spicked.\n")
    sleep(3)
    print("And after what feels like just a moment,\n")
    sleep(3)
    print("you fall to the ground, unconscious.\n")
    
    input("Press 'enter' to continue\n")

    print("After a while, you start to regain your senses.\n")
    sleep(3)
    print("The cold air around you makes you shiver.\n")
    sleep(3)
    print("It seems you're not in the place you left off.\n")
    sleep(3)
    print("You open your eyes...\n")

    input("Press 'enter' to continue\n")

    print("After a quick look around, you notice you're in some cold cell with the only source of light coming form the hall outside it (this is not quite someplace you want to be).\n")
    sleep(3)
    print("The walls seem to be somewhat wet, stained with bits dark mold.\n")
    sleep(3)
    print("The cell's interior consists of a small wooden bedside table, and a cell door right in front of you, seemingly locked.\n")
    sleep(4)
    print("")


