Game Name

About:
Old School commands line dungeon crawler-type adventure
game following the plot of saving a princess imprisoned by a dragon.
Players must use their creativity to think of the correct command 
to proceed with the storyline. 

Requirements:
Python 3.x and nothing but standard Python libraries

To play:
run "python cavalier.py"

Gameplay:
1. The player has to type the correct command base on the clues and description to proceed
with the story
2. Decide which items to collect in each room and find a way to rescue the princess
3. How many times the player keyed the game will record an input. The system will give hints after 
a certain amount of incorrect inputs.
4. The aim is to successfully rescue the princess while using the least number of 
wrong inputs

Item Tier List:
    Green(Will help you win):      Sword, Potion, Mushroom
    Yellow(Decoy):                 Knife, Batteries, Painting
    Red(Will hurt you):            Apple, lighter

Attack Random Range:
    3 green items:  20-30
    2 green items:  15-25
    1 green item:   10-20
    0 green item:   1- 10

How battle works:
- Once the player enters the basement, the battle will occur as follows
At the beginning of each turn, the player can decide if they want to 'attack' or
'defend'.

    - If they choose to attack, they will have a 50% chance of hitting the dragon
    The damage they deal will depend on the items they have in their inventory.
    However, if the attack miss, the dragon now has a chance to attack them back.
    The player will have a 25% chance of dodging the attack.

    - If they choose to defend, they will have an 80% chance of dodging the dragon's
    attack. If you avoided the attack, you now have a 1/3 chance to hit the dragon,
    However, the damage you receive will also be random within a range, if the dragon hits you. 

- This loop continues until the player or the dragon's hp is <= 0
-The player can choose to "run away", which will bring them back to the main corridor


Extra Credit:
Graphics from:
    House from: https://www.asciiart.eu/buildings-and-places/houses
    Doors from: https://ascii.co.uk/art/doors
    Sword from: https://www.asciiart.eu/weapons/swords
    Potion from: https://ascii.co.uk/art/bottle
    Mushroom from: https://www.asciiart.eu/plants/mushroom
    Dragon from: https://www.asciiart.eu/mythology/dragons
