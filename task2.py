#!/usr/bin/python3
dziennik = {"Kowalski" : ['2', '3', '2'], "Nowak" : ['4', '5', '4'], "Maliniak" : ['1', '3', '1']}
nazwisko = input("Podaj nazwisko ucznia: ")
if nazwisko in dziennik:
    print('\n'.join(dziennik.get(nazwisko)))
else:
    exit()
