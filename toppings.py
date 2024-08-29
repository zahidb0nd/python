available_toppings = ['mushrooms','olives','green peppers','pepperoni','extra cheese']
requested_toppings = ['mushrooms','pineapple','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("adding "+requested_topping+".")
    else:
        print("Sorry, we don't have "+requested_topping+".")
print("\nFinished making pizza")
