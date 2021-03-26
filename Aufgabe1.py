print("Hallo Benutzer")

A = int(input("Eingabe einer Zahl:"))
B = int(input("Eingabe einer zweiten Zahl:"))

if A < B:
    zahl1 = A
    zahl2 = B
elif B > A:
    zahl2 = A
    zahl1 = B
else:
    zahl1 = A
    zahl2 = B
    
Summe = A + B
print ("Summe" , Summe)
Differenz = zahl1 - zahl2
print ("Differenz" , Differenz)
Produkt = A * B
print ("Produkt" , Produkt)
Quotient = zahl2 / zahl1
print ("Quotient" , Quotient)














