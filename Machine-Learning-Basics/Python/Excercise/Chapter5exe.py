#5.1
car = 'subaru'
print(" Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\n car = 'audi'? I predict False. ")
print( car == 'audi')
#5.2

#5.3
alienColor = ('green','yellow','red')
if 'green' in alienColor:
    print('You earned 5 points\n')
#5.4
alienColor = ('green','yellow','red')
if 'green' in alienColor:
    print('You earned 5 points!\n')
else:
    print('You earned 10 points!\n')
#5.5
alienColor = ('green','yellow','red')
if 'green' in alienColor:
    print('You earned 5 points!')
if 'yellow' in alienColor:
    print('You earned 10 points!')
if 'red' in alienColor:
    print('You earned 15 points!')
#5.6 stages
age =13
if age < 2:
    print ('The person is baby')
elif age  >= 2 and age < 4:
    print('The person is toddler')
elif age  >= 4 and age < 13:
    print ('The person is kid')
elif age >= 13 and age < 20:
     print ('The person is teenager')
elif age >= 20 and age < 65:
     print ('The person is an adult')
else:
     print ('The person is an elder')
#5.7
favFruits = ['avocado','pineapple','cherry','blue berry','red berry']
if 'banana' in favFruits:
    print ("You really like bananas!")
else:
    print ("you don't like bananas")
#5.8
users = ['@birukmk', '@lydiaab','@admin', '@gelilaab','@amertiab','@amanuelab']
user = users[:]
for user in users:
    if user == '@admin':
        print("Hello " + user.title() + " would you like to see a status report?")
    else:
        print("Hello " + user.title() + " thank you for logging in again.")
#5.9 page 126/93
