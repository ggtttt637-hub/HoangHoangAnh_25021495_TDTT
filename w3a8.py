a = float(input("nhap chuoi a : "))
b = float(input("nhap chuoi b : "))
if len(a) > len(b):
    print("chuoi a dai hon chuoi b")
elif len(a) < len(b):
    print("chuoi b dai hon chuoi a")
else:
    print("hai chuoi bang nhau")