import pprint
from colorama import Fore, Back, Style, init
init()
from save_load import save_file, load_file

# Dictionary (Character Sheet)
character = {
    
    "stats": {},

    "inventory": {
        "gold": 0,
        "items": []
    }
}

# === Main menu code ===#
def create_character():

    global character
    
    while True:
        
        print(f"\nWelcome to GAME!\n")
        print(f"Load Previous Character")
        print(f"Create New Character")
        print(f"Exit Game")

        start_game = input(f"What would you like to do? :  ").strip().lower() #.strip() removes whitespace in inputs.  .lower() lowercases inputs

        # named command list for accessibility (I have come to really like these for this systme)
        load_char = ["1", "load", "previous", "load preavious character", "continue", "load game", "1. load previous character"]
        new_char = ["2", "new", "new game", "create new game", "new character", "create new character", "2. create new character", "start new game", "start new character"]
        exit_game = ["3", "exit", "quit", "back", "close", "quit game", "exit game", "close game", "stop"]

        # sets condition to load json file and then move to action menu
        if start_game in load_char:
            character = load_file("character.json")
            print(f"Character loaded.")
            break

        # sets condition to creat new character, running through new info and stats and then save the character as json and move to action menu
        elif start_game in new_char:    
            char_info()
            char_stats()
            save_file(character, "character.json")
            break

        elif start_game in exit_game:
            print(f"\nGoodby\n")
            exit() # exit() closes the script in the console

        else:
            print(f"Invalid, please try again")

# === Action menu code === #
def action_menu():
    while True:

        print(f"1. Open Character Editor")
        print(f"2. Open Inventory")
        print(f"3. Main Menu")
        print(f"4. Quit Game")

        action = input(f"What would you like to do? :  ").strip().lower()

        # named command list for accessibility (again)
        action_char_edit = ["1", "open character editor", "character editor", "open editor", "1. open character editor"]
        action_char_inv = ["2", "open inventory", "inventory", "2. open inventory"]
        action_main_menu = ["3", "return", "main menu", "open main menu", "3. main menu", "back"]
        action_quit_game = ["4", "quit", "quit game", "close game", "exit", "close", "stop", "end task", "4. quit game"]
        
        if action in action_char_edit:
            char_edit()
        elif action in action_char_inv:
            char_inv()
        elif action in action_main_menu:
            print(f"Returning to main menu.")
            break
        elif action in action_quit_game:
            print(f"\nGoodbye\n")
            exit()
        else:
            print("Invalid input")

# === Character info code === #
def char_info():
    char_name = input(f"Please name your character. :  ")
    character["char_name"] = char_name

    char_race = input(f"Please choose a race. :  ")
    character["char_race"] = char_race

    char_class = input(f"Please choose a class. :  ")
    character["char_class"] = char_class

    character["char_lvl"] = 1
    lvl_command = input("When prompted to do so, type 'level up' to increase your level!  ").lower()
    if lvl_command == "level up":
        character["char_lvl"] += 1
        print(f"You are now level {character['char_lvl']}!")

# === Stat block code === #
def char_stats():
    strength = int(input(f"Enter Strength:  "))
    character["stats"]["strength"] = strength

    dexterity = int(input("Enter Dexterity:  "))
    character["stats"]["dexterity"] = dexterity

    constitution = int(input("Enter Constitution:  "))
    character["stats"]["constitution"] = constitution

    intelligence = int(input(f"Enter Intelligence:  "))
    character["stats"]["intelligence"] = intelligence

    wisdom = int(input("Enter Wisdom:  "))
    character["stats"]["wisdom"] = wisdom

    charisma = int(input("Enter Charisma:  "))
    character["stats"]["charisma"] = charisma

# === Character editor === #
def char_edit():

    while True:

        print(f"\nCharacter Edit: \n")
        print(f"1. Edit Class")
        print(f"2. Edit Stats")
        print(f"3. View Stats")
        print(f"4. Close Edit Menu")

        edit_menu = input(f"Please select an option to continue. :  ").strip().lower()

        # -- named list for accessibility -- #
        edit_class_command = ["1", "edit class", "class", "set class", "change class", "1. edit class"]
        edit_stats_command = ["2", "edit stats", "stats", "set stats", "change stats", "2. edit stats"]
        view_stats_command = ["3", "view stats", "view", "3. view stats"]
        edit_quit_command = ["4", "quit", "quit edit menu", "quit edit", "exit", "exit", "stop", "close", "4. quit edit menu"]

        if edit_menu in edit_class_command:
            
            print(f"\nChange your class:")
            change_class = input(f"Choose a new class: ").strip()

            if change_class == "":
                print(f"Invalid format")
            
            elif change_class == "back":
                continue

            else:
                character["char_class"] = change_class
                print(f"Your class has been set to {character['char_class']}. ")
        
        elif edit_menu in edit_stats_command:

            print(f"\nUpdate your stats:")
            update_stats = input(f"What stat are you updating? :  ").strip().lower()
            
            if update_stats == "strength":
                new_strength = int(input(f"What is your new strength stat? :  "))
                character["stats"]["strength"] = new_strength
                print(f"Your strength has been updated to {character['stats']['strength']}.")

            elif update_stats == "dexterity":
                new_dexterity = int(input(f"What is your new dexterity stat? :  "))
                character["stats"]["dexterity"] = new_dexterity
                print(f"Your dexterity has been updated to {character['stats']['dexterity']}.")

            elif update_stats == "constitution":
                new_constitution = int(input(f"What is your new constitution stat? :  "))
                character["stats"]["constitution"] = new_constitution
                print(f"Your constitution has been updated to {character['stats']['constitution']}.")

            elif update_stats == "intelligence":
                new_intelligence = int(input(f"What is your new intelligence stat? :  "))
                character["stats"]["intelligence"] = new_intelligence
                print(f"Your intelligence has been updated to {character['stats']['intelligence']}.")

            elif update_stats == "wisdom":
                new_wisdom = int(input(f"What is your new wisdom stat? :  "))
                character["stats"]["wisdom"] = new_wisdom
                print(f"Your wisdom has been updated to {character['stats']['wisdom']}.")

            elif update_stats == "charisma":
                new_charisma = int(input(f"What is your new charisma stat? :  "))
                character["stats"]["charisma"] = new_charisma
                print(f"Your charisma has been updated to {character['stats']['charisma']}.")

            elif update_stats == "":
                print(f"Invalid input")

            elif update_stats == "back":
                continue

            else:
                print(f"Option not availible.")

        elif edit_menu in view_stats_command:

            print(f"\nYour stats are:  ")
           
            for stat, value in character["stats"].items():
                print(f"{stat.capitalize()}: {value}")

        elif edit_menu in edit_quit_command:
            print(f"Closing Character Editor...")
            return

        else:
            print(f"Invalid input, please try again.")

# === Inventory code === #
def char_inv():

    while True:

        print("\nInventory Options: \n")
        print("1. View Inventory")
        print("2. Add item")
        print("3. Remove Item")
        print("4. Add or Subtract Gold")
        print("5. Quit Inventory Menu")



        inv_menu = input("Please select an option to continue. :  ").strip().lower()

        # -- named list for accessibility -- #
        inv_view_command = ["1", "view inventory", "1. view inventory", "view"]
        inv_add_command = ["2", "add item", "2. add item", "add items", "add"]
        int_remove_command = ["3", "remove items", "3. remove item", "remove item", "remove"]
        inv_gold_command = ["4", "add gold", "subtract gold", "add or subtract gold", "gold", "4. add or subtract gold"]
        inv_quit_command = ["5", "quit", "quit inventory menu", "quit inventory", "exit", "stop", "close", "5. quit inventory menu"]



        if inv_menu in inv_view_command: # use if variable in list name when using named lists

            print(f"\nInventory:")
            gold = character.get("inventory", {}).get("gold", 0)
            items = character.get("inventory", {}).get("items", [])
                                            # .get retreaves the values and allows for you to define what it returns if there is no values in whatever list it is searching

            print(f"\nYou have {gold} gold.")
            if not items:
                print("Your backpack is empty!")
            else:
                print("Welcome to your inventory!")
                print("\n" + "\n".join(f"-{item}" for item in items))
                # This print says line break, plus another line break.  .join customizes an f string to add a hyphen in front of the returned value

        elif inv_menu in inv_add_command:

            print(f"\nAdd to your inventory:")
            items = character.get("inventory", {}).get("items", [])
            
            print("To add items, type them below.")
            print("To return to inventory menu, type 'back'.")

            add_item = input("What would you like to add? :  ").strip().lower()

            if add_item == "":
                print(f"Invalid format")
            elif add_item == "back":
                continue # continue moves to the top of the loop.  Use on subloop menus to allow back and forth within menu
            else:
                character["inventory"]["items"].append(add_item)
                print(f"\n{add_item.capitalize()} has been added to your inventory.")
                print("\n")

        elif inv_menu in int_remove_command:

            print(f"\nRemove from your inventory:")
            items = character.get("inventory", {}).get("items", [])


            print("To remove items, type them below.")
            print("To return to inventory menu, type 'back'.")

            remove_item = input("What would you like to remove? :  ").strip().lower()

            if remove_item == "":
                print(f"Invalid format")
            elif remove_item in items: # Basically says "item is in inventory = true"
                character["inventory"]["items"].remove(remove_item)
                print(f"\n{remove_item.capitalize()} has been removed from your inventory.")
                print("\n")
            elif remove_item == "back":
                continue
            else:
                print("Item does not exist")

        elif inv_menu in inv_gold_command:

            print(f"\nAdd or subtract gold:")
            gold = character["inventory"].get("gold", 0)

            print("Type 'back' to exit gold menu.")
            gold_menu = input(f"Would you like to add or subtract gold? :  ").strip().lower()

            if gold_menu == "add":
                add_gold = int(input("How much gold would you like to add? :  "))
                character["inventory"]["gold"] += add_gold
                print(f"Your new balance is {character['inventory']['gold']}")

            elif gold_menu == "subtract":
                minus_gold = int(input("How much gold would you like to subtract? :  "))
                character["inventory"]["gold"] -= minus_gold
                print(f"Your new balance is {character['inventory']['gold']}")
            
            elif gold_menu == "back":
                continue
            
            else:
                print(f"That option is not available.")

        elif inv_menu in inv_quit_command:
            print("Exiting Inventory...")
            return # In this case, return will take us back to the beginning, but later when other code is implemented, it will take us back to a main menu of sorts
        
        else:
            print("Invalid input.  Try again")


while True:
    create_character()
    action_menu()
    