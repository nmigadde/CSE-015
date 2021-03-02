number_array = list()
number = input("Enter the number of integers you want: ")
print("Enter those numbers")
for i in range(int(number)):
	n = int(input("number:"))
	result = n % 2
	if result == 1 and n>result:
		odd = n
	number_array.append(int(n))
print(odd)
