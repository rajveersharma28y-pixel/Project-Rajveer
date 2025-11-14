# Printing text
print("hello world")

# Basic math
x = 5
y = 7
print(x - y)
print(x + y)
print(x * y)
print(x / y)

# Variable types
x = 50
y = "rajveer"
print(x)
print(y)
print(type(x))
print(type(y))

# Float example
x = 7.3
print(type(x))

# Boolean and math
x = 5
y = 9
print(x + y)
print(type(x + y))
print(bool(x + y))

# Empty string is False
x = ""
print(bool(x))  # False

# Multiple assignment
x, y, z = "20", "30", "40"
print(x, y, z)
print(type(x))  # checking one type at a time

# Strings must be in quotes
x = "python"
print(x)

# String concatenation
x = "python"
y = "is"
z = "good"
print(x, y, z)
print(x + y + z)

# Function example
x = "good"

def my_function():
    print("python is " + x)

my_function()

# Lists
my_list = ["apple", "banana"]
print(type(my_list))
print(my_list)
print(len(my_list))

# Mixed list with Boolean
my_list = ["apple", "banana", 1, 3, True]
print(my_list)

# Access list elements
my_list = ["apple", "banana", "cherry", "sjc", "bsghjw", "gywwgyaaaaaaa"]
print(my_list[2:5])
print(my_list[-5:-2])

# Modify list
my_list = ["apple", "banana", "cherry", "sjc", "bdgdhej", "shhdgeb"]
my_list[1] = "mango"
print(my_list)


my_list = [1, 2, 3, 5, 6, 7, 8, 9, 10]

my_list.insert(3,4)
print(my_list)
my_list.append("apple")
print(my_list)
my_list.remove(1)
print(my_list)
list2 = ["anshu","tushar","ronak"]
my_list.extend(list2)
print(my_list)

list3 = []
list3.append(2)
print(list3)
list3[0]= "hello"
print(list3)


list4=[1,2,3,4,5,6]
for x in list4:
    print(x)
    list5=[1,2,3,4,5,5,5,6]
    for x in list5:
        print(x)


        #sort
        list6=[2,5,1,4,8]

        list6.sort()
        print(list6)


        list7=[2,5,1,4,8]
        list7.sort(reverse=True)
        print(list7)


        text="hello Python"
        print(text.upper())
        print(text.lower())
        print(text.strip())
        print(text.replace("Python","world"))
        print(text.split())




        x="bob"
        y=30
        print(f"my name is {x} and my age is {y}")


        x=5
        x+=3
        print(x)
        x=5
        x-=3
        print(x)
        x=5
        x*=3
        print(x)
        x=5
        x/=3
        print(x)

        x=10
        y=7
        print(x==y)
        print(x!=y)
        print(x>=y)
        print(x<=y)
        print(x>y)
        print(x<y)

        x=8
        y=x
        z=10
        print(y)
        print(z is x)

        colors = {"red","green","blue"}
        print(colors)
        colors.add("yellow")
        print(colors)

        colors.remove("green")
        print(colors)

        for color in colors:
            print(color)

            students={
                "name":"anshu",
                "age":30,
                "grades":"A"
            }
            print(students)

            students["age"]=21
            students["city"]="Delhi"
            print(students)

            #if else

            age=20
            if age>=18:
                print("you are adult")
            else:
                print("you are not adult")

                print("hello")


                print("hello")


print("x")
x=4
y=9
z=x*y
print(z)
print(z*2)


u=[13,5,36,4]
u.sort()
print(u)

u.append(8)
print(u)

list1=[0,4,7,5]
u.extend(list1)
print(u)

u.insert(3,5)
print(u)

print("anshu")

age= 17
if age>=18:
    print("you are adult")
else:
    print("ewww you are minor")
    
    marks=50
    if marks>50:
        print("have passed")
    elif marks==50:
        print("you got saved")
    else:
        print("falied")

        age=16
    if age>18:
        print("you are adult")
    elif age==17:
        print("you are teen")
    elif age==16:
        print("you are teen")
    elif age==15:
        print("you are teen")
    else:
        print("you are not adult")



    x=15
    if x>10:
        print("x is greater than 10")
        
        if x>20:
            print("x is greater than 20")
        else:
            print("x is not greater than 20")

            x=128
            
            if x%2==0:
                print("x is an even number")
            else:
                print("x is an odd number")\

                print("x")



            x= -19
            if x>0:
                    print("x is a positive no.")
            else:
                    print("x is a negative no.")


                    fruits = ["apple","banana","cherry"]

                    for fruit in fruits:
                        print(fruit)
                        
                        word="python"

                        for x in word:
                            print(x)



                        for i in range(5):
                            print(i)



                        for i in range(1,10,2):
                                print(i)



                        for i in range(7,14,3):
                            print(i)

                            '''wdhujuenjwnj'''


                            '''wdnbewgebhi'''


                            #x=15
                            #pri nt(x)


                    for i in range(1,4):
                        for j in range(1,3):
                            print(f"i={i},j={j}")



                    for i in range(1,6):
                        if i ==4:
                            break
                        print(i)

                        for i in range(1,4):
                            print(i)
                        else:
                                print("loop is finished")


                                for i in range(1,20):
                                    print(i)

                                for i in range(1,30):
                                    if i%2==0:
                                        print(i)


colors =["blue","green","yellow"]
for i in colors:
    print(i)




def greet():
     print("hello python!")
greet()


def greet(name):
    print(f"hello,{name}")
greet("alice")
greet("bob")

def add(a,b):
    return a+b
result=add(5,3)
print(result)

def add(a,b):
    return a+b
result=add(5,3)
print(result)

def subtract(a,b):
    return a-b
result=subtract(5,3)
print(result)

def multiply(a,b):
    return a*b
result=multiply(6,7)
print(result)


def greet(name="student"):
 print(f"hello,{name}!")
greet()
greet("Alice")


'''global'''

x=10
def my_func():
 y=5
 print("inside:",x,y)
my_func()
print("outside:",x)
print(y)


#greet
def greet():
     print("hello")
greet()

#add two no. and returns result

def add(a,b):
    return a+b
result=add(7,8)
print(result)


#class
class Car:
    def __init__(self,brand,color):
     self.brand=brand 
     self.color=color

    def drive(self):
     print(f"{self.color} {self.brand} is driving 🚗")


    #object
Car1=Car("BMW","Black")
Car2=Car("Tesla","white")


Car1.drive()
Car2.drive()


#Array

import array

#create an array of integers
numbers= array.array('i',[1,2,3,4,5])
print(numbers)

from numpy import random

x=random.randint(100)
print(x)



x=random.rand()
print(x)
print(type(x))

#1D array

x= random.randint(100,size=(5))
print(x)


#2D array

x=random.randint(100,size=(3,5))
print(x)

x=random.randint(100,size=(2,3,5))
print(x)

print("x")

x=random.randint(100,size=(2,2,3,5))
print(x)


x=random.choice([3,5,7,9])
print(x)



x=random.choice([3,5,7,9] , size=(5))
print(x)


x=random.choice([3,5,7,9] , size=(18))
print(x)


x=random.choice([3,5,7,9] , size=(1,3,8))
print(x)

#EXample-creating a series
import pandas as pd

data=[10,20,40]
s=pd.Series(data)
print(s)

#creating a dataframe

import pandas as pd 
data={
  "Name":["Alice","Bob","charlie","David"],
  "Age":[24,27,22,32],
  "city":["Delhi","Mumbai","Chennai","Kolkata"]
}
df=pd.DataFrame(data)
print(df)


#from a NumPy Array
import numpy as np
arr=np.array([1,2,3,4,5])
s=pd.Series(arr)
print(s)


#From a Dictionary
data={"Math":90,"science":85,"English":78}
s=pd.Series(data)
print(s)


#importing data forms

import pandas as pd
df = pd.read_csv("crocodile_dataset.csv")
print(df.head())
print(df.tail())












                                     


        