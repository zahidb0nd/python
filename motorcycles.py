motorcycles = ['honda','yamaha','kawasaki']
print(motorcycles)

motorcycles[0]='ducati'
print(motorcycles)

motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0,'KTM')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

last_owned = motorcycles.pop()
print(motorcycles)
print(last_owned)
print("My last motorcycle i owned was a "+last_owned.title()+".")
first_owned = motorcycles.pop(0)
print("the first motorcycle i owned was a "+first_owned.title()+".")
print(motorcycles)

too_expensive = 'kawasaki'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+too_expensive.title()+" is too expensive for me.")
motorcycles.insert(0,'aprilia')
print(motorcycles)
