print(10+20)
print("hi"*4)

#custom overloading-- magic methods
class book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        return self.pages+other.pages
b1=book(200)
b2=book(300)
print(b1+b2)