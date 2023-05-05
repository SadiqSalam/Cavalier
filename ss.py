import time
import sys
import random
def write(s):
    for i in s:
        print(i, end="", flush=True)
        time.sleep(.04)
    print()
    # for i in s:
    #     if i in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
    #         print(i, end="", flush=True)
    #         time.sleep(.01)
    #     else:
    #         print(i, end="", flush=True)
    # print()
bag = ("sword","potion","mushroom")
def attack_range():
    # global bag
    greenItems = ["sword", "potion", "mushroom"]
    numGreen = 0
    # print(list(ranRange.values()))
    for i in bag:
        if i.lower() in greenItems:
            numGreen+=1
    if numGreen> 2:
        return 20,30
    elif numGreen>1:
        return 15,25
    elif numGreen>0:
        return 10,20
    else:
        return 1,10



def final_fight():
    l=['face','legs','arms','body']
    health=50
    health_dragon=100
    s=("""    
       / \    )\__/(     / \       
      /   \  (_\  /_)   /   \      
 ____/_____\__\@  @/___/_____\____ 
|             |\../|              |
|              \VV/               |
|        ----------------         |
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
        x=input()
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
                    # a,b = attack_range()
                    health-=random.randint(10,25)
                    i=random.randint(0,len(l)-1)
                    write("The dragon hits you in your "+l[i])
                    write("Player's Health: "+str(health)+' HP')
                    print()
                    if health<=0:
                        write('\t\t\t\tYOU ARE DEAD!')
                        write('\t\t\t\t  GAME OVER')
                        sys.exit()
            
            else:
                a,b = attack_range()
                # print(a,b)
                health_dragon-=random.randint(a,b)
                write("You hit the dragon with your sword")
                write("Dragon's Health: "+str(health_dragon)+' HP')
                print()
                if health_dragon<=0:
                    write('\t\t\tCONGRATULATIONS!! THE DRAGON HAS BEEN DEFEATED!!')
                    write('\t\t\t\t\tYOU WIN!')
                    sys.exit()
        
        elif x == "defend":
            write("The dragon attacks you")
            dodge=random.randint(1,4)
            
            if dodge == 1:
                # a,b = attack_range()
                health-=random.randint(10,25)
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
               
#        elif x == "defend":
#             write("The dragon attacks you")
#             dodge=random.randint(1,3)
            
#             if dodge == 1:
#                 write("You dodged the dragon's attack")
#                 write("Player's Health: "+str(health)+' HP')
#                 print()
#                 write("You attack the dragon")
#                 dodge=random.randint(1,3)
                
#                 if dodge == 1:
#                     write("The dragon dodges your attack")
#                     write("Dragon's Health: "+str(health_dragon)+' HP')
#                     print()
                
#                 else:
#                     health_dragon-=random.randint(5,50)
#                     write("You hit the dragon with your sword")
#                     write("Dragon's Health: "+str(health_dragon)+' HP')
#                     print()
#                     if health_dragon<=0:
#                         write('\t\t\tCONGRATULATIONS!! THE DRAGON HAS BEEN DEFEATED!!')
#                         write('\t\t\t\t\t\tYOU WIN')
#                         sys.exit()
 
#             elif dodge != 1:
#                 health-=random.randint(5,20)
#                 i=random.randint(0,len(l)-1)
#                 write("The dragon hits you in your "+l[i])
#                 write("Player's Health: "+str(health)+' HP')
#                 print()
#                 if health<=0:
#                     write('\t\t\t\tYOU ARE DEAD!')
#                     write('\t\t\t\t  GAME OVER')
                    # sys.exit()
        elif x == 'check inventory':
            inventory()
        
        elif x == 'run away':
            print("You run away and are now back in the corridor")
            main()
final_fight()




