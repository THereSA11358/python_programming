ip=int(input("enter mm: "))
if ip in range(0,1):
    print("no rain")
elif ip in range(1,5):
    print("light rain")
elif ip in range(5,10):
    print("moderate rain")
else:
    print("heavy rain")
