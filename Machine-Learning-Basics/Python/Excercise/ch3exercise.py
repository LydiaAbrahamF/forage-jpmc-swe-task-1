
#3.4 Guest List
guest = ['mr abraham firew ','mrs getenesh abera ', 'sir kasa ']
firstGest = guest.pop()
SecondGest = guest.pop(1)
ThirdGest = guest.pop(0)
print (firstGest.title())
print (SecondGest)
print(ThirdGest)
print ( 'Dear ' + firstGest.title() + "you are invited to sheraton Addis Hotel for VIP dinner invitation on March 27 2024!")
print ( 'Dear ' + SecondGest.title() + "you are invited to sheraton Addis Hotel for VIP dinner invitation on March 27 2024!")
print ( 'Dear ' + ThirdGest.title() + "you are invited to sheraton Addis Hotel for VIP dinner invitation on March 27 2024!")

#3.5 changing guest list
print ('Unfortunately, '+ firstGest.title() + ' can not make it!')
guest = ['mr abraham firew ','mrs getenesh abera ', 'sir kasa ']
guest.insert(2, 'Mrs. Elifnesh Gemechu')
guest.pop()
firstGest = guest.pop()
SecondGest = guest.pop(1)
ThirdGest = guest.pop(0)
print ( 'Dear ' + firstGest.title() + "you are invited to sheraton Addis Hotel for VIP dinner invitation on March 27 2024!")
print ( 'Dear ' + SecondGest.title() + "you are invited to sheraton Addis Hotel for VIP dinner invitation on March 27 2024!")
print ( 'Dear ' + ThirdGest.title() + "you are invited to sheraton Addis Hotel for VIP dinner invitation on March 27 2024!")

#3.5 more guests
guest = ['mr abraham firew ','mrs getenesh abera ', 'sir kasa ']
guest.insert(2, 'Mrs. Elifnesh Gemechu')
guest.pop()
firstGest = guest.pop()
SecondGest = guest.pop(1)
ThirdGest = guest.pop(0)
print ( 'Dear ' + firstGest.title() + " you are invited to sheraton Addis Hotel for VIP dinner invitation on March 27 2024!")
print ( 'Dear ' + SecondGest.title() + " you are invited to sheraton Addis Hotel for VIP dinner invitation on March 27 2024!")
print ( 'Dear ' + ThirdGest.title() + " you are invited to sheraton Addis Hotel for VIP dinner invitation on March 27 2024!")
print ( 'Fortunately I found 3 more palces for reservation')
guest.insert(2,'miss gelila abraham')
guest.insert(3,'miss amerti abraham')
guest.append('mrs amanuel abreaham')
firstGest = guest.pop()
SecondGest = guest.pop(1)
ThirdGest = guest.pop(0)
print ( 'Dear ' + firstGest.title() + " you are invited to sheraton Addis Hotel for VIP dinner invitation on March 27 2024!")
print ( 'Dear ' + SecondGest.title() + " you are invited to sheraton Addis Hotel for VIP dinner invitation on March 27 2024!")
print ( 'Dear ' + ThirdGest.title() + " you are invited to sheraton Addis Hotel for VIP dinner invitation on March 27 2024!")
#shrink guest list
print ('Sadly there is only 2 seats available')
guest = ['mr abraham firew ','mrs getenesh abera ', 'sir kasa ']
guest.insert(2, 'Mrs. Elifnesh Gemechu')
guest.pop()
guest.insert(2,'miss gelila abraham')
guest.insert(3,'miss amerti abraham')
guest.append('mr amanuel abraham')
guest.remove('miss gelila abraham')
guest.remove('miss amerti abraham')
guest.remove('mr amanuel abraham')
guest.remove('Mrs. Elifnesh Gemechu')
print ( 'Dear ' + guest.pop().title() + " you are still invited to sheraton Addis Hotel for VIP dinner invitation on March 27 2024!")
print ( 'Dear ' + guest.pop(0).title() + " you are still invited to sheraton Addis Hotel for VIP dinner invitation on March 27 2024!")
print (guest)

# I should have used del to empty the list but it was not working since it was already popped out

#3.8 seeing the world
vacation = ['France', 'Italiy', 'England', 'USA', 'Jerusalem']
print(sorted(vacation))
print(vacation)
vacation.sort(reverse=True)
print(vacation)
print('original unsorted list: ')
print(vacation)
print("permanently reversed list: ")
vacation.reverse()
print (vacation)
print("The current order of the list: ")
print(vacation)
print('reversed again: ')
vacation.reverse()
print (vacation)
print('sorted list')
vacation.sort()
print(vacation)

print('resorted list')
vacation.sort(reverse=True)
print(vacation)
