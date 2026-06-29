n1=int(input("enter 1 "))
n2=int(input("enter 2 "))
f=False
if 1<=n1<=100 and 1<=n2<=100:
    for i in range(n1,n2+1):
        num=i
        sum=0
        while i>0:
            ld=i%10
            sum+=(ld**2)
            i=i//10
        if sum==num:
            print(num)
            f=True
if not f:
            print("none")
else:
    print("Wrong Input")
    