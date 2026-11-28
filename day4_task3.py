def scope_demo():
    secret = 42          # local variable

scope_demo()
print(secret)            # this will cause a NameError
