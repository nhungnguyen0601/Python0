#Viết hàm tính giai thừa của một số.
def giai_thua(n):
    if n < 0:
        return "Giai thừa không xác định."
    elif n == 0:
        return 1
    elif n ==1:
        return 1
    else:
        return n * giai_thua(n - 1)

so = int(input("Nhap so: "))

print(f"Giai thua cua {so} la: {giai_thua(so)}")
