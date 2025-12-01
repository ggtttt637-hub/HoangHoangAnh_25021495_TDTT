a = float(input("a="))
b = float(input("b="))
if a < 0 and b < 0:
    print("yes")
elif a > 0 and b > 0 or a < 0 and b > 0 or a > 0 and b < 0:
    print("no")