from logic import TruthTable

proposition = input("Enter proposition:")
proposition2 = input("Enter proposition:")

myTable = TruthTable([proposition, proposition2])
myTable.display()
print(myTable.table)
result=0
for row in myTable.table:
	if row [1][0] != row[1][1]:
		result += 1


if result >0:
	print("The propositions are not equivalent")
else:
	print("The propositions are equivalent")
