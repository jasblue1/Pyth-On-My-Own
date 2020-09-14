import random

def powercalc (number, exponent):
    result = 1
    for attempts in range(exponent):
        result = (result * number)
    return result
try:
    nummy = input("Number? ")
    powy = input("To the power of? ")
    print(powercalc(int(nummy), int(powy)))
except ValueError:
    print ("Bakayarou, put some fucking digits.")

counting = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for row in counting:
    for col in row:
        print (col)

from ClassTest import Adventurer

Erick = Adventurer("Thief", "Female", "Daggers", "Chaotic-Neutral", "Halfling", True)
Steven = Adventurer("Bard", "Male", "Pan Flute", "Chaotic-Evil", "Halfling", True)
Joshua = Adventurer("Mage", "Male", "Staff", "Anarchist", "Elf", False)
River = Adventurer("Monk", "Male", "Fists", "Lawful Good", "Human", False)
Justin = Adventurer("Ranger", "Female", "Crossbow", "Chaotic Evil", "Elf", True)
Davy = Adventurer("Weaboo", "Male", "Katana", "Super Good", "Black", False)
AJ = Adventurer("Stan", "Male", "K-Pop Discs", "Homosexual", "Asian", True)

Guildmates = {
    "Erick" : Erick,
    "Steven" : Steven,
    "Joshua" : Joshua,
    "River" : River,
    "Justin" : Justin,
    "Davy" : Davy,
    "AJ" : AJ
}

try:
    print (Guildmates.get(input("Who's weapon do you want to see? "), "Please put a friend.").weapon)
except AttributeError:
    print ("Please put a friend I know!")

try:
    jobcheck = input("Who's job do you want to see? ")
    print (jobcheck + " is a " + Guildmates.get(jobcheck).job)
except AttributeError:
    print ("I'm sorry, they aren't registered in the guild.")

