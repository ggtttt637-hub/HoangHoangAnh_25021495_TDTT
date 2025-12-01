a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
d = float(input("d="))
if a > b and a > c and a > d:
    print("a lon nhat =", a)
elif b > a and b > c and b > d:
    print("b lon nhat =", b)
elif c > a and c > b and c > d:
    print("c lon nhat =", c)
else:
    print("d lon nhat =", d)