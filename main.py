##
# || Benjamin Leanna || Text Based Game "Baldir's Revenge: A journey through realms ||
##

###
# dictionary created for areas, actions, and items in game
###

areas_text = {1: {'east': '1) Go east to Asgard.',
                  'text': 'You have arrived across space and time to the Bifrost!',
                  'exit': '2) Jump off bridge!'},
              2: {'east': '1) Venture east into Odin/s Throne room',
                  'north': '2) Travel north to the great hall, Valhalla',
                  'south': '3) Head south to the valley of Muspelheim',
                  'west': '4) Head back to the Bifrost bridge.',
                  'item': '5) Search for item....',
                  'text': 'You enter into the great city of Asgard.....in ruins.....',
                  'exit': '6) Give up!'},
              3: {'south': '1) Travel back south to Asgard.',
                  'north': '2) Take the flaming portal north to Hel!',
                  'item': '3) Talk to Odin',
                  'text': 'You see the Valkyries welcome you into Valhalla.',
                  'exit': '4) Give up!'},
              4: {'south': '1) Take the flaming portal back south to Valhalla.',
                  'item': '2) Offer a trade to Fenrir',
                  'text': 'You are transported to the depths of the underword; Welcome to Hel!',
                  'exit': '3) Give up!'},
              5: {'north': '1) Walk north back to Asgard',
                  'west': '2) Climb down west to the Ruins of Vanaheim',
                  'east': '3) Climb up east to the land of giants, Jotunheim.',
                  'item': '4) Plead with Frigg',
                  'text': 'You arrive deep in the mountains of Muspelheim.',
                  'exit': '5) Give up!'},
              6: {'east': '1) Travel back east to Muspelheim',
                  'item': '2) Steal from Loki',
                  'text': 'You enter the ruins of Vanaheim.',
                  'exit': '3) Give up!'},
              7: {'west': '1) Head back down the mountain to Muspelheim',
                  'north': '2) Take the secret passage north to the Kingdom of the Dwarves',
                  'item': '3) Unclasp the dead giants hand',
                  'text': 'You arrive in a harsh blizzard in the home of the frost giants, Jotunheim.',
                  'exit': '4) Give up!'},
              8: {'south': '1) Take the passage back down to Jotunheim',
                  'west': '2) Leap out into the void',
                  'item': '3) Ask the dwarves to relight the forge!!',
                  'text': 'Through a secret path you stumble upon the Dwarven Kingdom!',
                  'exit': '4) Give up!'},
              9: {'name': 'Odin/s Throne Room', 'boss': 'Tyr'}
              }
#####################################################################################
##                      Legend for quick reference                                 ##
#####################################################################################
## Area Key:                 ## Item Key:             ## Direction Key:            ##
## 1: Bifrost                ## NONE                  ## East                      ##
## 2: Asgard                 ## Map of the city       ## West, North, South, East  ##
## 3: Valhalla               ## Odin's Right eye      ## North, South              ##
## 4: Hel                    ## Fenrir's Claw Shield  ## South                     ##
## 5: Muspelheim             ## Frigg's Potion        ## West, North, East         ##
## 6: Ruins of Vanaheim      ## Loki's Knowledge      ## East                      ##
## 7: Jotunheim              ## Dwarven Compass       ## West, North               ##
## 8: Kingdom of the Dwarves ## Mjollnir              ## South, West               ##
## 9: Odin's Throne Room     ## NONE                  ## NONE                      ##
#####################################################################################
## print(areas[7]['text']) ... example: prints Jotunheim's text from dictionary
###
# list created to store items collected throughout game.
###
inventory_list = []
# inventory_list.append(areas[2]['item']) ... example to add item from Asgard to Inventory List
###
# option variables defined from area_text dictionary.
###
bifrost_options = '{}\n{}'.format(areas_text[1]['east'], areas_text[1]['exit'])
asgard_options = '{}\n{}\n{}\n{}\n{}\n{}'.format(areas_text[2]['east'], areas_text[2]['north'], areas_text[2]['south'],
                                                 areas_text[2]['west'], areas_text[2]['item'], areas_text[2]['exit'], )
valhalla_options = '{}\n{}\n{}\n{}'.format(areas_text[3]['south'], areas_text[3]['north'], areas_text[3]['item'],
                                           areas_text[3]['exit'])
hel_options = '{}\n{}\n{}'.format(areas_text[4]['south'], areas_text[4]['item'], areas_text[4]['exit'])
muspelheim_options = '{}\n{}\n{}\n{}\n{}'.format(areas_text[5]['north'], areas_text[5]['west'], areas_text[5]['east'],
                                                 areas_text[5]['item'], areas_text[5]['exit'])
vanaheim_options = '{}\n{}\n{}'.format(areas_text[6]['east'], areas_text[6]['item'], areas_text[6]['exit'])
jotunheim_options = '{}\n{}\n{}\n{}'.format(areas_text[7]['west'], areas_text[7]['north'], areas_text[7]['item'],
                                            areas_text[7]['exit'])
kingdom_options = '{}\n{}\n{}\n{}'.format(areas_text[8]['south'], areas_text[8]['west'], areas_text[8]['item'],
                                         areas_text[8]['exit'])


##
# Defining function for error if user inputs something not in choices (numbers only) if
# a number is not entered it will check for that in each menu's funtion and report error
# and make them choose again
##
def error():
    print('That is an invalid choice! \nPlease select a choice from the menu!')


##
# Making Dictionary for death if user inputs choice that kills them!
##
deaths = {
    1: 'You jump off the bridge and become lost in the void forever!\n\n GAME OVER!',
    2: 'You try to use the path back south again but slip off the edge and fall to your death!\n\n GAME OVER!',
    3: 'You/ve arrived in Hel and stand face to face with the mighty Fenrir.\n'
       'It seems you have nothing to offer him and he attacks you!\n'
       'With nothing to defend yourself, Fenrir tears you apart, limb from limb!\n\n GAME OVER!',
    4: 'You have chosen to give up..... like a coward!\n\n GAME OVER!'
}


##
# Defining menus for each area
##
def bifrost_menu():
    print(inventory_list)
    print(areas_text[1]['text'])
    print(bifrost_options)
    print('Enter a number to pick your choice >> ')
    user_i = input()
    if user_i.isdigit() != True:  # if input is not a digit, ex: str - then will be promted to try again
        print('That is not a number from the list, try again!')
        return bifrost_menu()
    user_i = int(user_i)  # after checking if its a digit entered, convert the user_i to an int so you can use in loop
    while (user_i > 0) and (user_i < 3):
        if user_i == 1:
            return asgard_menu()
        elif user_i == 2:
            print(deaths[1])
            quit()
        elif (user_i <= 0) or (user_i >= 2):
            return error(), bifrost_menu()


def asgard_menu():
    print(inventory_list)
    print(areas_text[2]['text'])
    print(asgard_options)
    print('Enter a number to pick your choice >> ')
    user_i = input()
    if user_i.isdigit() != True:  # if input is not a digit, ex: str - then will be promted to try again
        print('That is not a number from the list, try again!')
        return asgard_menu()
    user_i = int(user_i)  # after checking if its a digit entered, convert the user_i to an int so you can use in loop
    while (user_i > 0) and (user_i < 7):
        if user_i == 1:
            return throne_menu()
        elif user_i == 2:
            return valhalla_menu()
        elif user_i == 3:
            return muspelheim_menu()
        elif user_i == 4:
            return bifrost_menu()
        elif user_i == 5:
            if 'Map of the city' not in inventory_list:
                inventory_list.append('Map of the city')
                return print('You dig through the rubble and find a small box.\n'
                             'Upon opening the box you fight the Map of the city and it is'
                             ' added to your inventory!'), asgard_menu()
            else:
                return print('You already scourged the city and have obtained this item!'), asgard_menu()
        elif user_i == 6:
            print(deaths[4])
            quit()
        elif (user_i <= 0) or (user_i >= 6):
            return error(), asgard_menu()


def valhalla_menu():
    print(inventory_list)
    print(areas_text[3]['text'])
    print(valhalla_options)
    print('Enter a number to pick your choice >> ')
    user_i = input()  # if input is not a digit, ex: str - then will be promted to try again
    if user_i.isdigit() != True:
        print('That is not a number from the list, try again!')
        return valhalla_menu()
    user_i = int(user_i)  # after checking if its a digit entered, convert the user_i to an int so you can use in loop
    while (user_i > 0) and (user_i < 5):
        if user_i == 1:
            return asgard_menu()
        elif user_i == 2:
            return hel_menu()
        elif user_i == 3:
            if 'Odin/s Right Eye' not in inventory_list:
                inventory_list.append('Odin/s Right Eye')
                return print('You explain the quest you/re on to avenge him and save his beloved city.....'
                             '\nOdin sees greatness in you and proceeds to remove his one eye left to help'
                             ' guide you along your venture!\n'
                             'Odin/s Right Eye is added to your inventory!'), valhalla_menu()
            else:
                return print('Odin tells you to seek out his wife, Frigg. Perhaps she has something for you that will'
                             ' help you along the way!'), valhalla_menu()
        elif user_i == 4:
            print(deaths[4])
            quit()
        elif (user_i <= 0) or (user_i >= 4):
            return error(), valhalla_menu()


def hel_menu():
    print(inventory_list)
    # Checking to see if you've been to muspelheim first to get frigg's potion and that
    # it is in your inventory. If not, the dog kills you.
    if 'Frigg/s Potion' not in inventory_list:
        print(deaths[3])
        quit()
    print('Enter a number to pick your choice >> ')
    print(areas_text[4]['text'])
    print(hel_options)
    user_i = input()  # if input is not a digit, ex: str - then will be promted to try again
    if user_i.isdigit() != True:
        print('That is not a number from the list, try again!')
        return hel_menu()
    user_i = int(user_i)  # after checking if its a digit entered, convert the user_i to an int so you can use in loop
    while (user_i > 0) and (user_i < 5):
        if user_i == 1:
            return valhalla_menu()
        elif user_i == 2:
            if 'Fenrir/s Claw Shield' not in inventory_list:
                inventory_list.append('Fenrir/s Claw Shield')
                return print('You hold up Frigg/s Potion and Fenrir/s eye begin to glisten.\n'
                             'She knows what you hold will free her from this damnation of guarding Hel for'
                             ' eternity and allow him to be able to see her family again!\n'
                             'She bites off her left paw and hands it over in exchange of the potion. '
                             'You fasted the paw and bone into a mighty shield. \n'
                             'Fenrir/s Claw Shield is added to your inventory!'), hel_menu()
            else:
                return print('Fenrir has left this place. There is nothing more to collect.'), hel_menu()
        elif user_i == 4:
            print(deaths[4])
            quit()
        elif (user_i <= 0) or (user_i >= 4):
            return error(), hel_menu()


def muspelheim_menu():
    print(inventory_list)
    print(areas_text[5]['text'])
    print(muspelheim_options)
    print('Enter a number to pick your choice >> ')
    user_i = input()  # if input is not a digit, ex: str - then will be promted to try again
    if user_i.isdigit() != True:
        print('That is not a number from the list, try again!')
        return muspelheim_menu()
    user_i = int(user_i)  # after checking if its a digit entered, convert the user_i to an int so you can use in loop
    while (user_i > 0) and (user_i < 6):
        if user_i == 1:
            return asgard_menu()
        elif user_i == 2:
            return vanaheim_menu()
        elif user_i == 3:
            return jotunheim_menu()
        elif user_i == 4:
            if 'Frigg/s Potion' not in inventory_list:
                inventory_list.append('Frigg/s Potion')
                return print('You sit down with Frigg. She is in distress on what has happened to her husband and \n'
                             'everyone else in their wonderful city. You plead with her for help to help you along \n'
                             'in your quest. Using her magic, she brews a special potion that can allow anyone or \n'
                             'anything out of the depth of Hel.\n'
                             'Frigg/s Potion is added to your inventory!'), muspelheim_menu()
            else:
                return print('Frigg urges you to explore for others that may have some truth and guidence. \n'
                             'Take her potion and use if wisely!'), muspelheim_menu()
        elif user_i == 5:
            print(deaths[4])
            quit()
        elif (user_i <= 0) or (user_i >= 5):
            return error(), muspelheim_menu()


def vanaheim_menu():
    print(inventory_list)
    print('Enter a number to pick your choice >> ')
    print(areas_text[6]['text'])
    print(vanaheim_options)
    user_i = input()  # if input is not a digit, ex: str - then will be promted to try again
    if user_i.isdigit() != True:
        print('That is not a number from the list, try again!')
        return vanaheim_menu()
    user_i = int(user_i)  # after checking if its a digit entered, convert the user_i to an int so you can use in loop
    while (user_i > 0) and (user_i < 5):
        if user_i == 1:
            return muspelheim_menu()
        elif user_i == 2:
            if 'Loki/s Knowledge' not in inventory_list:
                inventory_list.append('Loki/s Knowledge')
                return print('As you come upon the beach in the Ruins of Vanaheim, a shadow figure lies on the beach.\n'
                             ' As you approach the man, you notice that it is none other than the brother of Thor,'
                             ' Loki! \nAs you are now over top of him looking down, you see a small book next to him.'
                             ' You pick up the book and it speaks into your mind. \nYou know why you are here now! '
                             'You know why it is you that must stop all of this..... for you are Baldir, first '
                             'born of Odin and rightful heir to the throne. \nWith this knowledge you know you are '
                             'worthy of wielding a might weapon that can defeat Tyr!\n'
                             'Loki/s Knowledge is added to your inventory!'), vanaheim_menu()
            else:
                return print('Quickly, before Loki notices, you need to leave!!!'), vanaheim_menu()
        elif user_i == 3:
            print(deaths[4])
            quit()
        elif (user_i <= 0) or (user_i >= 3):
            return error(), vanaheim_menu()


def jotunheim_menu():
    print(inventory_list)
    # Checking to see if you've been to vallhala first to get odin's eye and that
    # it is in your inventory. If not, you cannot enter and have to turn back.
    if 'Odin/s Right Eye' not in inventory_list:
        print('The snowy blizzard up the mountain into Jotunheim is too much for you bear.\n'
              'You turn around before you lose your way and head back to the Muspelheim valley.')
        return muspelheim_menu()
    print('Enter a number to pick your choice >> ')
    print(areas_text[7]['text'])
    print(jotunheim_options)
    user_i = input()  # if input is not a digit, ex: str - then will be promted to try again
    if user_i.isdigit() != True:
        print('That is not a number from the list, try again!')
        return hel_menu()
    user_i = int(user_i)  # after checking if its a digit entered, convert the user_i to an int so you can use in loop
    while (user_i > 0) and (user_i < 5):
        if user_i == 1:
            return muspelheim_menu()
        if user_i == 2:
            if 'Dwarven Compass' not in inventory_list:
                print('You are unable to find your way to passage. Perhaps there is an item you need?')
                return jotunheim_menu()
            else:
                print('With the inner sight that Odin/s Right Eye gives you, you can use the Dwarven Compass to find'
                      ' your way to a secret passage.')
                return kingdom_menu()
        elif user_i == 3:
            if 'Dwarven Compass' not in inventory_list:
                inventory_list.append('Dwarven Compass')
                return print('Amongst the snow drifts you see a fallen giant.\n'
                             'His hand is clasped shut but you can see he is holding onto something!\n'
                             'You pry his hand open to find the Dwarven Compass!!\n'
                             'Dwarven Compass is added to your inventory!'), jotunheim_menu()
            else:
                return print('You have the compass. Along with Odin/s eye you will be able to use it'), jotunheim_menu()
        elif user_i == 4:
            print(deaths[4])
            quit()
        elif (user_i <= 0) or (user_i >= 4):
            return error(), jotunheim_menu()


def kingdom_menu():
    print(inventory_list)
    print(areas_text[8]['text'])
    print(kingdom_options)
    print('Enter a number to pick your choice >> ')
    user_i = input()  # if input is not a digit, ex: str - then will be promted to try again
    if user_i.isdigit() != True:
        print('That is not a number from the list, try again!')
        return kingdom_menu()
    user_i = int(user_i)  # after checking if its a digit entered, convert the user_i to an int so you can use in loop
    while (user_i > 0) and (user_i < 6):
        if user_i == 1:
            print(deaths[2])
            quit()
        elif user_i == 2:
            print('Falling into the void you enter a wormhole! You are transported safely back to the Bifrost!')
            return bifrost_menu()
        elif user_i == 3:
            if 'Mjollnir' not in inventory_list:
                inventory_list.append('Mjollnir')
                return print('The dwarves greet you with tired hands. \nAs their forge heats up with the power from'
                             ' a dying star, mythical metal is poured into a cast. When it cools off they hand'
                             ' you a hammer fit for a god!\n'
                             'Mjollnir is added to your inventory!!'), kingdom_menu()
            else:
                return print('There is no time to waste! You must hurry to the Throne room and battle'
                             ' Tyr!'), kingdom_menu()
        elif user_i == 5:
            print(deaths[4])
            quit()
        elif (user_i <= 0) or (user_i >= 5):
            return error(), kingdom_menu()

def throne_menu():
    if len(inventory_list) == 6:
        print('You enter Odin/s Throne room where Tyr is sitting on the Throne.\n'
              'You charge at him with Mjollnir equipped in your left hand and Fenrir/s Claw Shield attached to your'
              'right.\n'
              'You battle fiercely but overcome and defeat him!\n'
              'Congradulations, you have won the game!!!!')
        quit()
    else:
        print('As you enter Odin/s Trone room where Tyr sits upon the throne, you feel unprepared!\n'
              'Tyr sees this as he charges you! With one swift hit he pummels you to death!\n\n'
              'GAME OVER')
        quit()


print(
    'You emerge into a strange area with no memory of who you are.\nThere/s a voice from behind you that tells you his'
    ' name is Heimdall. He tells you that Thor/s brother Tyr has gone mad and taken over the throne in Asgard city.\n'
    'He urges you to fufil your destiny and save the Aesir city, but before he can answer you on who you are he is '
    'warped away from you to an unknown place!\nThis is where your jouney begins!')

bifrost_menu()