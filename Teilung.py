import Check


def teilung(list, low, high):
    pivot = list[high]

    low_cache = low

    high_cache = high

    while low < high:

        while high > low_cache and Check.check_rechts(pivot, list[high]):
            high -= 1

        while low < high_cache and Check.check_links(pivot, list[low]):
            low += 1

        if low < high:
            list[low], list[high] = list[high], list[low]
        else:
            break
    if not Check.check_links(pivot, list[low]):
        list[high_cache], list[low] = list[low], list[high_cache]

    return low
