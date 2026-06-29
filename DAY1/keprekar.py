#n=35

#sqn=str(n**2)
#a=int(sqn[0])
#b=int(sqn[0]+sqn[1])
#c=int(sqn[2]+sqn[3])
#if a+b==n or b+c==n:print("is keprekar")

#else:print("not keprekar")

n=12
sq=n*n
d=len(str(sq))
r=sq%(10**d)
l=sq//(10**d)
if l+r==n:
    print("is keprekar")
else:
    print("not keprekar")