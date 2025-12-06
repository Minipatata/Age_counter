name=str(input("Please, enter your name:"))
print("Welcome to AG (Age Generater)",name,"!")
try:
    age=int(input("Please, enter your age to proceede:"))
    print(age)
    if(age<15):
        print("Your age is not valid!")
    else:
        print("Your age is verry valid")
except Exception:
    print("ERROR")
finally:
    print("We'll see you a next time, bye",name)