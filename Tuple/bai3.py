#Bài 3: Chuyển đổi một danh sách các số thành tuple, sau đó in ra các phần tử của tuple bằng vòng lặp for ===========
list_2 = [3, 4, 6, 1, 4, 6]

tuple_2 = tuple(list_2)
print(tuple_2)
for i in tuple_2:
	print(i)
	i +=1