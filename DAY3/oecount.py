l=list(map(int,input("enter: ").split()))

ec=0
oc=0

for j in l:
    if j%2==0:
        ec+=1
    else:
        oc+=1
print("odd=",oc,"even=",ec)