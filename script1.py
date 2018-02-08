#!/usr/bin/python3
print("Kalkulator długów")
debt = float(input("Kwota zadłużenia (w PLN): "))
daily_interest = float(input("Karne odsetki za 1 dzień spóźnienia: "))
days = int(input("Liczba dni od upłynięcia terminu spłaty: "))
total_debt = debt + daily_interest * days
print("Całkowity dług wynosi:", total_debt, "PLN")
