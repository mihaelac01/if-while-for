n=int(input("dati un numar: "))
s=0
for i in range(1,n+1):
    p=1
    for n in range(1,i+1):
        p*=n
    s+=p
print("1!+2!+3!+...+n!=",s)