counter=0
import time
import sys
import random

def write(s):
    # create the type writer effect using delay when printing each letters
    for i in s:
        print(i, end="", flush=True)
        time.sleep(.01)
    print()
    

class player:
    # give the player attribute, name and health that can be accessed anywhere in the code
  def __init__(self, name, health):
    self.name = name
    self.health = health

    
def attack_range():
    # return the minimum and maximum values when the player attacks
    greenItems = ["sword", "potion", "mushroom"]
    numGreen = 0
    for i in bag:
        if i.lower() in greenItems:
            numGreen+=1
            # check how many items the player has are green
    if numGreen> 2:
        return 20,30
    elif numGreen>1:
        return 15,25
    elif numGreen>0:
        return 10,20
    else:
        return 1,10

def playerGrade():
    global counter
    if counter < 25:
        return " A"
    elif counter <30:
        return " B"
    elif counter <35:
        return " C"
    else:
        return " D"
        
#  print once
def start():
# the instructions of the game
    global counter                                              
    global p1
    counter=0 
    lcounter=0 #counts how many times the player input incorrectly
    write('[ALL INPUTS SHOULD NOT INCLUDE "A", "AN", OR "THE"]')
    print()
    write("-------Welcome to Cavalier-------")
    x = input("What should we call you?\n")
    
    p1 = player(x,50)
    print("Welcome", p1.name)
    write("You are playing as a young knight, navigating through an expansive and\ndangerous dungeon to save a princess. \nYour skills, wits, and determination will be tested in this exciting\nfirst-person action-adventure game.")
    print()
    write("You have made your way to the dungeon where the princess is held.\nYou feel a dark aura surrounding the place, and you are told a mighty\ndragon is guarding the princess.")
    print()
    write("Instructions:")
    write("You will navigate your way through the house, collect magical items and defeat the tyrannical dragon. \nYou can only hold three items at a time.")
    print()
    write("Here are some basic commands in your toolbox:")
    write("(walk forward, open door, check items)")
    print()
    write("Pay close attention to the clues and narration.\nRemember to use common sense. It is your greatest ally!")
    print("----------------------------------------")
    printHouse()
    while True:
        counter+=1
        if lcounter>2: #if more than 3 consecutive tries we will give hints
            write("Try going forward and opening the door")
        x=input()
        if x=="look around":
            write("You are standing at the front gate of the house. The sides are all barred.")
            print("----------------------------------------")
        elif x=="walk forward" or x=="go forward" or x=="go to door":
            write("You have arrived at the door")
            openDoor(False)
            print("----------------------------------------")
        elif x == "open door":
            openDoor(True)
            print("----------------------------------------")
            return
        elif x == "check items":
            print('You have (', ', '.join(bag), ') in bag now.')
        else:
            write("Try Again")
            lcounter+=1
            
def corridor():
# The function for the corridor
    write("You enter the main corridor, stunned by it’s rusty nature, you slowly\nwalk on top of the rugged carpet.\nIt made a suspiciously loud squeak as you proceeded forward.")
    write("There are three doorways for you to choose:\nthe kitchen on the left, the living room in front and the bedroom on the right.")

def livingRoom():
# The function for the living room
    global counter,items
    lcounter=0 #counts how many times the player input incorrectly
    write("You are in the living room")
    write("This is the largest room on this floor. You switched on the lights and\nfound a sofa on one side and a TV across from it.")
    while True:
        counter+=1
        if counter>45:
            write("\t\t\tYOU TOOK TOO MANY MOVES")
            write("\t\t\t   YOU ARE DEAD")
            sys.exit()
        print()
        if lcounter > 2:
            write("Try (go to sofa) or (go to tv) or (leave living room)")
            print("-----------------------------")
        x = input()

        if x.lower() == "go to sofa":
            items = ['gloves','sword']
            write("You were reluctant to sit on the sofa. You found a pair of gloves!\nThe sofa has a weird reflection towards your eye, you try to grab it,\nand it creates a small cut on your hand.\nYou have found a sword!\nYou can ( take ***, drop ***, check items, leave sofa ).")
            while True:
                counter += 1
                x=input()
                ins = x.split()
                while 'take' in ins or 'drop' in ins or 'check' in ins:
                    check(x)
                    x = input()
                    ins = x.split()
                    # if 'take' not in ins and 'drop' not in ins and 'check' not in ins and x != 'leave sofa' and x!='leave':
                    #         write("Try Again")
                    #         continue
                if x == 'leave sofa' or x == 'leave':
                    write('You can (go to sofa) or (go to tv) or (leave living room) now.')
                    break
                else:
                    write("Try Again")

        elif x.lower() == "go to tv":
            items = ['painting','lighter']
            write("There is an ancient painting on the wall.\nBehind the TV you found a lighter.\nYou can ( take ***, drop ***, check items, leave table ).")
            while True:
                counter += 1
                x=input()
                ins = x.split()
                
                while 'take' in ins or 'drop' in ins or 'check' in ins:
                    if x != "take lighter":
                        check(x)
                    else: 
                        write("The Lighter Exploded!!")
                        write("You lose 10 HP")
                        p1.health-=10
                    if p1.health < 0:
                        write("\t\t\tYOU ARE DEAD!!")
                        write("\t\t\t  GAME OVER")
                        sys.exit()
                    x = input()
                    ins = x.split()
                    # if 'take' not in ins and 'drop' not in ins and 'check' not in ins and x != 'leave tv' and x!='leave':
                    #         write("Try Again")
                if x == 'leave tv' or x == "leave":
                    write('You can (go to sofa) or (go to tv) or (leave living room) now.')
                    break
                else:
                    write("Try Again")
                
        elif x.lower() == "leave living room" or x.lower() == "leave room" or x.lower() == "leave":
            write("back to corridor from living room")
            break
        elif x.lower() == "check items":
            print('You have (', ', '.join(bag), ') in bag now.')
        
        else:
            lcounter+=1
            write("Try Again")
        
    corridor()
        

def kitchen():
# The function of kitchen
    global counter,items
    lcounter = 0 #counts how many times the player input incorrectly
    write("You have entered what appears to be a kitchen. There are no windows and is a dead end.\nThere is a table in the middle of the room and a kitchen counter next to the wall.")
    
    while True:
        print()
        x = input()
        counter += 1
        if counter > 35:
            write("\t\t\tYOU TOOK TOO MANY MOVES")
            write("\t\t\t   YOU ARE DEAD")
            sys.exit()
        
        if lcounter > 2: #if more than 3 consecutive tries we will give hints
            write("Try (go to table) or (go to kitchen counter) or (leave kitchen).")
            print("-----------------------------")
        
        if x.lower() == "go to table":
            lcounter=0
            items = ['apple', 'knife']
            write("You walked slowly towards the table, you found an apple and a knife lying there.\nYou can ( take ***, drop ***, check items, leave table ).")
            while True:
                counter += 1
                x = input()
                ins = x.split()
                if x == "take apple":
                        write("\t\t\tTHE APPLE WAS POISONOUS!!")
                        write("\t\t\t\tYOU ARE DEAD")
                        write("\t\t\t\t GAME OVER")
                        sys.exit()
                while 'take' in ins or 'drop' in ins or 'check' in ins:
                    check(x)
                    x = input()
                    ins = x.split()
                    # if 'take' not in ins and 'drop' not in ins and 'check' not in ins:
                    #     if x!="leave table" or x!="leave":
                    #         write("Try Again")
                if x == 'leave table' or x == "leave":
                    write('You can (go to kitchen counter) or (leave kitchen) or (go to table) now.')
                    break
                else:
                    write('Try again')
        
        elif x.lower() == "go to kitchen counter" or x.lower() == "go to counter":
            lcounter=0
            items = ['potion']
            write(
                "You looked around the rundown space and signed. But your hand manages to grab onto a potion. You can ( take ***, drop ***, check items, leave kitchen counter ).")
            while True:
                counter += 1
                x = input()
                ins = x.split()
                while 'take' in ins or 'drop' in ins or 'check' in ins:
                    check(x)
                    x = input()
                    ins = x.split()
                    # if 'take' not in ins and 'drop' not in ins and 'check' not in ins and x!= 'leave kitchen counter' and x!='leave':
                    #     write("Try Again")
                if x == 'leave kitchen counter' or x == "leave":
                    write('You can (go to kitchen counter) or (leave kitchen) or (go to table) now.')
                    break
                else:
                    write("Try Again")
        
        elif x.lower() == "leave kitchen" or x == "leave room" or x == "leave":
            write("back to corridor from kitchen")
            break
        
        elif x.lower() == "check items":
            print('You have (', ', '.join(bag), ') in bag now.')
        
        else:
            lcounter += 1
            write("Try Again")
        
    corridor()


def bedroom():
# The function for the bedroom
    global counter,items
    lcounter = 0 #counts how many times the player input incorrectly
    write("You are in the bedroom")
    write("There is a bed in one corner, and an old TV at another.")
    while True:
        counter +=1
        if counter > 35:
            write("\t\t\tYOU TOOK TOO MANY MOVES")
            write("\t\t\t   YOU ARE DEAD")
            sys.exit()
        print()
        
        if lcounter>2:  #if more than 3 consecutive tries we will give hints
            write("Try (go to bed) or (go to tv) or (leave bedroom).")
            print("-----------------------------")
        
        x=input()

        if x.lower() == "go to bed":
            items=['mushroom']
            write("As disgusting as it is, you lift up the blankets and found a glowing magic mushroom.\nYou can ( take ***, drop ***, check items, leave bed ).")
            while True:
                counter += 1
                x = input()
                ins = x.split()
                while 'take' in ins or 'drop' in ins or 'check' in ins:
                    check(x)
                    x = input()
                    ins = x.split()
                    # if 'take' not in ins and 'drop' not in ins and 'check' not in ins and x!= 'leave bed' and x!='leave':
                    #     write("Try Again")
                
                if x == 'leave bed' or x == 'leave':
                    print('You can (go to tv) or (leave bedroom) or (go to bed) now.')
                    break
                else:
                    write("Try Again")

        elif x.lower() == "go to tv":
            write("You found a set of batteries.")
            items=['batteries']
            while True:
                counter += 1
                x = input()
                ins = x.split()
                while 'take' in ins or 'drop' in ins or 'check' in ins:
                    check(x)
                    x = input()
                    ins = x.split()
                    # if 'take' not in ins and 'drop' not in ins and 'check' not in ins and x!= 'leave tv':
                    #     write("Try Again")
                if x == 'leave tv' or x == 'leave':
                    print('You can (go to bed) or (go to tv) or (leave bedroom) now.')
                    break
                else:
                    write("Try Again")
        
        elif x.lower() == "leave bedroom" or x == 'leave room' or x == "leave":
            write("back to corridor from bedroom")
            break
        
        elif x.lower() == "check items":
            print('You have (', ', '.join(bag), ') in bag now.')        
        else:
            lcounter +=1
            write("Try Again")
    corridor()
        
def printHouse():
# to print the house
    print("""`     `'::.
    _________H ,%%&%,
   /\     _   \%&&%%&%
  /  \___/^\___\%&%%&&
  |  | []   [] |%\Y&%'
  |  |   .-.   | ||  
~~@._|@@_|||_@@|~||~~~~~~~~~~~~~
     `""") 


def openDoor(a):
    if a == False:
        print("""
    ____________
    |  __  __  |
    | |  ||  | |
    | |  ||  | |
    | |__||__| |
    |  __  __()|
    | |  ||  | |
    | |  ||  | |
    | |  ||  | |
    | |  ||  | |
    | |__||__| |
    |__________|

    """)
    else:
        print("""
        |\ ___________ /|
        | |  /|,| |   | |
        | | |,x,| |   | |
        | | |,x,' |   | |
        | | |,x   ,   | |
        | | |/    |%==| |
        | |    /] ,   | |
        | |   [/ ()   | |
        | |       |   | |
        | |       |   | |
        | |       |   | |
        | |      ,'   | |
        | |   ,'      | |
        |_|,'_________|_| 
""")


def obtainSword():
# to print the sword
    print("""
,_,_,_,_,_,_,_,_,_,_|___________________________________________________
| | | | | | | | | | |__________________________________________________/
'-'-'-'-'-'-'-'-'-'-|-------------------------------------------------/
""")

def obtainPotion():
# to print the potion 
    print("""
      _____
     `.___,'
      (___)
      <   >
       ) (
      /`-.\
      
     /     \

    / _    _\
    
   :,' `-.' `:
   |         |
   :         ;
    \       /
     `.___.' 
""")

def obtainMushroom():
# to print the mushroom
    print("""
       ------------
     /  (_)_   _    \

  /)      (_) (_)      \

 |       _          _   |
| _     (_)   _    (_) _ |
|(_)  _      (_)  _   (_)|
|____(_)_________(_)_____|
 \\\\\\\\\||||||||///////
          |      |
          |      |
          |      |
           \____/
""")

def final_fight():
# The function for the final fight with the dragon
    health_dragon=100
    health=p1.health
    lcounter = 0
    l = ['face','legs','arms','body']
    
    s=(f"""    
       / \    )\__/(     / \       
      /   \  (_\  /_)   /   \      
 ____/_____\__\@  @/___/_____\____ 
|             |\../|              |
|              \VV/               |
         Welcome {p1.name}        
|       -------------------       |
|_________________________________|
 |    /\ /      \\       \ /\    | 
 |  /   V        ))       V   \  | 
 |/     `       //             \ |
 `              V               `  
 """)
    for i in s:
        print(i, end="", flush=True)
        time.sleep(.005)
    print()
    write("\t!!!YOU ENCOUNTER A DRAGON!!!")
    print()
    
    while True:
        if lcounter > 2:
            write("Try (attack) or (defend). You can (run away) as well!")
        x = input()
        if x == "attack":
            write("You attack the dragon")
            dodge=random.randint(1,2)
            
            if dodge == 1:
                write("The dragon dodges your attack")
                write("Dragon's Health: "+str(health_dragon)+' HP')
                print()
                write("The dragon attacks you")
                dodge=random.randint(1,4)
                
                if dodge==1:
                    write("You dodged the dragon's attack")
                    write("Player's Health: "+str(health)+' HP')
                    print()
                
                else:
                    health-=random.randint(10,25)
                    i=random.randint(0,len(l)-1)
                    write("The dragon hits you in your "+l[i])
                    write("Player's Health: "+str(health)+' HP')
                    print()
                    
                    if health<=0:
                        write('\t\t\t\tYOU ARE DEAD!')
                        write('\t\t\t\t  GAME OVER')
                        sys.exit()
            
            elif dodge == 2:
                a,b = attack_range() #determine the damage from attack_range function
                health_dragon-=random.randint(a,b) #this determins the maximum and minimum damage to dragon
                write("You hit the dragon with your sword")
                write("Dragon's Health: "+str(health_dragon)+' HP')
                print()
                
                if health_dragon<=0:
                    write('\t\t\tCONGRATULATIONS!! THE DRAGON HAS BEEN DEFEATED!!')
                    write('\t\t\t\t\tYOU WIN!')
                    write('\t\t\t\t\tTHE PRINCESS HAS BEEN SAVED!!!')
                    write("\t\t\t\t\tGrade" + playerGrade())
                    sys.exit()
        
        elif x == "defend":
            write("The dragon attacks you")
            dodge=random.randint(1,5)
            
            if dodge == 1:
                health-=random.randint(15,25)
                i=random.randint(0,len(l)-1)
                write("The dragon hits you in your "+l[i])
                write("Player's Health: "+str(health)+' HP')
                print()
                
                if health<=0:
                    write('\t\t\t\tYOU ARE DEAD!')
                    write('\t\t\t\t  GAME OVER')
                    sys.exit()
                
 
            elif dodge != 1:
                write("You dodged the dragon's attack")
                write("Player's Health: "+str(health)+' HP')
                print()
                dodge=random.randint(1,3)
                
                if dodge == 1:
                    write("The dragon dodges your attack")
                    write("Dragon's Health: "+str(health_dragon)+' HP')
                    print()
                
                else:
                    a,b= attack_range()
                    health_dragon-=random.randint(a,b)
                    write("You hit the dragon with your sword")
                    write("Dragon's Health: "+str(health_dragon)+' HP')
                    print()
                    if health_dragon<=0:
                        write('\t\t\tCONGRATULATIONS!! THE DRAGON HAS BEEN DEFEATED!!')
                        write('\t\t\t\t\t\tYOU WIN')
                        write('\t\t\t\t\tTHE PRINCESS HAS BEEN SAVED!!!')
                        write("\t\t\t\t\tGrade" + playerGrade())
                        sys.exit()

        elif x == 'check items':
            print('You have (', ', '.join(bag), ') in bag now.')
        
        elif x == 'run away' or x == 'run' or x == 'leave':
            write("You run away and are now back in the corridor")
            main()
        
        else:
            write("Try Again")
            lcounter+=1
            
bag = [] 
def main():
# The main function  
    global counter
    global items
    items=[]
    corridor()
    exit= False
    lcounter=0
    
    while True:
        
        if counter > 35:
            write("\t\t\tYOU TOOK TOO MANY MOVES")
            write("\t\t\t   YOU ARE DEAD")
            sys.exit()
        print()

        if lcounter > 2:
            write("Try entering kitchen, living room, or the bedroom.")
        x= input()
        counter +=1
        if exit == False:
            if x.lower() == "enter kitchen" or x.lower()=="go to kitchen":
                kitchen()

            elif x.lower() == "enter living room" or x.lower()=="go to living room":
                livingRoom()

            elif x.lower() == "enter bedroom" or x.lower()=="go to bedroom":
                bedroom()

            elif x.lower() == "lift the carpet" or x.lower()=="lift carpet" or x.lower()=="look under carpet" or x.lower()=="look under the carpet" :
                write("You found a hidden trap door to the basement.")
                write("Will you enter? type y/n")
                answer=input()
                if answer.lower()=='y' or answer.lower()=='yes':
                    final_fight()
            
            elif x.lower() == "check items":
                print('You have (', ', '.join(bag), ') in bag.')
            
            else:
                write("Try again")
                lcounter+=1

def check(x):
# function for the inventory
    x = x.lower()
    if 'take' in x:
        item = x.split('take ')
        if item[1] in items:
            take_in_bag(item[1]) 
            print('You have (', ', '.join(bag), ') in bag now.')
            items.remove(item[1])
        else:
            print('''Can only find(''', ', '.join(items), ').')
    if 'drop' in x:
        item = x.split('drop ')
        if item[1] in bag:
            take_out_bag(item[1])
            print('I have (', ', '.join(bag), ') in bag.')
            items.append(item[1])
        else:
            print('''Ah! Can't find it.''')#if the player has not found the item
            print('You only have (', ', '.join(bag), ') in bag.')
    if 'check items' in x:
        print('You have (', ', '.join(bag), ') in bag.')



def take_in_bag(x):
    if x in bag: # checks if the player already has this item
        print('Ah! You already have it!')
        return
    bag.append(x)  # if not, then add the item into the list
    if len(bag) > 3:  # check if the bag has more than 3 items
        del bag[-1]
        print('Ah! Your bag is full.')
        return
    # if the item recently picked up is one of the green item, print special graphic as hint
    if x.lower()=="potion":
        obtainPotion()
    elif x.lower()=="mushroom":
        obtainMushroom()
    elif x.lower()=="sword":
        obtainSword()
    print(f'Ah! You got a {x}.')

def take_out_bag(x):
    if x in bag:
        bag.remove(x)  # remove item from the list
        if len(bag)==1:
            print('Ah! Now you can collect another one.')
    else:
        print("""Ah! Can't find it.""") #if the player has not found the item



start()
main()

    
