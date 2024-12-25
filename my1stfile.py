print("Hello Coders")
print("Hello!", end= " ")
print("Prajita")

name = "Prajita"
title = "Bera"
age = 20
is_genius = True
print(name + " " + title)
print(age)
print(is_genius)

name = input("What is your name?")
print("Hello" + " "  + name)
super_hero = input("What is your superhero name?")
print(super_hero)

old = input("Enter you old age: ")
new = int(old) + 2
print(new)
n=8
print(int(n))
print(str(n))
print(float(n))
print(bool(n))

name = input("Enter name: ")
title = input("Enter title: ")
fullname = name + " " + title
print("Fullname is " + fullname)
no1 = input("Enter 1st number:")
no2 = input("Enter 2nd number:")
x = int(no1) / int(no2)
print("Division is : " + str(x))

name = input("Enter your name : ")
print(name.upper())
print(name.lower())
print(name.find('p'))
print(name.find('P'))
print('P' in name)
print('p' in name)
print(name.replace('P' , 'S'))
print(name.replace('Prajita' , 'Dilip'))

print(3*4)
print(6//4)
print(6%4)
print(3**3)
print(3>4)
print(3<=4)
print(3==4)
print(3!=4)
print(2>3 or 2>=3)
print(2!=3 and 2<=3)
print(not 2>=3)
print(not 2<3)

age = input("Enter the age : ")
if int(age) >= 18:
    print("You're an adult.")
    print("You can vote.")
elif int(age)<18 and int(age)>3:
    print("You're in school.")
else:
    print("You're a child.")
print("Thank you.")

#Calculator(another file)

#Pattern Printing(another file)

j= input("Enter no:")
j = int(j)
for i in range(j):
    print(i)
   #print(i+1)

marks = [15, 16, 17, 18, 19]
print(marks)
print(marks[1])
print(marks[-4])
print(marks[0:4])
print(marks[2:5])
for score in marks:
    print(score)
age = [2,3,5]
age.append(6)
print(age)
age.insert(2,4)
print(age)
print(4 in age)
print(16 in age)
print(len(age))
age.clear()
print(age)
height = [163,170,168,166]
k=0;
while k<len(height): # Print using len operator where k is the index which can not be = length of list as at that index no item is stored
    print(height[k])
    k = k+1

strength = ['40','35','33','37','43']
for s in strength:
    if s == '37':
        break
    print(s)

grade = ['4','5','6','7','8','9']
for g in grade:
    if g == '6':
        continue
    print(g)

list = (66, 23, 45, 23, 12, 67, 23)
feast = 12, "Rice", 34, 67, "Rice", "Chicken"
print(list.count(23))
print(list.index(23))
print(list.index(12))
print(feast.count("Rice"))
print(feast.index(67))

set = {"circle", "square", "kite", "oval", "kite"}
print(set)
for item in set:
    print(item)

status = {"Phy":98, "Chem":97, "Math":100}
print(status["Math"])
status["Bio"] = "NULL"
print(status)
print(status["Bio"])
status["Math"] = 99
print(status)

import math
print(dir(math))
from math import sqrt
print(sqrt(25))
from math import *
print(sqrt(25))
print(sin(1.56))
print(log(1))

def sum(first, second):
    print(first + second)
sum(1,2)
def sum(first, second=3):
    print(first + second)
sum(2)

