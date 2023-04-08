#chapter 6
#Dictionaries

alien0 = {'color': 'green', 'points': 5}
print(alien0['color'])
print(alien0['points'])
#a dictionary in python is a collection of key - value pairs.
#a key value can be a number, a sring, a list, a dictionary

newPoints = str(alien0['points'])
print('you just earned ' + newPoints + ' points!')

#adding new key values
print(alien0)
alien0['x_position'] = 0
alien0['y_position'] = 25
print(alien0)

#modifying values
alien0['color'] = 'yellow'
print(alien0)

alien0 = {'x-position':0, 'y-position':25, 'speed':'medium'}
print("Original x-position: " + str(alien0['x-position']))

if alien0['speed'] == 'slow':
    x_inc = 1
elif alien0['speed'] == 'medium':
    x_inc = 2
else:
    x_inc = 3
alien0['x-position'] = alien0['x-position'] + x_inc
print(alien0)
print ("New x-position: "+ str(alien0['x-position']))
#removing key value
del alien0['speed']
print(alien0)
#dictionary of similar objects
favoriteLanguages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
print(favoriteLanguages)
print("sara's favorite language is " + favoriteLanguages['sarah'].title() + ".")

#looping through all key value pairs
user0 = {
    'username': 'efermi',
    'first' : 'enrico',
    'last' : 'fermi',
}
for key, value in user0.items():
    print("\nKey:" + key)
    print("Value:" + value)

favoriteLanguages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for name, language in favoriteLanguages.item():
    print(name.title() + "'s favorite laguage is " + language.title() + ".")
#page104 chapter6 encountered error
