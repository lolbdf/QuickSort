List = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R","r","S","s", ]


for buchstaben in List:
    if 64 < ord(buchstaben) < 91:  # wenn es Großbuchstaben sind
        nummer_buchstabe = ord(buchstaben)
        erg = nummer_buchstabe - 64 + ((nummer_buchstabe - 64) - 1)
    else:  # wenn es Kleinbuchstaben sind
        nummer_buchstabe = ord(buchstaben)
        erg = nummer_buchstabe - 96 + ((nummer_buchstabe - 96))
    print(erg)