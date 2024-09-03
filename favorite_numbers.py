fav_nums = {
    'bond':['7','70'],
    'hank':['6','69'],
    'red':['420','240'],
    'bob':['808','007'],
    'rob':['1738','2001'],
    }
for person, num in fav_nums.items() :
    print(person.title()+"'s favorite number is: ")
    for number in num:
        print(number.title())
    print("\n")

    
