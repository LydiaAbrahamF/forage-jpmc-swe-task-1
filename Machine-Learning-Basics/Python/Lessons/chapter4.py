#Chatper 4 working with lists

#Looping through an entire list
magicians = ['alice ', 'david', 'clorina']
for magician in magicians:
    print(magician.title() + ' that was a great trick!')
    print ("I can't wait to see your next trick, " + magician.title() + ".\n")
print('Thank you, everyone. That was a great magic show!')

#Making Numerical Lists
for value in range(1,6):
    print(value)
numbers = list(range(1, 6))
print(numbers)
even_numbers = list(range(2,11,2))
print(even_numbers)
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
#simple statistics
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
#List Comprehensions
squares = [value**2 for value in range(1,11)]
print(squares)
#working with part of a list

#slicing a list
players = ['cherles', 'martina','michael', 'florence', 'elif']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
#looping Through a Slice
players = ['charles','martina','micheal','florence','elif']
print("Here are the first three plyers on my team:")
for player in players[:3]:
    print(player.title())
#Copying a List
myFoods = ["pizza", 'flafle', 'carrot cake']
friendsFoods = myFoods[:]
print("My favorite foods are:")
print(friendsFoods)
print("\nMy friend's favorite foods are:")
print(friendsFoods)
#to check we have different lists
myFoods.append('cannoli')
friendsFoods.append('ice cream')
print("My favorite foods are:")
print(friendsFoods)
print("\nMy friend's favorite foods are:")
print(friendsFoods)

#TUPLES
#are just like list except for using brackets
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
#dimensions[0] = 250  we can't assign new vlaue to tuple
#Looping Through All Values in A Tuple
for dimension in dimensions:
    print(dimension)

#writing over a Tuple
print("Original dimesions: ")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions: ")
for dimension in dimensions:
    print(dimension)
#-------------------------------------------
#styling your code
#According to PEP 8 use 4 sapce or 1 tab for every indentation level.
#Line length should less than 80 characters.
#Comments should be limited to 72 characters
#To group your program use blank lines
#
