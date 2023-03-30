#4.1
pizzas = ['margarita pizza', 'tuna pizza', 'special pizza', 'beef pizza', 'chicken pizza']
for pizza in pizzas:
    print('I like ' + pizza.title())
print('My favorite pizza is Margarita Pizza.\nI like Tuna Pizza Too.\nI can say I really love pizza!')
#4.2
animals = ['ox', 'sheep', 'goat']
for animal in animals:
    print(animal.title() + ' is source of meat')
    print(animal.title() + ' is also a domestic animal')
#4.3
number = []
for num in range(1,21):
    number.append(num)
print(number)
#4.4
millions = [value for value in range(1,1000001)]
print(millions)
#4.5
print(min(millions))
print(max(millions))
print(sum(millions))
#4.6
odd = []
for value in range(1,20,2):
    odd.append(value)
print(odd)
#4.7
threes = [value for value in range(3,30,3)]
print(threes)
#4.8
cubes = []
for value in range (1,11):
    cubes.append(value**3)
print(cubes)
#4.9
cubes = [value**3 for value in range (1,11)]
print(cubes)
#4.10
myCars = ['suzuki', 'Hyunadi', 'Nissan','marcedece', 'v8', 'volcewagen']
print ("My first three cras are: ")
print(myCars[0:3])
print('some of my cars includes:')
print(myCars[1:4])
print('the lastest three cars of mine: ')
print(myCars[-3:])
#4.11
pizzas = ['margarita pizza', 'tuna pizza', 'special pizza', 'beef pizza', 'chicken pizza']
friendsPizza = pizzas[:]
friendsPizza.append('vegtable')
print("My favorite pizzas are: ")
print(pizzas)
print("My friend's favorite pizzas are: ")
print(friendsPizza)
#4.12
foods = pizzas [2:]
for food in foods:
    print(food.title())
foods = friendsPizza [:]
print('\n')
for food in foods:
    print(food.title())
#4.13
buffet = ('special beef burger','club sandwich', 'chicken nugget','shwarma','flafle')
print('\n')
for food in buffet:
    print(food.title())
#4.14PEP 8:
#READING ASSGNMEMT

#4.15
#REVIEW THE CODE OF YOUR PREVIOUS ASSIGNMENT
