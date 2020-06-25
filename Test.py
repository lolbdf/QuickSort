def teilung(list, low, high):

    print("Teilung")

    pivot = list[high]

    low_cache = low

    high_cache = high

    while low < high:

        print("Schleife eins")

        while high > low_cache and list[high] > pivot:
            high -= 1

        while low < high_cache and list[low] < pivot:
            low += 1

        if low < high:
            list[low], list[high] = list[high], list[low]


    if list[low] > list[high_cache]:
        list[high_cache], list[low] = list[low], list[high_cache]

    return low

def quicksort(liste, erstes, letztes):  # rekursive Funktion

    if erstes < letztes:
        pivot = teilung(liste, erstes, letztes)  # erster Durchlauf mit kompletter Liste von anfang bis Ende
        quicksort(liste, erstes, pivot - 1)
        quicksort(liste, pivot + 1, letztes)

    return liste  # Die geordnete Liste wird zurückgegeben

LISTE = [4,6,13,6,8,7,2,1,4]
print(quicksort(LISTE,0,len(LISTE)-1))