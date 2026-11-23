import random
def hariul(hariult): 
    if hariult == 1:
        return "yag uu"
    elif hariult == 2:
        return "yag ymuu"
    elif hariult == 3:
        return "ain???"
    elif hariult == 4:
        return "za bishee"
    elif hariult == 5:
        return "buruu buudlaa"
    elif hariult == 6:
        return "azgui blaa"
    elif hariult == 7:
        return "boli boli"

print ("tiim esvel ugui:")
input(">")
r=random.randint(1,7)
fortune=hariul(r)
print(hariul(random.randint(1,7)))