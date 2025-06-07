names = []


while True:

    # This is a simple, noninteractive menue, it looks weird from the inside but it makes a lot of sence if you think about it
    print(f"What action would you like to complete?")
    print(f"1. Add a name")
    print(f"2. Remove a name")
    print(f"3. View the list")
    print(f"4. Quit")

    menu = input(f"Please type the number coorisponding to your choice. :  ")

    if menu == "1":  # input will never return an integer, allways a string.
        print(f"You selected, 'Add a name'. ")
        name = input(f"What name would you like to add? :  ")
        names.append(name) # .append adds to a list

    elif menu == "2": 
        print(f"You selected 'Remove a name'.")
        name = input(f"What name would you like to remove? :  ")

        if name in names: # This nested if statement checks if the name exists in the list, preventing an error if an input does not exist.
            names.remove(name) # .remove removes from a list
            print(f"{name} has been removed from the list. ")
        else:
            print("That name isn't in the list. ")

    elif menu == "3":
        print(f"You selected 'View the list'.")

        print("\n" .join(names)) 
        # \n adds a clean line break, .join customizes the way strings are joined together.  
        # \n .join makes it to where all strings are seperated by a clean line break.
    

    elif menu == "4":
        print(f"You selected 'Quit'. ")
        print(f"Goodbye! ")

        break # end loop on input "4: Quit"