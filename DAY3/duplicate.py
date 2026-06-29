l=list(map(int,input("Enter:the numbers ").split()))
if len(l)==len(set(l)):
    print("False")
else:
    print("True")
