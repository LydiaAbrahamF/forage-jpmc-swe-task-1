print ("hello world")
#variables chapter 2
#message = "hello python crash course world!"
message = 'this is also string!'
print (message)
#changing case in a string with  methods
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
#combining strings
fist_name = "ada"
second_name = "lOvlace"
fullName = fist_name + " " + second_name
print(fullName)
print ("Hello, " +fullName.title() +"!")
#adding whitespace string
print ("\tpython")
print("python")
print("Languages: \npython\nC\nJavaScript")
#stripping whitespace
lang = "  python"
print(lang)
lang = lang.lstrip()
print(lang)
#avoiding  syntax error with strings
message1 = "One of python's strength is its diverse community."
#2.5 famous saying
message2 = 'Albert Einstine Once said "A person who never made a mistake never tired anything new".'
print(message1)
print(message2)
#2.3 personal Message
Name = "Eric"
print ("Hello " + Name + ", would you like to learn some python today?")
#2.4 name cases
print(Name.upper())
print(Name.lower())
print(Name.title())
#2.6 famous qoute
famous_person = "Albert Einstein"
print(famous_person.title() + ' once said "A person who never made a mistake never tired anything new".')
#2.stripping name
name2 = '\tLydia'
print (name2)
print(name2.lstrip())
name2 ='\nLydia'
name2 =' Lydia '
print(name2.rstrip())
name2= ' Lydia '
print(name2.strip())
#Numbers
x = 2**4 #exponents
print(x)
#type casting
age = 23
message3 = "Happy "+ str(age) +" rd Birthday"
#TypeError: can only concatenate str (not "int") to str
# if age was not type casted
print(message3)

