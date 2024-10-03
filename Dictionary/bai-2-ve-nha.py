#Bài tập 2: Viết chương trình đếm số lượng ký tự, khoảng trắng, và dấu câu trong một chuỗi.
# a = input("pls enter a sentene: ")
# print(len(a))

#define 1 list ky tu
chuoi = input("Nhap cau: ")

list_ky_tu = [".", ",", ";", "!"]

kytu = 0
space = 0
charactor =0

#for in chuoi
for i in chuoi:
    if i in list_ky_tu:
        kytu +=1
    elif i == " ":
        space +=1
    else:
        charactor +=1

print("so ky tu la: ", kytu)
print("so khoang trang la: ", space)
print("so charactor la: ", charactor)
#if i trong list ky tu +=1
#elif =" " space+=1
#else characters +=1

