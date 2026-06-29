greet=lambda:"hello"                    #lambda with no parameter
print(greet())

single=lambda x:x*x
mult=lambda a,b:a*b
print(single(10),mult(10,20))

#MAP()
n=[1,2,3,4]
result=list(map(lambda x:int(x)*int(x),input("enter digit")))
print(result)