import generat_random_list


def get_list(random, laenge=1, laufzeitcheck=False):  # Die Datei wird gelesen und und eine Liste umgewandelt
    liste_random_woerter = []

    if not laufzeitcheck:
        while True:
            if not random:
                try:
                    print(
                        "Bitte geben sie den exakten Pfad an, wo sich die Datei mit den gemischten Wörtern befindet: ")  # Die datei mit den Wörtern wird erfragt
                    datei_lesen = input(">")
                    f = open(datei_lesen, "r+", encoding="utf-8")
                    print()
                    print("----------------------------------------------------")
                    print()
                    break
                except FileNotFoundError:
                    print()
                    print("Dieser Pfad existiert nicht! Bitte versuchen sie es erneut")
                    print()
                    print("----------------------------------------------------")
                    print()
            else:
                try:
                    print(
                        "Bitte geben sie den Pfad ein, wo die gemischte Liste mit den random Wörtern gespeichert werden soll: ")  # Die datei mit den Wörtern wird erfragt
                    datei_random_woerter = input(">")
                    f = open(datei_random_woerter, "w", encoding="utf-8")
                    print()
                    print("----------------------------------------------------")
                    print()
                    break
                except FileNotFoundError:
                    print()
                    print("Dieser Pfad existiert nicht! Bitte versuchen sie es erneut")
                    print()
                    print("----------------------------------------------------")
                    print()

        if not random:
            print("Sollten Jedes Wort in einer neuen Zeile stehen geben sie Bitte eine 1 ein,")
            print(
                "Sollten die Wörter durch ein einzelnes Lehrzeichen getrennt sein geben sie bitte ein Lehrzeichen ein und drücken enter")
            print(
                "Sollten ihre Wörter anders getrennt sein geben sie bitte exakt an, welche Zeichen zwischen den Wörtern stehen.")
            split = input(">")
            print()
            print("----------------------------------------------------")
            print()

            if split == "1":
                liste_started = f.read().split()
            else:
                liste_started = f.read().split(split)

            for i in range(len(liste_started)):
                wert = liste_started[i].split("\n")
                for j in wert:
                    if j != '':
                        liste_random_woerter.append(j)
        else:
            liste_random_woerter = generat_random_list.create(laenge)

            for i in range(len(liste_random_woerter)):  # Datei wird gefüllt mit 1 wort pro zeile
                f.writelines(liste_random_woerter[i] + "\n", )
            f.close()
        return liste_random_woerter  # Die Liste wird zurückgegeben

    else:
        liste_random_woerter = generat_random_list.create(laenge)
        return liste_random_woerter


def neue_datei():
    while True:
        try:
            print(
                "Bitte geben sie den exakten Pfad an, wo sie die Datei mit der sortierten Liste erstellt haben möchten: ")  # erstellort erfragt
            datei_name = input(">")
            f = open(datei_name, "w")  # file variable erstellen
            break  # aus schleife ausbrechen
        except FileNotFoundError:
            print()
            print("Dieser Pfad existiert nicht! Bitte versuchen sie es erneut")
            print()
            print()
    return datei_name  # gibt der existierenden Pfad zurück
