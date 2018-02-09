#!/usr/bin/python3
print("Obliczanie cen towarów bez podatku VAT")
prices = input("Podaj ceny towarów (z VAT): ").split(", ")
vat = float(input("Podaj wysokość podatku VAT (w %): "))
vat /= 100
for price in prices:
    base_price = float(price) / (1 + vat)
    # print("Cena towaru bez VAT to: " + str(base_price) + " PLN")
    print("Cena towaru bez VAT to: {:.2f} PLN".format(base_price))
