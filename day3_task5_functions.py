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

def check_grade(score):
    if score >= 90 and score <= 100:
        return "you got an A"
    elif score >= 80 and score < 90:
        return "you got a B"
    elif score >= 70 and score < 80:
        return "you got a C"
    elif score >= 60 and score < 70:
        return "you got a D"
    elif score >= 0 and score < 60:
        return "you got an F"
    else:
        return "you got an invalid grade"

score = int(input("Enter your score: "))
print(check_grade(score))

print(check_grade(100))
print(check_grade(90))
print(check_grade(89))
print(check_grade(101))
print(check_grade(-5))