woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
woerterbuch_englisch = ["apple", "pear", "cerry", "melon", "apricot", "peach"]

def addWord(deutschesWort, englischesWort):
    try:
        searchWord(deutschesWort)
        print("Wort bereits vorhanden")
    except:
        woerterbuch_deutsch.append(deutschesWort)
        woerterbuch_englisch.append(englischesWort)
    
def searchWord(wordInput):
    index = 0
    for wort in woerterbuch_deutsch:  
        if wordInput.lower() == wort.lower():  
            break
        index +=1   
    
    if index == len(woerterbuch_deutsch):
        index=0
        for wort in woerterbuch_englisch:     
            if wordInput.lower() == wort.lower():
                break
            index +=1    
        
        if index == len(woerterbuch_englisch):
            raise Exception("nicht gefunden")
    return (woerterbuch_deutsch[index], woerterbuch_englisch[index], index)

def delWord():
    try:
        output = searchWord(input("zu löschendes Wort?: "))
        woerterbuch_deutsch.remove(output[0])
        woerterbuch_englisch.remove(output[1])
    except Exception as e:
        print(e)
        
def getWord():
    try:
        output = searchWord(input("Zu übersetzendes Wort: "))
        print(output[0] + "[DE]")
        print(output[1]+ "[EN]")
    except Exception as e:
        print(e)
        
def eingabeBefehl():
    while True:
        auswahl = input("Befehl? \n[E]infügen \n[L]öschen \n[A]bfrage \n[Q]uit: ")
        if auswahl.lower() == "e" or  auswahl.lower() =="l" or auswahl.lower() =="a" or auswahl.lower() =="q":
            return auswahl.lower()
        else:
            print("Falsche Eingabe!")
    
while True:
    auswahl = eingabeBefehl()
    if auswahl == "e":
        addWord(input("Deutsches Wort eingeben: "), input("Englisches Wort eingeben: "))
        
    elif auswahl == "l":
        delWord()
    elif auswahl == "q":
        break   
    else:
        getWord()

    print(woerterbuch_deutsch)
    print(woerterbuch_englisch)
    
