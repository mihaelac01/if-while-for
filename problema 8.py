a = int(input("introduceti 1 latura: "))
b = int(input("introduceti 2 latura: "))
c = int(input("introduceti 3 latura: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    if ((a == b) and (a != c)) or ((a == c) and (a != c)) or ((b == c) and (b != a)):
        print("Numerele formeaza un triunghi isoscel")
    elif (a == b) and (a == c):
        print("Numerele formeaza un triunghi echilateral")
    else:
        print("Numerele formeaza un triunghi scalen")
else:
    print("Numerele nu formeaza un triunghi")
    