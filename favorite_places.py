favorite_places = {
    'zahid':['qatar','LA','italy'],
    'hank':['NYC','LA'],
    'charlie':['rome','sydney']
    }

for person,places in favorite_places.items():
        print(person.title()+"'s favorite places are: ")
        for place in places:
            print(place.title())
        print("\n")

    
