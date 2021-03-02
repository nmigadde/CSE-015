from logic import TruthTable

myTable = TruthTable(['-a'])
myTable2 = TruthTable(['a and b'])
myTable3 = TruthTable(['a or b'])
myTable4 = TruthTable(['a -> b'])
myTable5 = TruthTable(['a <-> b'])

myTable.display()
myTable2.display()
myTable3.display()
myTable4.display()
myTable5.display()