a=int(input("enter 1st no.: "))
b=int(input("enter 2nd no.: "))
c=int(input("enter 3rd no.: "))
d=int(input("enter 4th no.: "))

if a>b and a>c and a>d:
    print(a)
elif b>c and b>d:
    print(b)
elif c>d:
    print(c)
else :
    print(d)
    
