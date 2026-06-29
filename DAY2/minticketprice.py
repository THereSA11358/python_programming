n=int(input("enter number of tickets: "))
cat=int(input("enter 1 if student else 0: "))
price=200
amount=(n*price)
discount=0
#edge cases
if n>=15:
    discount+=20
if cat==1:
    discount+=5
if discount>0:
    amount=amount-(amount*discount/100)
    print(amount)
    if n>15 and cat==1:
        print("maxticken=t and student discounta applied")
    elif n>15:
        print("max ticket discount applied")
    else:
        print("student discount applied")
else:
    print(amount, "no discount")
        
    