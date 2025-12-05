a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = float(input("d = "))
if b % a == 0 and a != 0:
  x = b / a
  if x * b == c and x * c == d:
    print("abcd là cấp số nhân")
  else:
    print("abcd không là cấp số nhân")
else:
    print("abcd không là cấp số nhân")
    