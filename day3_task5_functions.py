def check_odd_even(number): 
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_odd_even(10))
print(check_odd_even(11))
print(check_odd_even(12))
print(check_odd_even(13))
print(check_odd_even(14))
print(check_odd_even(15))
print(check_odd_even(16))
print(check_odd_even(17))

def check_grade(x):
    if x >= 90 and x <= 100:
        return "you got an A"
    elif x >= 80 and x < 90:
        return "you got a B"
    elif x >= 70 and x < 80:
        return "you got a C"
    elif x >= 60 and x < 70:
        return "you got a D"
    elif x >= 0 and x < 60:
        return "you got an F"
    else:
        return "you got an invalid grade"

score = int(input("Enter your score: "))
print(check_grade(score))

print(check_grade(95))
print(check_grade(72))
print(check_grade(40))