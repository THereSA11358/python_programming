n=eval(input("enter list: "))
k=1
l=[]
freq=dict()
count=0
for num in n:
    freq[num]=freq.get(num,0)+1
for key,value in freq.items():
    if value==1:
        l.append(key)
print("lost product id:",l)