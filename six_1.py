

person1 = {
    'first':'zahid',
    'last':'hussain',
    'age':'23',
    'city':'bangalore',
    }

person2 = {
    'first':'hank',
    'last':'moody',
    'age':'40',
    'city':'california',
    }

person3 = {
    'first':'raymond',
    'last':'reddington',
    'age':'60',
    'city':'NYC',
    }
people = [person1,person2,person3]

for peeps in people:
    print(f"First name: {peeps['first']}")
    print(f"Last name: {peeps['last']}")
    print(f"Age: {peeps['age']}")
    print(f"city: {peeps['city']}\n")
