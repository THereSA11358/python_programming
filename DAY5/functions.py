def greet(a,b):                        #positional
    print("hello",a, "and",b)
greet("apple","orange")

def greet(a="apple"):                  #default
    print("hello",a)
greet()

def add(*args):                        #arbitrary, arguments packed as a tuple.     
    print(sum(args))
    print(args)
add(10,20,40,50)
              
def function(**kwargs):                #arbitrary keyword, packed into a dictionary
    print(kwargs)
function(name='apple',age=45,city='banglore')

def mixed(a,*args):                    #mixed arguments
    print("name is",a)
    print(args)
mixed("apple",20,30,40)


def add(a,b,c):
    print(a+b+c)
numbers=[10,20,30]
add(*numbers)


