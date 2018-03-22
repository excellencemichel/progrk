import csv

import xlrd




with open("michel.csv", "r" ) as csv_file:
	csv_reader = csv.reader(csv_file)

	for line in csv_reader:
		print(line)



workbook =xlrd.open_workbook("excel.xlsx")


#open sheet:

worksheet = workbook.sheet_by_name("Feuil1")
print(worksheet)

worksheet = workbook.sheet_by_index(0)
print(worksheet)

print("La valeur à la ligne 4 et la colonne 2 est {}".format(worksheet.cell(4,2).value))

#Le nombre total de classeur
sheet_count = workbook.nsheets

print("Le nombre total de classeur est de {}".format(sheet_count))

#Le nom de ces classeurs

sheets_name = workbook.sheet_names()
print("Les noms des classeurs sont {}".format(sheets_name))

print(type(sheets_name))

for classeur in sheets_name:
	print(classeur)

#Nombre total de ligne
total_ligne = worksheet.nrows

#Nombre total de colonne 
total_colone = worksheet.ncols

print("Nombre de ligne est {} et le nombre total de colonne est {}".format(total_ligne, total_colone))



#Boucle sur le contenu de la feuille

table = list()
record = list()


for x in range(total_ligne):  # Boucle sur le nombre de ligne
	for y in range(total_colone): # Boucle sur le nombre de colonne
		record.append(worksheet.cell(x,y).value)

	table.append(record)
	record = []
	x +=1



print(table)
