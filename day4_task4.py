def set_age(age):
    if age < 0: 
        raise ValueError("age cannot be negative") #is showing error caused by the function if the number is negative, it will raise the error messesge "..."
    
    return age
print(set_age(25))
print(set_age(-5)) #is negative number and it will cause error message "age cannot be negative"