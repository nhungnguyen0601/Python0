#=Bài 4: Tìm số lớn nhất và nhỏ nhất trong một danh sách số nguyên. numbers = [5, 1, 9, 3, 7, 2]
numbers = [5, 1, 9, 3, 7, 2]

maxValue = numbers[0]

for number in numbers:
	if number > maxValue:
	    maxValue = number
print(f"Max number is: {maxValue}")

minValue = numbers[0]

for number in numbers:
	if number < minValue:
	    minValue = number
print(f"Min value is: {minValue}")
