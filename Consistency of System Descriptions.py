from logic import TruthTable
import array as arr

proposition = ["Hello"]
proposition[0] = input("Enter a proposition: ")

i = 1

while i == 1:
	more = input("Would you like to enter more (Y/N): ")
	if more == "N" or more == "n":
		i = 0
	else:
		if more == "Y" or more == "y":
			proposition2 = input("Enter a proposition: ")
			proposition.append(proposition2)
			i = 1

check = len(proposition)

if check == 5:
	myTable = TruthTable([proposition[0], proposition[1], proposition[2], proposition[3], proposition[4]])
if check == 4:
	myTable = TruthTable([proposition[0], proposition[1], proposition[2], proposition[3]])
if check == 3:
	myTable = TruthTable([proposition[0], proposition[1], proposition[2]])
if check == 2:
	myTable = TruthTable([proposition[0], proposition[1]])
if check == 1:
	myTable = TruthTable([proposition[0]])

#myTable.display()
#print(myTable.table)
result=0
for row in myTable.table:
	if row [1][0] == row[1][1]:
		result = 1

if result == 1:
	print("Your description is consistent")
else:
	print("Your description is inconsistent")
