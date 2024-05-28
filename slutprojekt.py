def openfile():
    with open("qa.txt", "r", encoding="UTF-8") as file:
        everyline = file.readlines()
        nylista = []
        for line in everyline:
            rensad = line.strip()
            nylista.append(rensad)
    return nylista

#---------------------------Kollar vart i qa.txt som frågan ligger, svarsalternativet och facit-----------------------

def rattellerfel(lines, allaindex):
    counter = 0  
    for i in range(3):  # Loopar igenom alla frågor
        fråga_index = 0 + i * 6  # Indexet för varje fråga, där varje frågeblock är 6 rader långt
        korrekt_svar_index = 4 + i * 6  # Indexet för det korrekta svaret, som då är i femte raden i varje frågeblock
        counter = queans(lines, fråga_index, korrekt_svar_index, counter) 
    for index in allaindex:
        print("\n Innehåll på rad", index + 1, ":", rattsvar(lines, index))
    return counter

#----------------- Om korrektsvarindex är kortare än hela listan så hämtar den det som står i det indexet ----------------------

def rattsvar(lista, korrekt_svar_index):
    if korrekt_svar_index < len(lista):
        rattasvaret = lista[korrekt_svar_index] # Hämtar det som det står i det indexet
        return rattasvaret  
    else:
        print("Index out of range")


#--------------------------------# ställer frågan + visar svarsalternativen och jämför med korrekt svar--------------------------
def queans(lista, fråga_index, korrekt_svar_index, counter):
    print(lista[fråga_index])  # Printar frågan
    
    # Printar svarsalternativen
    for k in range(3):
        print(f"{lista[fråga_index + k + 1]}")  # Hämtar + printar svarsalternativen 

    try:
        user_ans = int(input("Välj ett svarsalternativ (ange numret): ").strip())
        correct_ans = int(lista[korrekt_svar_index])  
    

        if user_ans == correct_ans:
            print("Rätt svar!")
            counter += 1
        else:
            print(f"Fel svar, rätt svar är: {correct_ans}")


    except ValueError:
        print("Ange ett giltigt nummer!")
    except IndexError:
        print("Ange ett nummer mellan 1-3 som ditt svar!")
    return counter  # Returnera counter så jag kan använda den i saveresult

#-----------------------------Sammanställer resultat i ny txt fil------------------------

def saveresult (counter):
    with open ("sammanstallersvar.txt", "a", encoding="UTF-8") as file:
        file.write(f"Ditt resultat är: {counter}/3\n")

#--------------------------------Main---------------------------
def main():
    lines = openfile()
    allaindex = [4, 10, 16]  # index 4, 10, och 16 som då är svaren
    counter = rattellerfel(lines, allaindex)  # Ta emot den returnerade counter
    saveresult(counter)
    #OM DU VILL KÖRA IGEN
    print("VIll du köra igen, Y/N? ")
    while True:
        skriv = input().strip()
        if skriv == "Y" or "y" or "yes" or "Yes" or "YES":
            main()


main()
