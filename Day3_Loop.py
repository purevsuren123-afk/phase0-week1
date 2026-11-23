name = ""
while name != "your name":
    print("Please type your name.")
    name = input(">")
print("Thank you!") 

print("how many guests will you have?") 
num_of_guests = int(input(">"))
if num_of_guests > 10:
    print("Sorry, we can't host more than 10 guests.")
print("Thank you for your reservation.")