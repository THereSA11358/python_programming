oddeven=lambda n:"even" if n%2==0 else "odd"    #lambda fn with conditional expressions
print(oddeven(10))
print(oddeven(11))                              
    
mult=lambda x:lambda y:x*y
double=mult(2)
print(double(10))