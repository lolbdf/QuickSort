import random


def create(Wort_Anzahl):
    liste = []

    for i in range(Wort_Anzahl):
        wortlaenge = int(random.randint(5, 10))
        wort = ""
        for j in range(wortlaenge):
            buchstabe = chr(int(random.randint(97, 122)))
            if j == 0:
                grossbuchstabe = random.randint(0, 1)
                if grossbuchstabe == 1:
                    buchstabe = chr(ord(buchstabe) - 32)
            wort = wort + buchstabe
        liste.append(wort)
    return liste
