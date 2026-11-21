x = int(input("what's x? ..."))

if x >0: 
    print(str(x) + " is positive")
elif x<0:
    print(str(x) + " is negative")
else:
    print(str(x) + " is zero")  
if x % 2 == 0:
    print(str(x) + " is even")
else:
    print(str(x) + " is odd")