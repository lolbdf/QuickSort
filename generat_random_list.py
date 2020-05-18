import random

def create(Wort_Anzahl):
    liste = []
    for i in range(Wort_Anzahl):
        wortlänge = int(random.uniform(10, 11))
        wort_list = []
        for j in range(wortlänge):
            buchstabe_zahl = int(random.uniform(0,26))
            buchstabe = chr(buchstabe_zahl + 97)
            wort_list.append(buchstabe)
            wort = ""
        for k in range(len(wort_list)):
            wort = wort + wort_list[k]
        liste.append(wort)
    return liste
