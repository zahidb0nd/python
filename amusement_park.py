age = int(input("enter age:\n"))

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("your admission price is $"+str(price)+".")

