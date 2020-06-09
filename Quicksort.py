import Teilung


def quicksort(liste, erstes, letztes):  # rekursive Funktion

    if erstes < letztes:
        pivot = Teilung.teilung(liste, erstes, letztes)  # erster Durchlauf mit kompletter Liste von anfang bis Ende
        quicksort(liste, erstes, pivot - 1)
        quicksort(liste, pivot + 1, letztes)



    return liste  # Die geordnete Liste wird zurückgegeben
