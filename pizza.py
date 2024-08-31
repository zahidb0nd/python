#store information about a pizza being ordered
pizza = {
    'crust':'thick',
    'toppings':['mushroom','extra cheese']
    }
#summarize the order
print("you order a "+pizza['crust']+"-crust pizza"+" with the following toppings:")
for topping in pizza['toppings']:
    print("\t"+topping)
