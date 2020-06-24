def quicksort(L, anfang, ende):
    if L != []:
        pivot = L[anfang]
        links = anfang
        rechts = ende
        while links <= rechts:
            while L[links] < pivot:
                links = links + 1
            while L[rechts] > pivot:
                rechts = rechts - 1
            if links <= rechts:
                if links < rechts:
                    h = L[links]
                    L[links] = L[rechts]
                    L[rechts] = h
                links = links + 1
                rechts = rechts - 1
            print(L)
            print(anfang, ende, links, rechts)
        print()
        if anfang < rechts:
            L = quicksort(L, anfang, rechts)
        if links < ende:
            L = quicksort(L, links, ende)
    return L


# Test
L = [25, 17, 32, 56, 25, 19, 8, 66, 29, 6, 20, 29]
print(L)
L = quicksort(L, 0, len(L) - 1)
print(L)
