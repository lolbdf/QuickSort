import Convert


def check_links(liste, pivot, links,
                index):  # Es wird überprüft wie das Linke element im Verhältnis zum Pivot element steht

    if Convert.convert(liste[links][index]) < Convert.convert(liste[pivot][index]):  # Ist es kleiner return True
        return True

    if liste[links] == liste[pivot]:  # Sind die WÖRTER Identisch return False
        return False

    try:  # Try except wichtig, wenn die Wörter nicht gleichlang sind
        if Convert.convert(liste[links][index]) == Convert.convert(liste[pivot][
                                                                       index]):  # Wenn die Buchstaben gleich sind, selbe function aber mit Index + 1 (also nächster Buchstabe) -->rekursion
            return check_links(liste, pivot, links, index + 1)

    except IndexError:  # sollten die Buchstaben nicht gleichlang sein
        if len(liste[links]) > len(liste[pivot]):  # wenn links länger als Pivot return False
            return False

        else:  # wenn links kleiner als Pivot return True
            return True

    return False  # wenn hier angekommen muss der wert von links größer sein als Pivot. Deshalb return False


def check_rechts(liste, pivot, rechts, index):  # selbes Spiel wie für links

    if Convert.convert(liste[rechts][index]) > Convert.convert(
            liste[pivot][index]):  # wenn wert vonrechts größer ist als von Links return True
        return True

    if liste[rechts] == liste[pivot]:  # wenn Die wörter identisch sind return False
        return False

    try:  # checken ob die wörter unterschiedlich lang sind
        if Convert.convert(liste[rechts][index]) == Convert.convert(liste[pivot][
                                                                        index]):  # wenn der Wert rechts == Pivot dann die selbe Funktion mit den nächsten Buchstaben der Wörter
            return check_rechts(liste, pivot, rechts, index + 1)

    except IndexError:  # sollte ein wort länger sein als das andere
        if len(liste[rechts]) < len(liste[pivot]):  # ist rechtskleiner als Pivot return false
            return False

        else:  # ist rechts größer return True
            return True

    return False  # sind wir hier angekommen ist der Wert rechts noch großer als Pivot --> return True
