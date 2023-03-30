#CHAPTER 5 IF STATEMENTS
cars = ['suzuki', 'bmw', 'nissan', 'toyota' , 'hyunadi']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
#Conditional Tests
car = 'suzuki'
answer = car.upper() == 'SUZUKI'
print(answer)
car = 'nissan'
answer = car == 'bmw'
print(answer)
#checking for inequality
requestedToppping = 'mushrooms'
if requestedToppping != 'anchovies':
    print("Hold the anchovies!")
#Numerical comparisons
age = 18
answer = age == 18
print(answer)
num = 17
if num != 42:
    print("That is not the correct answer. please try again!")
#checking multiple conditions
age0 = 22
age1 = 22
answer = (age0 >= 21 and age1>= 21)
print (answer)
#checking whthere a value is in a list
requestedToppping = ('mushrooms', 'oninos', 'pineapples')
answer = 'mushrooms' in requestedToppping
print(answer)
#checking whthere a value is not in a list
bannedUser = ['andrew','calorina','david']
user = 'marie'
if user not in bannedUser:
    print(user.title() + ' you can post  a response if you wish.')
#Boolean Expressions
gameActive = True
canEdit = False

#if-else statments
age = 20
if age >= 18:
    print("You are old enough to vote")
    print("Have you registered to vote yet?")
else:
    print("\nsorry, you are too young to vote.")
    print("Please register to vote as soon as you trun 18!")
print("--------------")
#The if-elif-else Chain
age = 12
if age < 4:
    print("Your  admission cost is $0.")
elif age < 18:
    print("Your addmission cost is $5")
else:
    print("Your admission cost is $10.")
#Using Multiple elif Blocks
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission is " + str(price) +'.')

#making multiple conditions
requestedTopppings = ('mushrooms', 'extra cheese')
if 'mushrooms' in requestedToppping:
    print("Adding mushrooms.")
if 'pepperoni' in requestedToppping:
    print("Adding pepperoni. ")
if 'extra cheese' in requestedToppping:
    print("Adding extra cheese.")
print("\nFinished making your pizza!\n")

#using if with lists
requestedTopppings = ['mushrooms', 'extra cheese', 'green peppers']
for requestedToppping in requestedTopppings:
    print("Adding " + requestedToppping + ".")
print ('\nFinished making your pizza!')

for requestedToppping in requestedTopppings:
    if requestedToppping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requestedToppping + ".")
print("\nFinished making your pizza!")
#checking a list is not empty
requestedTopppings = []
if requestedTopppings:
    for requestedToppping in requestedTopppings:
        print("Adding" + requestedToppping + '.')
    print("\n Finished making your pizzas!")
else:
    print("Are you sure you want plain pizza?")
#using multiple lists
availableToppings = ['mushrooms', 'olive', 'green peppers', 'pepperoni','pineapple','extra cheese']
requestedTopppings = ['mushrooms', 'french fries','extra cheese']
for requestedToppping in requestedTopppings:
    if requestedToppping in availableToppings:
        print("Adding "+ requestedToppping + ".")
    else:
        print("Sorry, we don't have " + requestedToppping + '.')
print("\nFinished making your pizza!")

