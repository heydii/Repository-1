#!/usr/bin/python3
print("Wartość Netto")
gross_amount = float(input("Cena produktu Brutto w PLN: "))
vat_rate = int(input("Stawka VAT: "))
net_amount = gross_amount * (vat_rate)
print("Wartość netto produktu:", net_amount, "PLN")
