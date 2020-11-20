b=eval(input("dati un numar:"))#numarator
c=eval(input("dati un numar:"))#numitor
d=eval(input("dati un numar:"))#numarator
e=eval(input("dati un numar:"))#numitor
f=(b*e+d*c)
g=c*e
h=b*d
from fractions import Fraction 
if c!=0 or e!=0:
    print("suma este =",Fraction(f,g))
    print("produsul este =",Fraction(g,h))
else:
    print("impartirea la 0 nu are sens")
    


    