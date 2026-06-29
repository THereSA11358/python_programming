l=int(input("Enter Number of Items:"))
product={}
for i in range(1,l+1):
    k=input("Enter item:")
    v=int(input("Enter price:"))
    product[k]=v
sortby=int(input("1 to sort by items, 0 to sort by price"))
if sortby==1:
    sortbykey=dict(sorted(product.items()))
    print(sortbykey)
else:
    sortbyvalue=dict(sorted(product.items(), key=lambda item: item[1]))
    print(sortbyvalue)


