a = int(input("so nam : "))
if (a % 4 == 0 and not a % 100 == 0) or (a % 400 == 0):
    print("nam nhuan")
else:
    print("nam khong nhuan")