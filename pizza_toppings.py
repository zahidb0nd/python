prompt = "\nEnter your favorite pizza toppings: "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(topping+" added to your pizza")
