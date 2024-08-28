my_foods = ['pizza','burger','falafel']
friend_foods = my_foods[:]

my_foods.append('mango')
friend_foods.append('banana')
print("my favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("LOOP")
for myfood in my_foods:
    print(myfood)

##here’s what happens when you try to copy a list without using a slice:
#Instead of storing a copy of my_foods in friend_foods at u, we set
#friend_foods equal to my_foods. This syntax actually tells Python to connect the new variable friend_foods to the list that is already contained in
#my_foods, so now both variables point to the same list. As a result, when we
#add 'cannoli' to my_foods, it will also appear in friend_foods. Likewise 'ice
#cream' will appear in both lists, even though it appears to be added only to
#friend_foods.
