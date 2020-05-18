import xlsxwriter



def write_in_exel(laenge, Zeiten):
    # neues exel Document mit Worksheet erstellen
    workbook = xlsxwriter.Workbook('Werte.xlsx')
    worksheet = workbook.add_worksheet("Datensatz")

    # Format anpassung der ersten und zweiten spalte
    worksheet.set_column('A:A', 20)
    worksheet.set_column('B:B', 60)

    # beschriftunge der ersten und zweiten spalte
    worksheet.write('A1', 'Anzahl der Wörter')
    worksheet.write('B1', 'Zeit für Sortiervorgang')

    # Daten in exel tabelle schreiben
    for i in range(len(laenge)):
        worksheet.write(i+1, 0, laenge[i])
        worksheet.write(i+1, 1, Zeiten[i])

    workbook.close()


