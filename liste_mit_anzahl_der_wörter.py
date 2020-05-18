def laufzeitcheck(untergrenze, obergrenze, schritte):
    liste = []
    for i in range(int(untergrenze), int(obergrenze), int(schritte)):
        liste.append(i+1)
    return liste
