import Check
import Tausch


def teilung(liste, erstes, letztes):



    pivot = erstes  # Pivot element soll immer das erste Element sein

    position_links = erstes  # das erste element ist immer das linke

    position_rechts = letztes  # das rechte Element ist das immer das letzte

    while position_links <= position_rechts:  # solange sich die Position von links und rechts nicht überkreutzen wird die schleife ausgeführt

        index = 0  # index 0 da wir beim 0ten Element des Wortes starten

        while Check.check_links(liste, pivot, position_links,
                                index):  # solange links nicht größer als pivot wird links zum wort rechts neben sich
            position_links += 1

        while Check.check_rechts(liste, pivot, position_rechts,
                                 index):  # solange rechts nicht kleiner als pivot wird rechts zum wort links neben sich
            position_rechts -= 1

        if position_links <= position_rechts:  # positions tausch
            liste = Tausch.tausch(liste, position_links, position_rechts)
            position_rechts -= 1  # Position links und rechts erhöht, damit beim nächsten durchlauf nicht das selbe wort genommen wird
            position_links += 1
    return position_links  # position links wird zurückgegeben, damit diese dann die neue Teilliste bildet
