arrow = ("       _____  \n       |   |  \n       |   |  \n       |   |  \n       |   |  \n       |   |  \n       |   |  \n     ---   ---\n     \       /\n      \     / \n       \   /  \n        \ /   ")

madlib = input("Do you wanna mad lib? Y/N ")
if madlib == "Y" or madlib == "y":
    print (arrow)
    objects = input("Give me a plural noun or genitalia: ")
    largeobjects = input("Give me another plural noun or genitalia: ")
    location = input("Give me a happy place: ")
    igger = input("Give me something that rhymes with bigger: ")
    print (arrow)
    print (objects + " are big.")
    print (largeobjects + " are bigger.")
    print ("Why is " + location + ",")
    print ("so full of " + igger + "s")
else:
    print (arrow)
    print ("Don't worry, it's racist anyways.")
cont = input("Press Enter to continue.")
print (arrow)
decentcalc = input("Do you wanna try my new calculator? Y/N ")
if decentcalc == "Y" or decentcalc == "y":
    print (arrow)
    num1 = input("Gimme your first number! ")
    symbol = input("Gimme the sign! ")
    num2 = input("Gimme your second number! ")
    print (arrow)
    if symbol == ("+"):
        print (float(num1) + float(num2))
    elif symbol == ("-"):
        print(float(num1) - float(num2))
    elif symbol == ("x") or symbol == ("*"):
        print(float(num1) * float(num2))
    elif symbol == ("/"):
        print(float(num1) / float(num2))
    else:
        print ("haha idiot, try again")
else:
    print (arrow)
    print ("It's ok, math is kinda boring sometimes.")
cont = input("Press Enter to continue.")
print (arrow)
traps = input("Do you wanna see my traps? Y/N ")
if traps == "Y" or traps == "y":
    print (arrow)
    traplist = {
        "Astolfo": "Fate/Grand Order",
        "Totsuka": "Oregairu",
        "Felix": "Re:Zero",
        "Ruka": "Steins;Gate",
        "Hideri": "Blend S"
    }
    sausagemenu = input("Pick a trap, any trap! ")
    print (arrow)
    print (traplist.get(sausagemenu, "My bad, I've only added the popular traps."))
else:
    print (arrow)
    print ("What are you? Scared for your sexuality?")
cont = input("Press Enter to continue.")
print (arrow)

guessgame = input("Do you wanna try to guess? Y/N ")
if guessgame == "Y" or guessgame == "y":
    print (arrow)
    bestgirl = ""
    tries = 0
    while bestgirl != "Futaba" and tries < 3:
        bestgirl = input("Best girl from Bunny Girl Senpai? ")
        tries += 1
        if bestgirl != "Futaba" and tries == 1:
            print ("Justin says you suck at this game!")
        elif bestgirl != "Futaba" and tries == 2:
            print ("Justin says you're gay.")
        else:
            print ("")
    print (arrow)
    if bestgirl == "Futaba":
        print ("Congratulations you are super cultured.")
    else:
        print ("Sorry, none of yo girls are good enough.")
else:
    print (arrow)
    print ("Fine, I don't wanna guess with you either.")
cont = input("Press Enter to continue.")
print (arrow)

exponentcalc = input("Do you wanna try to my new exponent calculator? Y/N ")
if exponentcalc == "Y" or exponentcalc == "y":
    print (arrow)
    num1 = input("Number? ")
    exp = input("To the power of? ")
    prev = 1
    for trials in range(int(exp)):
            prev = (int(prev) * int(num1))
    print (prev)
else:
    print ("It's all good. You really don't wanna math huh.")