from ClassTest import Adventurer

friendslist = []

class Background(Adventurer):
    def access(self):
        return print (
            "Job: " + str(self.job) +
            "\nGender: " + str(self.gender) +
            "\nWeapon: " + str(self.weapon) +
            "\nAlignment: " + str(self.alignment) +
            "\nRace: " + str(self.race) +
            "\nRetarded? " + str(self.is_retarded))

class Friend:
    def __init__(self, name, iq, background):
        self.iq = iq
        self.name = name
        self.background = background
    def add(self):
        friendslist.append(self)

guild = [
    Background("Archer", "Male", "Bow and Arrows", "Chaotic Good", "Elf", "No"),
    Background("Warrior", "Male", "Sword and Shield", "Lawful Good", "Orc", "No"),
    Background("Sorceror", "Male", "Staff and Tome", "Lawful Neutral", "Dwarf", "No"),
    Background("Bard", "Male", "Bagpipes", "Neutral Evil", "Human", "Yes")
]

def avg(list):
    result = 0
    for entry in list:
        result = result + int(entry.iq)
    result = result / len(list)
    return print (result)

f1 = Friend("Davy", "1", guild[1])
f2 = Friend("Justin", "44", guild[0])
f3 = Friend("AJ", "88", guild[2])
f4 = Friend("Erick", "69", guild[3])

f1.add()
f2.add()
f3.add()
f4.add()
avg(friendslist)

f4.background.access()

