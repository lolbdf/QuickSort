import Teilung


def quicksort(liste, erstes, letztes):  # rekursive Funktion

    trenner = Teilung.teilung(liste, erstes, letztes)  # erster Durchlauf mit kompletter Liste von anfang bis Ende

    if erstes < trenner - 1:  # wenn das zurückgegebene Linke wert - 1 großer ist als 0 dann word die list von 0 - linkeselement -1 sortiert
        quicksort(liste, erstes, trenner - 1)

    if trenner < letztes:  # wenn das rechte Element nicht die letzte stelle der Liste ist wird die Liste von linkeselement bis letztes element sortiert
        quicksort(liste, trenner, letztes)
    return liste  # Die geordnete Liste wird zurückgegeben
