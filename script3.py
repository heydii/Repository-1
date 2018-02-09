#!/usr/bin/python3
while True:
    password = input("Podaj hasło: ")
    if password != "admin1":
        print("Niepoprawne hasło")
        continue
    print("Uzyskano dostęp!")
    break

print("Super tajne dane")
