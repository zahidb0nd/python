prompt = "\nHow old are you? "
prompt += "Type quit to exit: "

while True:
    age = input(prompt)
    if age == 'quit':
        print("\nthank you, visit again")
        break
    age = int(age)
    if age < 3:
        print("The ticket is free")
    elif age <= 12:
        print("the ticket is $10")
    else:
        print("The ticket is $15")

