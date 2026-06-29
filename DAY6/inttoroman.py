class Conversion:
    def int_to_roman(self,num):
        romanvalues=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        integers=[1000,900,500,400,100,50,40,10,9,5,4,1]
        romanequal=""
        for i in range(len(integers)):
            while num>=integers[i]:
                romanequal+=romanvalues[i]
                num-=integers[i]
        return romanequal
num=int(input("enter the number:"))
obj=Conversion()
print(obj.int_to_roman(num))
