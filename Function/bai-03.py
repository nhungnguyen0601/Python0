#viết hàm đếm số lượng ký tự hoa, ký tự thường trong một chuỗi
def count_charactor(enter_string):
    upper =0
    lower=0

    for i in enter_string:
        if i.isupper():
            upper +=1
        elif i.islower():
            lower +=1
    return upper, lower

enter_string = input("nhap chuoi: ")
a, b= count_charactor(enter_string)
print("upper =", a)
print("lower =", b)

