# Electricity bill calculator - first 100 units-> 1.5/unit  
#  next 100 units 2.50 and above 200 units 4/unit.
#  calc bill when sample input->75 unit= 75*1.50=112.50

n=int(input("enter qnty of units used: "))
if 0<n<=100:
    print(n*1.50)
elif (n<200):
    print(1.50*100+(2.50*(n-100)))
else:
    print(1.50*100+2.50*100+4*(n-200))


