#!/usr/bin/python3

people = []

def new_person():
    name = input("Podaj imie osoby: ")
    age = int(input("Podaj wiek osoby: "))
    return {"name": name, "age": age}

def who(being):
    return "It's " + being["name"] + ", they are " + str(being["age"])

for i in range(2):
    people.append(new_person())

for person in people:
    print(who(person))
