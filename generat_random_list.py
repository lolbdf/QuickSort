import random


def create(Wort_Anzahl):
    liste = []
    for i in range(Wort_Anzahl):
        wortlänge = int(random.randint(5, 10))
        wort_list = []
        for j in range(wortlänge):
            buchstabe_zahl = int(random.randint(0, 25))
            buchstabe = chr(buchstabe_zahl + 97)
            wort_list.append(buchstabe)
            wort = ""
        for k in range(len(wort_list)):
            groß = random.randint(0, 1)
            if k == 0:
                if groß == 1:
                    wort_list[k] = chr(ord(wort_list[k]) - 32)
            wort = wort + wort_list[k]
        liste.append(wort)
    return liste
