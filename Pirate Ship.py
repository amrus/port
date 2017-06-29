while True:

    name = input("Enter your name: ")
    print ("%s, you may now start your adventure!! Goodluck " %name)
    start = '''
    You are a female pirate, at a time where men dominate the business.
    You arrived at Oar's Rest Port, hoping to find a ship and crew necessary for your adventure.
    '''

    print (start)

    inst1 = '''
    Your first task is to obtain a ship. You saw two ships at the Port.
    One is a luxurious new ship with all the fancy stuffs and technologies, but is
    heavily guarded. While the other one is an abandoned old but somehow functional ship.
    What do you do?
    '''
    print (inst1)
    print ("Type 'old' to take over the old ship or type 'new' to steal the new ship and risk your life. ")
    user_input = input()
    if user_input == "old":
            oldinst1 = '''
            You are now the captain of the Sisterhood ship. However, you don't have a crew to sail with.
            '''

            print (oldinst1)
            print ("Do you want to recruit a crew? Yes or No? ")
            crew = input()
            if crew == "Yes":
                crew1 = '''
                As you try to recruit your crew, men laugh and objectify you because of your gender.
                Not many women feel encouraged to be pirates.
                Rumor has it that Devil's Cove has lots of trained badass women
                '''
                print (crew1)

                print ("Do you want to sail to Devil's Cove? Yes or No ")
                cove = input()
                if cove == "Yes":
                    cove1= '''
                    You now have a large badass crew
                    What do you want to do now?
                    '''
                    print (cove1)

                    print ("Type 'Treasure' to sail to Treasure Cove or 'Revenge' to sail the sea and take-over ships. ")
                    user_input2 = input()
                    if user_input2 == "Treasure":
                        treasure1 = '''
                        After a long and hard journey, you found lots of treasure chests and gained wealth for life!
                        Congratulations!!
                        '''
                        print (treasure1)
                        print ("Play again? Yes or No ")
                        play2 = input()
                        if play2 == "Yes":
                            "Game Over"
                        if play2 == "No":
                            break
                    if user_input2 == "Revenge":
                        print ("You and your crew became a notorious and highly respected crew within the Pirate organization.")

                        print ("Congratulations!! Girl power prevails!!")

                        print ("Play again? Yes or No")
                        play3 = input()
                        if play3 == "Yes":
                            "Game Over"
                        if play3 == "No":
                            break
                if cove == "No":
                    print ("Sail the sea by yourself and continue to be mocked by men.")
                    print ("Game Over")
            if crew == "No":
                print ("You sail the sea by yourself and face a thunderstorm and die because you can't do everything alone.")
                print ("Game Over")
    if user_input == "new":
            new = '''
            You are heavily wounded after fighting another crew but you manage to still get away.
            You see the coastguard and hear the sirens approaching. What do you do?
            1. Lead a high speed chase?
            2. Jump overboard?
            '''
            print (new)

            action_option = int(input("Enter an Option "))
            if action_option == 1:
                print ("The coastguard catches you because of the chase. They then throw you into a stinky, rat filled cell.")
            elif action_option == 2:
                print ("You unfortunately drown because the current is too strong.")
            print ("The End")
            print ("Play again? Yes or No")
            play4 = input()
            if play4 == "Yes":
                "Game Over"
            if play4 == "No":
                break
