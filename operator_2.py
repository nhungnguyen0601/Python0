# a = int(input("a la: "))
# b = int(input("b la: "))
# print(f"Tổng hai số nguyên a và b là {a + b}")
# print(f"Hiệu hai số nguyên a và b là {a - b}")

# a = float(input("Nhap a = "))
# a += 10
# print(f"Sau khi cong a, gia tri la: {a}")
# a -= 5
# print(f"Sau khi tru a, gia tri la: {a}")
# a *= 8
# print(f"Sau khi nhan a, gia tri la: {a}")
# a /= 2
# print(f"Sau khi chia a, gia tri la: {a}")

# number = int(input("Nhap mot so: "))
# if number > 0:
#     print(f"{number} la so duong")
# elif number < 0:
#     print(f"{number} la so am")
# else:
#     print("Day la 0")

# Bài tập về nhà 01
# kilomet = float(input("Nhập số kilomet: "))

# total_amount = 0

# if kilomet == 0:
#     print("Không cần trả tiền đi free")
# elif kilomet ==1:
#     total_amount = 15000
# elif kilomet <= 10:
#     total_amount = 15000 + (kilomet - 1) * 13000
# else:
#     total_amount = 15000 + 9 * 13000 + (kilomet - 10) * 11000

# print(f"Số tiền taxi là: {total_amount} VND")

# # Bài tập về nhà 02
# year = int(input("Năm "))

# if (year % 4 == 0 and year % 100 != 0 or year % 400 ==0):
#     print(f"Năm {year} là năm nhuận.")
# else:
#     print(f"Năm {year} không phải là năm nhuận.")
#Bài tập về nhà 03:

# a = float(input("Độ dài cạnh thứ nhất: "))
# b = float(input("Độ dài cạnh thứ hai: "))
# c = float(input("Độ dài cạnh thứ ba: "))

# if (a + b > c) and (a + c > b) and (b + c > a):
#     print("Ba cạnh của  một tam giác hợp lệ.")    
# else:
#     print("Ba cạnh của một tam giác khônghợp lệ.")

# Bai tap 04
# doanh_so = float(input("Nhập doanh số bán hàng: "))

# if doanh_so >= 1000000:
#         print(f" Thưởng: {doanh_so* 0.05}")
# elif doanh_so >= 500000:
#          print(f" Thưởng: {doanh_so * 0.03}")
# elif doanh_so >= 100000:
#          print(f" Thưởng: {doanh_so * 0.01}")
# else:
#         print(f" Thưởng: {0}")

#Bai tap 05
kWh = int(input("Nhập số kWh điện sử dụng:"))
if kWh <=0:
	print("Không hợp lệ")
elif kWh < 50 and kWh > 0:
	print (f"Giá điện là: {50*1500}")
elif kWh == 50 and kWh < 100:
	print (f"Giá điện là: {(50*1500)+ (kWh-50)*2000}")
else:
	print (f"Giá điện là: {(50*1500)+ (kWh-50)*2000+ (kWh-100)*3000}")