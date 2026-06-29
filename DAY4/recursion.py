#def climbStairs(n):
        #if n==1 or n==0:
            #return 1
        #return climbStairs(n-1)+climbStairs(n-2)
#print(climbStairs(4))

def mcCarthy(n):
    if n>100:
        return n-10
    return mcCarthy(mcCarthy(n+11))
n=int(input('Enter a number:'))
print("Number:",mcCarthy(n))