def tausch(liste, position_links, position_rechts):  # Linkes und rechtes Element werden vertauscht
    tmp = liste[position_links]
    liste[position_links] = liste[position_rechts]
    liste[position_rechts] = tmp
    return liste  # Die Liste mit den getauschten Elementen wird zurückgegeben
