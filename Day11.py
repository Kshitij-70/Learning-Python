#Function without Parameters
def addton():
    num1=10
    num2=15
    total=num1+num2
    print(total)
addton()
#Function Returning a Value - Part 1
"""Functions return values using the return statement. If a function has no return statement, it returns None. Let us rewrite the above functions using return. From now on, we get a value from a function when we call the function and print it."""
def addton():
    num1=10
    num2=15
    total=num1+num2
    return total
print(addton())
"""
a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
def addition():
    c=a+b
    print(c)
addition()"""

"""Function with Parameters
In a function we can pass different data types(number, string, boolean, list, tuple, dictionary or set) as parameters.
Single Parameter: If our function takes a parameter we should call our function with an argument"""

def add(num):
    sum=num+10
    print(sum)
add(4)
def sq(x):
    sqare=x*x
    return(sqare)
print(sq(10))
def area_of_cicre(r):
    area=3.14*r*r
    return area
print(area_of_cicre(10))

def sum_of_no(n):
    total=0
    for i in range(n+1):
        total+=i
    return total
print(sum_of_no(10))
"""
Two Parameter: A function may or may not have a parameter or parameters. A function may also have two or more parameters. If our function takes parameters we should call it with arguments. Let us check a function with two parameters:"""
def fullname(fname,lname):
    fulname=fname+" "+lname
    return fulname
print(fullname("kshitij","koli"))

def sum_2no(num1,num2):
    sum=num1+num2
    return sum
print(sum_2no(10,29))

def calculate_age(current_year,birth_year):
    age=current_year-birth_year
    return age
print(calculate_age(current_year=2026,birth_year=2006))
print(calculate_age(2026,2006))

def even(n):
    evno=[]
    for i in range(n+1):
        if i%2==0:
            evno.append(i)
    return evno
print(even(15))

"""Function with Default Parameters
Sometimes we pass default values to parameters, when we invoke the function. If we do not pass arguments when calling the function, their default values will be used."""
def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh'))

"""Arbitrary Number of Arguments
If we do not know the number of arguments we pass to our function, we can create a function which can take arbitrary number of arguments by adding * before the parameter name."""
def sum_of_all_no(*args):
    total=0
    for i in args:
        total+=i
    return total
print(sum_of_all_no(2,3,5))

#Dictionary unpacking
def greeting(name,location):
    print("Hello im ",name," and i live in ",location)
mydict={"name":"Kshitij","location":"Pune"}
greeting(**mydict)

#Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(arg1,arg2):
    sum=arg1+arg2
    print(sum)
add_two_numbers(10,100)

#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    area=3.14*r*r
    print(area)
    return area
print(area_of_cicre(10))

#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    total=0
    for i in args:
        total+= i
    print(total)
add_all_nums(10,10,11)

#Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(C):
    F=(C*9/5)+32
    print(F)
convert_celsius_to_fahrenheit(8)

#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    Autumn=["September", "October","November"]
    Winter=["December", "January", "February"]
    Spring=["March","April","May"]
    Summer=["June","July","August"]
    if month in Autumn:
        print("Autumn")
    elif month in Winter:
        print("Winter")
    elif month in Spring:
        print("spring")
    elif month in Summer:
        print("Summer")
    else:
        print("Wrong input")
check_season("August")

#Write a function called calculate_slope which return the slope of a linear equation
#m = (y₂ - y₁)/(x₂ - x₁)
def calculate_slope(X,Y,x,y):
    slope=(y-Y)//(x-X)
    return slope
print(calculate_slope(2,1,4,7))

#Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a,b,c,x):
    eq=a*x**2 + b*x + c 
    print(eq)
solve_quadratic_eqn(6,17,12,10)

#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for i in lst:
        print(i)
print_list([1,9,3,8,5])

#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(arr):
    return arr[::-1]
print(reverse_list([1, 2, 3, 4, 5]))
def reverse(arr):
    return arr[::-1]
print(reverse_list(["A", "B", "C"])) 

#Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst):
    capitalized_list=[]
    for i in lst:
        capitalized_list.append(i.upper())
    print(capitalized_list)
capitalize_list_items(["ak","bc","mc"])
        
#Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(lsit):
    food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
    food_stuff.append(lsit)
    return food_stuff
print(add_item('Meat')) 

#Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(lsit):
    food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
    food_stuff.remove(lsit)
    return food_stuff
print(remove_item("Mango")) 

#Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(n):
    total=0
    for i in range(n+1):
        total+=i
    return total
print(sum_of_numbers(5))  
print(sum_of_numbers(10)) 
print(sum_of_numbers(100))

#Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(n):
    total=0
    for i in range(n+1):
        if i % 2 != 0:
            total+=i
    return total
print(sum_of_odds(5))  

#Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(n):
    total=0
    for i in range(n+1):
        if i%2==0:
            total+=i
    return total
print(sum_of_even(6))

#Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(n):
    odd=0
    even=0
    for i in range(n):
        if i%2==0:
            even+=1
        else:
            odd+=1
    print("The even no are:",even)
    print("The odd no are:",odd)          
(evens_and_odds(7))

#Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(wno):
    fact=1
    for i in range(1,wno+1):
        fact*=i
    return fact
print(factorial(5))

#Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(a):
    return not a
print(is_empty([]))

#Write a function called greet which takes a default argument, name. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.
def greet(name,msg="Hello"):
    print(f"{msg},{name}!")
greet("kshitj")

#Create a function called show_args to take an arbitrary number of named arguments and print their names and values.
def show_args(name,age,city):
    print("name:",name,"age:",age,"city:",city)
show_args(name="Alice", age=30, city="New York")