import csv


annoPrec = 0 
dizionario = {0:0}

with open("annual.csv", newline="", encoding="ISO-8859-1") as file:

    csv_reader = csv.reader(file, delimiter=',')
    
    for riga in csv_reader:
        riga[2] = float(riga[2])
        if riga[1] != annoPrec:
            dizionario[riga[1]] = riga[2] 
            annoPrec = riga[1]
        else:
            dizionario[annoPrec] = round((dizionario[annoPrec] + riga[2]) / 2, 3)

    print(dizionario)

def trovaMaxMin(anno1, anno2):
    max = dizionario[anno1]
    for k in range(int(anno1), int(anno2) + 1, 1):
        if (dizionario[str(k)] > max):
            max = dizionario[str(k)]
    
    print(max)

    min = dizionario[anno1]
    for k in range(int(anno1), int(anno2) + 1, 1):
        if (dizionario[str(k)] < min):
            min = dizionario[str(k)]
    
    print(min)

trovaMaxMin("2013","2016")