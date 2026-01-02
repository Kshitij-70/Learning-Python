#Day 3 - Operators
#1) Assignment Operators : =, +=, -=, 
"""
2)Arithmetic Operators:
Addition(+): a + b
Subtraction(-): a - b
Multiplication(*): a * b
Division(/): a / b
Modulus(%): a % b
Floor division(//): a // b
Exponentiation(**): a ** b"""

a=10
b=5
total=a+b
diff=a-b
product=a*b
div=a/b
remainder=a%b
floor_div=a//b
exponential= a**b
print(total)
print(diff)
print(product)
print(div)
print(remainder)
print(floor_div)
print(exponential)
#calculating area of circle
"""radius=int(input("Enter the radius:"))
area_of_circle=3.14*radius**2
print("Area of circle for radius",radius,"is :",area_of_circle)"""
# Calculating area of a rectangle
"""length=int(input("Enter the length:"))
width=int(input("Enter the Width:"))
area_of_rectangle=length*width
print(area_of_rectangle)"""

#3)Comparison Operators ==, !=, <, >, <=, >=
print(4 is 2*2)
print(4 is not 2*1)
print("a" in "apple")
print("a" not in "king")

#4)Logical Operators (and, or and not)
print(3 > 2 and 4 < 3) 
print('True and True: ', True and True)
print(3 > 2 or 4 > 3) 
print(3 < 2 or 4 < 3)
print('True or False:', True or False)
print(not 3 > 2)  
print(not not False)

# Exercises - Day 3
#Declare your age as integer variable
age=19
print(age)
#Declare your height as a float variable
height=5.6
print(height)
#Declare a variable that store a complex number
complx=1+2j
print(complx)
#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
"""base=int(input("Enter the base:"))
height=int(input("Enter the height:"))
areaoftriangle=0.5*base*height
print("The area of the triangle is :",areaoftriangle)"""
#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
"""side_a=int(input("Entre side a:"))
side_b=int(input("Entre side b:"))
side_c=int(input("Entre side c:"))
perimeter=side_a+side_b+side_c
print("The perimeter of the triangle is ",perimeter)"""
#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
"""length=int(input("Entre the length:"))
width=int(input("Entre the width:"))
area=length*width
perimeter=2*(length+width)
print(area)
print(perimeter)"""
#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius=int(input("Enter the radius:"))
area=3.14*radius**2
circumference=2*3.14*radius
print(area)
print(circumference)


#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len("Python") > len("Dragon"))
#Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("on" in "python" and "on" in "dragon")
#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("jargon" in "I hope this course is not full of jargon")
#Find the length of the text python and convert the value to float and convert it to string
text="Python"
print(len(text))
print(float(len(text)))
print(str(len(text)))
#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7//3 == int(2.7)) 
#Check if type of '10' is equal to type of 10
print(type('10')==type)
