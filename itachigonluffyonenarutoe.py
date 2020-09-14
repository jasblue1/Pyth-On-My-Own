from math import *
god = "Steven"
answer = "Yeah"
ranking = "1"
age_legal = 18
arrow = ("       _____  \n       |   |  \n       |   |  \n       |   |  \n       |   |  \n       |   |  \n       |   |  \n     ---   ---\n     \       /\n      \     / \n       \   /  \n        \ /   ")
print ("We love " + god)
print (god.upper() + " is the number " + ranking + " life form in the universe")
print (god.lower().isupper())
print ("In meters, How long is my dick?")
print (len(god))
print ("Those were some fun experiments\nright?")
print (answer[0])
print ("How many times will I need to cry for myself?")
print (god.index("n"))
print (god.replace("Steven","River") + " is the number " + ranking + " life form in the universe")
print ("Officer, Erick said she was " + str(age_legal) + ", but she's actually " + str(age_legal-4))
print ("My GPA is a " + str(sqrt(9) - 1))
print (str(6) + " Pistols")
print ("I wish my GPA was a " + str(pow(2.1,2)))
rainbow = ["red" , "orange" , "yellow" , "green" , "blue" , "purple"]
rainbow.append("black")
rainbow2 = rainbow.copy()
print (rainbow[5])
print (rainbow[6])
print ("Blue is at location " + str(rainbow.index("blue")))
rainbow2.sort()
print (rainbow2)
rainbow2[6] = "white"
print (rainbow2[6])
tupperman = ("Joe","Clank", "Assblaster")
print ("I love my friend, " + tupperman[2] + "!")
print ("^just ignore this mess, I was having fun, also remember to research OR statements for Y or y")
print ("-------------------------------------------------------------")
print (arrow)

funtime = input("Do you wanna try the fun stuff? Y/N ")
if funtime == "Y" or funtime == "y":
    print (arrow)
    selection = input("What would you like to play today?\n1:Weeb Experiment\n2:Math Experiment\n3:Exponent Experiment")
    if selection == "1":
        print (arrow)
        weeb = input("You really want to do some weeb shit? Y/N ")
        if weeb == "Y" or weeb == "y":
            print(arrow)
            name = input("What's your name?\nWatashi wa ")
            waifu = input("--------\nAstolfo\nRaphtalia\nRem\nHayasaka\nRuka\nIshigami\n--------\nWho is best girl? ")
            if waifu == "Astolfo":
                print(arrow)
                print("That's kinda gay, " + name + ", and I LOVE THAT SHIT!")
            elif waifu == "Raphtalia":
                print(arrow)
                print(name + ", dude she's like....underage, right? ARE YOU A FURRY?")
            elif waifu == "Rem":
                print(arrow)
                print(name + ", No one here is named Rem, did you mean Emilia, or Ram?")
            elif waifu == "Hayasaka":
                print(arrow)
                print(name + ", you spitting facts, Hayasaka best girl.")
            elif waifu == "Ruka":
                print(arrow)
                print(name + ", I think my dick just El Psy Con Grew.")
            elif waifu == "Ishigami":
                print(arrow)
                print("Good answer, " + name + ". I hope you like sports festivals! ")
            else:
                print(arrow)
                print(waifu + " would totally marry you, " + name)
        else:
            print(arrow)
            print("It's not like I wanted you to test my program, baka!")
    elif selection == "2":
        print (arrow)
        calc = input("You really wanna do some quick maths? Y/N ")
        if calc == "Y" or calc == "y":
            print(arrow)
            print("Alrighty then, What's X + Y?")
            X = input("X= ")
            Y = input("Y= ")
            if X == "9" and Y == "10":
                print(arrow)
                print("Mr. Hatley says 21")
            elif X == "10" and Y == "9":
                print(arrow)
                print("Mr. Hatley says 21")
            else:
                print(arrow)
                print("Mr. Hatley says " + str(float(X) + float(Y)))
        else:
            print(arrow)
            print("Mr. Hatley says \"Pussy ass bitch can't handle a few digits huh?\"")
    elif selection == "3":
        exponentcalc = input("Do you wanna try to my new exponent calculator? Y/N ")
        if exponentcalc == "Y" or exponentcalc == "y":
            print(arrow)
            num1 = input("Number? ")
            exp = input("To the power of? ")
            prev = 1
            for trials in range(int(exp)):
                prev = (int(prev) * int(num1))
            print(prev)
        else:
            print("It's all good. You really don't wanna math huh.")
    else:
        print (arrow)
        print ("Pick 1, 2, or 3 next time!")
else:
    print (arrow)
    print ("Fine, no fun for you.")
keepgoing = input("Press Enter to continue")

child = "Erick baka"
def yeet(item):
    print ("I'm boutta yeet this " + item + " out of the window!")
yeet(child)
def divorce(kids):
    return kids / 2

print ("Karen please, the Judge said I'd get " + str(int(divorce(20))) + " children fair and square!")

for jojofan in ["Steven", "River", "Justin", "AJ", "Davy", "Erick", 'Joshua']:
    print (jojofan + " likes Jojo's Bizarre Adventure.")

TwoDList = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print (TwoDList[1][0])
print (TwoDList[2][0])

for row in TwoDList:
    for col in row:
        print ( str(col) + " fish")

#This is the stuff from my jungle.
def wordspicer(phrase):
    result = ""
    newvowel = input("Replace every vowel with this character: ")
    for letter in phrase:
        if letter in "aeiou" and newvowel in "QWERTYUIOPASDFGHJKLZXCVBNM":
            result = result + newvowel.lower()
        elif letter in "AEIOU" and newvowel in "qwertyuiopasdfghjklzxcvbnm":
            result = result + newvowel.upper()
        elif letter in "AEIOUaeiou":
            result = result + newvowel
        else:
            result = result + letter
    return result
# This is not even a cohesive translator...
print (wordspicer(input("Spice up any word: ")))

def japanizer(phrase):
    result = ""
    japancheck = False
    for letter in phrase:
        if letter.lower() in "lbtcdpfgk":
            japancheck = True
            result = result + letter
        elif letter.lower() == "r" and japancheck:
            result = result + "or"
            japancheck = False
        else:
            japancheck = False
            result = result + letter
    return result
# This is not really a Japanese Translator...
print (japanizer(input("Japanize a word that contains 'consonant-r' in it: ")))

joe_file = open("JOE", "r")

for fireforcer in joe_file.readlines():
    print (fireforcer)
joe_file.close()

vulcan = open("Vulcan_Gadgets", "w")
vulcan.write("Magnet Grenades\nPenguin Suit\nTekkyo Airpods\nSloth Goggles")

#Testing Divide by zero with try/except
try:
    nonzero = input("Put a number: ")
    test_error = 10 / float(nonzero)
    print (test_error)
except ZeroDivisionError:
    print ("The number was divided by 0!")
except TypeError:
    print ("Please type something!")

