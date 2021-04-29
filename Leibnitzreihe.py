i = int(input("Anzahl Interationen:"))
zahlIt = 0 
piAnnäh = 0

while zahlIt < i:
    piAnnäh += (-1)**zahlIt/(2*zahlIt+1)
    print("Wert", piAnnäh)
    zahlIt += 1
    
piAnnäh *= 4
print("Annäherung", piAnnäh)

