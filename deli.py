print("The deli has ran out of pastrami")
sandwich_orders = ['pastrami sandwich','Grilled sandwich','Egg sandwich','pastrami sandwich','pastrami sandwich','Chicken sandwich','Grilled cheese','Club sandwich']
finished_sandwiches = []

while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')


while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"\ni made your {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)

print("\nSandwiches made")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")




