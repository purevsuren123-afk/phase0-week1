x = int(input("what's your grade? ..."))
print(f"your grade is {x}")
if x >= 90 and x <= 100:
    print("you got an A")
elif x >= 80 and x < 90:
    print("you got a B")
elif x >= 70 and x < 80:
    print("you got a C")
elif x >= 60 and x < 70:
    print("you got a D")
elif x >= 0 and x < 60:
    print("you got an F")
else:
    print("you got an invalid grade")  
