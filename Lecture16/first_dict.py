#!/usr/bin/python3
import os
os.system('clear')

personal_info = {}

def evaluate(name,age,colour,python,flat):
    import string
    print("You have provided the following details:\nName: ",name,"\nAge: ", age,"\nFavourite colour: ", colour,"\nPython preference: ", python, "\nFlat World: ", flat)
    for character in name:
        if character not in string.ascii_letters:
            return print("\nPlease provide a real name")
    if age < 21 :
        print("\nAw, you're just a baby!")
    if colour != "dark green":
        print("\new")
    else:
        print("\nDARK GREEN IS MY FAVE TOO! :)")
    if python[0] != "y":
        print("\nIt could be worse, we could be doing bash again")
    if flat != "False":
        print("\nYou must have spelt False wrong...")
    return print("Thanks for answering")

personal_info['name'] = input("What's your name? ")
personal_info['age'] = int(input("How old are you? "))
personal_info['colour'] = input("What is your favourite colour? ")
personal_info['python'] = input("Do you like Python? ")
personal_info['flat'] = input("Is the world flat? True/False ")

#print(list(personal_info.items()))

evaluate(*list(personal_info.values()))
