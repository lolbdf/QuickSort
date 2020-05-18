import Listen_Dateien
import Quicksort
import time
import liste_mit_anzahl_der_wörter
import exel

#egalllll

# papalapapp
if __name__ == "__main__":  # der teil wird nur ausgeführt wenn man die datei direkt ausführt nicht aber wenn man die Datei importiert

    untergrenze = ""

    obergrenze = ""

    schritte = ""

    laenge = ""

    Liste_der_listen_mit_anzahl_der_woerter = [1]

    datei_schreiben = ""
    erg = ""

    finish_time = ""

    Liste_Zeiten = []

    Liste_laengen = []

    Laufzeitcheck = False

    while True:
        print("Wollen sie eine random generierte Liste sortieren lassen? [Ja / Nein / Laufzeitcheck] ")
        random_check = input(">")
        print()
        print("----------------------------------------------------")
        print()
        if random_check == "Ja" or random_check == "ja" or random_check == "Nein" or random_check == "nein" or random_check == "Laufzeitcheck":
            if random_check == "Ja" or random_check == "ja":
                while True:
                    try:
                        print("Bitte geben sie ein wie viele Wörter die Liste haben soll: ")
                        laenge = int(input(">"))
                        print()
                        print("----------------------------------------------------")
                        print()
                        break
                    except ValueError:
                        print()
                        print("----------------------------------------------------")
                        print()
                        print("Bitte geben sie eine Ganzzah an!")
                        print()
                        print("----------------------------------------------------")
                        print()
                        continue

                random_check = True
                break
            elif random_check == "Nein" or random_check == "nein":
                random_check = False
                break
            else:
                while True:
                    try:
                        print("Bitte geben sie die Untergrenze der Anzahl der Wörter ein: ")
                        untergrenze = int(input(">")) - 1
                        print()
                        print("----------------------------------------------------")
                        print()
                        break
                    except ValueError:
                        print()
                        print("----------------------------------------------------")
                        print()
                        print("Bitte geben sie eine Ganzzah an!")
                        print()
                        print("----------------------------------------------------")
                        print()
                        continue

                while True:
                    try:
                        print("Bitte geben sie die Obergrenze der Anzahl der Wörter ein: ")
                        obergrenze = int(input(">"))
                        print()
                        print("----------------------------------------------------")
                        print()
                        break
                    except ValueError:
                        print()
                        print("----------------------------------------------------")
                        print()
                        print("Bitte geben sie eine Ganzzah an!")
                        print()
                        print("----------------------------------------------------")
                        print()
                        continue

                while True:
                    try:
                        print("Bitte geben sie ein in welchen schritten sie arbeiten möchten: ")
                        print(
                            "z. B. wenn sie 2 eingeben und von 1 - 10 gehen ist die Liste mit der Anzahl der Wörter: 1, 3, 5, 7, 9")
                        schritte = int(input(">"))
                        print()
                        print("----------------------------------------------------")
                        print()
                        break
                    except ValueError:
                        print()
                        print("----------------------------------------------------")
                        print()
                        print("Bitte geben sie eine Ganzzah an!")
                        print()
                        print("----------------------------------------------------")
                        print()
                        continue

                Liste_der_listen_mit_anzahl_der_woerter = liste_mit_anzahl_der_wörter.laufzeitcheck(untergrenze,
                                                                                                    obergrenze,
                                                                                                    schritte)
                Laufzeitcheck = True
                random_check = False
                break

        else:
            print("Dies ist eine Pflichtangabe. Bitte geben sie Ja oder Nein ein!")
            print()
            print("----------------------------------------------------")
            print()

    for i in range(len(Liste_der_listen_mit_anzahl_der_woerter)):

        if Laufzeitcheck:
            laenge = Liste_der_listen_mit_anzahl_der_woerter[i]

        Liste = Listen_Dateien.get_list(random_check, laenge, Laufzeitcheck)  # Die datei wird in ne Liste umgewandelt

        if not Laufzeitcheck:
            datei_schreiben = Listen_Dateien.neue_datei()

        start_time = time.time()

        erg = Quicksort.quicksort(Liste, 0, len(Liste) - 1)  # sortierte Liste wird in erg gespeichert

        finish_time = time.time() - start_time

        if Laufzeitcheck:
            Liste_Zeiten.append(finish_time)
            Liste_laengen.append(Liste_der_listen_mit_anzahl_der_woerter[i])

    if not Laufzeitcheck:

        f = open(datei_schreiben, "w", encoding="utf-8")  # neue Datei mit eingegebenem Pfad erstellt
        print()
        print("----------------------------------------------------")
        print()
        print(
            "Sollte ihre Liste nicht zu ihrer zufriedenheit sortiert wurden sein, Führen sie die Datei erneut aus und achten darauf, das die Wörter einheitlisch getrennt sind, und sie die Trennung korrekt angegeben haben")
        for i in range(len(erg)):  # Datei wird gefüllt mit 1 wort pro zeile
            f.writelines(erg[i] + "\n")
        f.close()

        print("Der sortiervorgang hat " + str(finish_time) + " sekunden gedauert.")
    else:
        exel.write_in_exel(Liste_laengen, Liste_Zeiten)
        print("fertig")
