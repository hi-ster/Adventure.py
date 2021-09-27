import pyfiglet

#Vars and shit

logo = pyfiglet.print_figlet("Adventure.py", colors='GREEN')
intro = "Welcome to adventure.py! In this game you will explore a series of dungeons and slay some monsters."
ready = "Are you ready? Y/N?"
ans_y = ["Yes", "Y", "yes", "y"]
ans_n = ["No", "N", "no", "n"]
ans_1 = "1"
ans_2 = "2"
ans_3 = "3"
ans_quit = ["Quit, quit, Q, q"]
ans_quit = quit
#Stats
wep = "Sword"
hp = 100
lvl = 1
gold = 0

#def stats():
#int hp = 100
#weapon = "Sword"
print("Made by Steven!")
#Game Code Starts here
print(intro)
print("Stats: Level:", lvl, ", Health:", hp, ", Weapon:", wep, ", Gold: ", gold )
print(ready)

start = input(">>")

if start in ans_y:
    print("You awake in a dark cave. You are unsure of how you got here")
    print("There is light ahead. Will you go towards it? Y/N?")

    go_to_light = input(">>")

    if go_to_light in ans_y:
        print("You head towards the light. You emerge from the cave to be greeted by a sea of trees.")
        print("You notice a path towards your right. Will you go towards it? Y/N?")

        #Go to Path?
        path_y_or_n = input(">>")

        if path_y_or_n in ans_y:
            print("You head towards the path. As you get closer you notice the path goes off in two directions.")
            print("Will you go Right (1) or Left (2)?")

            #@ path, right or left?
            path_r_or_l = input(">>")
            if path_r_or_l in ans_1:
                print("You take the path right.")
                print("After walking for a while, you stumble upon a Goblin camp.")
                print("You have a look around and find a lone goblin, but it doesn't notice you.")
                print("Will you fight the goblin? Y/N?")

                #Fight Goblin?
                fight_lone_goblin = input(">>")

                if fight_lone_goblin in ans_y:
                    print("You launch a suprise attack on the goblin dealing a critical blow.")
                    print("You Leveled up!")
                    print("Level: ", lvl + 1, ", Health: ", hp + 10)
                    print("You gained 10 Gold!")
                    print("Gold: ", gold + 10)
                    print("you contiue down the path until you reach a small town.")
                    print("Upon entering the town you notice a merchants hut. Will you go see what they have? Y/N?")
                    #Level 2 wiv cash
                    town_lvl2_to_merch = input(">>")

                    if town_lvl2_to_merch in ans_y:
                        print("You enter the merchants shop.")
                        print("Merchant: Greeting traveller! We don't get many vistors as of recent with all the goblin activity around here.")
                        print("Merchant: Anyway, what can I do you for?")
                        print("You notice a steel axe sat on the counter.")
                        print("Merchant: Oh I see you've taken an interest into this axe of mine here. Tell you what...")
                        print("Merchant: I will do a special deal for you, if you promise to go sort out our goblin problem.")
                        print("Merchant: I'm thinking, hmm...?")
                        print("Merchant: 10 gold?")
                        print("How convientent!? Thats exactly how much you have. Will you pay it? Y/N?")

                        #Obtain Axe
                        get_axe = input(">>")

                        if get_axe in ans_y:
                            print("You acquire the axe!", "Gold: ", gold)
                            print("Merchant: Thankyou very much! I hope it serves you well. Hey, why not go speak with the mayor of this town? He has a quest for an adventurer like you.")
                            print("You leave the merchants hut with a new shiny axe. You decide to go to the mayor in search of quest.")
                            print("You head towards a large building in the middle of town.")
                            print("Guard: Halt! What business do you have with the mayor?")
                            print("You explain that you are here to help with the towns goblin problem.")
                            print("The guards let you in.")
                            print("Mayor: So, you're the adventurer thats just arrived here I take it? I have a special quest only someone like you can handle.")
                            print("Mayor: It involves our goblin problem. I need you to go and kill the goblin lord. He's not too far frome here.")
                            print("Mayor: So what do you say?")
                            print("Will you Accept this quest? Y/N?")

                            with_axe = input(">>")

                            if with_axe in ans_y:
                                print("With axe in hand, you eagarly accept this quest.")

                            elif with_axe in ans_n:
                                print("You Decline the Quest and head home. At least you got this cool axe! Guess you can become a lumberjack....")
                                pyfiglet.print_figlet("Game Over", colors="RED")


                            #To add:
                            # - Mayor convo for both lvl 1 and lvl 2 adventurer
                            # - Goblin Fights 1 & 2 w/ rand health item drop and rand dmg taken between 5 and 35
                            # - Impliment Goblin Lord fight w/ rand dmg taken, between 15 and 50, critical of 100? Maybe?
                            # - Add fleeing from quest resulting in death

                        elif get_axe in ans_n:
                            print("You leave the merchants store, with no axe.")
                            print("You notice a big building and head towards it.")
                            print("Guard: Halt traveler! What is your business here?")
                            print("You explain that you are here to help with the towns goblin problem.")
                            print("The guards let you in.")
                            print("Mayor: So, you're the adventurer thats just arrived here I take it? I have a special quest only someone like you can handle.")
                            print("Mayor: It involves our goblin problem. I need you to go and kill the goblin lord. He's not too far frome here.")
                            print("Mayor: So what do you say?")
                            print("Will you Accept this quest? Y/N?")
                            
                            with_no_axe_lvl2 = input(">>")

                            if with_no_axe_lvl2 in ans_y:
                                print("With axe in hand, you eagarly accept this quest.")

                            elif with_no_axe_lvl2 in ans_n:
                                    print("You Decline the Quest and head home. Your days as an adventurer are over. You wern't cut out for it after all.")
                                    pyfiglet.print_figlet("Game Over", colors="RED")


                elif fight_lone_goblin in ans_n:
                    print("You sneak past the goblin and continue down the path until you reach a small town.")
                    print("Upon entering the town you notice a merchants hut. Will you go see what they have? Y/N")

                    #Get to town no cash
                    town_lvl1_to_merch = input(">>")

                    if town_lvl1_to_merch in ans_y:
                        print("You enter the merchants shop.")
                        print("Merchant: Howdy! What can I do you for?")
                        print("Would you like to buy anything? Y/N?")
                        
                        broke_ass = input(">>)")

                        if broke_ass in ans_y:
                            print("Merchant: Hey! you have no gold!")
                            print("It goes against your morals, but you have the choice. Will you steal from the merchant? Y/N?")

                            broke_ass_steals = input(">>")
                            if broke_ass_steals in ans_y:
                                print("You reach for a shiny axe resting on the merchants counter.")
                                print("Suddenly, you hear a loud BONK! and everything turns black....")
                                print("You awaken in a prison cell...")
                                print("Your execution will be in a few days. Just remember.... Heros don't steal.")
                                pyfiglet.print_figlet("Game Over", colors="RED")

                            elif broke_ass_steals in ans_n:
                                print("You leave the merchants store.")
                                print("You notice a big building and head towards it.")
                                print("Guard: Halt traveler! What is your business here?")
                                print("You explain that you are here in town looking for work.")
                                print("The guards let you in.")
                                print("Mayor: So, you're an adventurer right? Thats just what we need to deal with our current problem.")
                                print("Mayor: Our problem involves goblins. I need you to go and kill the goblin lord. He's not too far frome here.")
                                print("Mayor: So what do you say, are you up to this challenge?")
                                print("Will you Accept this quest? Y/N?")

                                #Brokeass Dont Steal Quest: This route is guarenteed death as only level 1 lol
                                BADS_Quest = input(">>")

                                if BADS_Quest in ans_y:
                                    print("You accept the Quest!")
                                    print("You head north in search of the goblin lord.")

                                elif BADS_Quest in ans_n:
                                    print("You Decline the Quest and head home. Your days as an adventurer are over. You wern't cut out for it after all.")
                                    pyfiglet.print_figlet("Game Over", colors="RED")

                        elif broke_ass in ans_n:
                            print("You leave the merchants store.")
                            print("You notice a big building and head towards it.")
                            print("Guard: Halt traveler! What is your business here?")
                            print("You explain that you are here in town looking for work.")
                            print("The guards let you in.")
                            print("Mayor: So, you're an adventurer right? Thats just what we need to deal with our current problem.")
                            print("Mayor: Our problem involves goblins. I need you to go and kill the goblin lord. He's not too far frome here.")
                            print("Mayor: So what do you say, are you up to this challenge?")
                            print("Will you Accept this quest? Y/N?")

                    elif town_lvl1_to_merch in ans_n:
                        print("You decide to head to the Mayor of this town to see if there is any work to be done.")
                        print("Guard: Halt traveler! What is your business here?")
                        print("You explain that you are here in town looking for work.")
                        print("The guards let you in.")
                        print("Mayor: So, you're an adventurer right? Thats just what we need to deal with our current problem.")
                        print("Mayor: Our problem involves goblins. I need you to go and kill the goblin lord. He's not too far frome here.")
                        print("Mayor: So what do you say, are you up to this challenge?")
                        print("Will you Accept this quest? Y/N?")

            elif path_r_or_l in ans_2:
                print("You decide to follow the path left. On this path you hear strange noises, but continue on unbothered.")
                print("As you follow the path, you stumble upon a Trolls den.")
                print("You decide that you will go into the den and fight the troll, for you are a brave adventurer.")
                print("Unsuprisingly, you are no match for the troll.")
                print("And this is where your adventure ends...")
                pyfiglet.print_figlet("Game Over", colors="RED")


        elif path_y_or_n in ans_n:
            print("You decide not to follow the path and run off, deeper into the woods. You stumble upon a Trolls den. Loud noises can be heard from inside.")
            print("Will yo go inside? Y/N?")

            #Troll Den
            troll_den_y_or_n = input(">>")

            if troll_den_y_or_n in ans_y:
                print("You enter the trolls den. To your suprise a troll is standing infront of you, giving you a meanacing glare.")
                print("Will you fight the troll? Fight (1) or Run (2)?")
                
                #Troll Fight
                troll_fight = input(">>")

                if troll_fight in ans_1:
                    print("you attempt to fight the troll. This does not end well...")
                    pyfiglet.print_figlet("Game Over", colors="RED")
                elif troll_fight in ans_2:
                    print("You panic and run away as fast as you can.")
                    print("You run for a few moments, but are caught off guard by a pack of wolves.")
                    print("You panic and reach for your Sword, However, by some devine bad luck its not there!")
                    print("Unable to defend yourself you fall to the wolves, and this is how your adventure ends...")
                    pyfiglet.print_figlet("Game Over", colors="RED")

            elif troll_den_y_or_n in ans_n:
                    print("You panic and run away as fast as you can.")
                    print("You run for a few moments, but are caught off guard by a pack of wolves.")
                    print("You panic and reach for your Sword, However, by some devine bad luck its not there!")
                    print("Unable to defend yourself you fall to the wolves, and this is how your adventure ends...")
                    pyfiglet.print_figlet("Game Over", colors="RED")
    elif go_to_light in ans_n:
        print("You decide not to leave the cave. You just sit there.")
        print("You have ascended... For you have beaten the game by not playing.")
        pyfiglet.print_figlet("You Win!", colors="GREEN")       

#Quit
elif start in ans_n:
    quit