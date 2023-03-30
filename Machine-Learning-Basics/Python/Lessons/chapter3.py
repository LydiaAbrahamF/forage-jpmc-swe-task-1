#Chapter 3 List
bicyles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicyles)
#acessing elemnts in list
print(bicyles[0].title())
print(bicyles[1].title())
print(bicyles[-1].title())
print(bicyles[3].title())
#using individua values from a list
message = "My first bicycle was a " + bicyles[0].title() + "."
print(message)
#3.1Names
names = ['ana', 'brad', 'jason', 'kaleb']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
#3.2greetings
message = print(" Hello, " + names[0].title() + " welcome back!")
message = print(" Hello, " + names[1].title() + " welcome back!")
message = print(" Hello, " + names[2].title() + " welcome back!")
message = print(" Hello, " + names[3].title() + " welcome back!")
#3.3 your own listing
transport = ['suzuki dezire', 'hyundai strek', 'nissan Qashiqa', 'private plane']
affirmation = print("I have " + transport[0].title())
affirmation = print("I have " + transport[1].title())
affirmation = print("I have " + transport[2].title())
affirmation = print("I have " + transport[3].title())

#modifying element in a list

motorcycles = ['honda', 'yamah', 'suzuki']
print(motorcycles)

#changing
motorcycles[0] = 'ducati'
print(motorcycles)

#adding
motorcycles.append('ducati')
print(motorcycles)

#inserting
motorcycles.insert(2, 'ducati')
print(motorcycles)

#removing first item
motorcycles.remove('ducati')
print(motorcycles)
del motorcycles[1] #deleting at any position
print(motorcycles)

#removing using pop page
cars = ['suzuki','hyunadi', 'nissan','toyota']
print (cars)
poppedCars = cars.pop()
print(cars)
print(poppedCars)
print('The last car I owned was a ' + poppedCars.title() + ' .')
firstOwned = cars.pop(0)
print('The first car I owned was a ' + firstOwned.title() +' .')
cars = ['suzuki','hyunadi', 'nissan','toyota']
print (cars)
removed = 'suzuki'
cars.remove(removed)
print (cars)
too_expensive = 'nothing'
print ( too_expensive.title()+ ' is too expensive for me!')

#organizing a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list: ")
print(cars)
print ("Here is reversed list: ")
cars.sort(reverse= True) #permanently changed unless declared again
print(cars)
print("Here is sorted list: ")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars)) #temporary sorting
print("Here is the original list again: ")
print(cars)
#finding the length of a list
cars = ['suzuki', 'toyota', 'nissan' , 'hyundai']
length= len(cars)
print (length)
