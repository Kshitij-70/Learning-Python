"""try:
    print("10" + "5")
except:
    print('Something went wrong')

try:
    born=input("Enter when where you born :")
    age= 2026 - int(born)
    print(f"Your current age is {age}")
except TypeError:
    print("Something went wrong")


try:
    your_age=input("Enter age:") 
    if int(your_age) >=18:
        print("You can vote")
    else:
        print("You cant vote")
except:
    print("Somethig went wrong")"""

#Packing and Unpacking Arguments in Python
#Unpacking Lists
"""
* for tuples
** for dictionaries"""
def sum_of_no(a,b,c,d):
    return a+b+c+d
lst=[10,12,14,16]
print(sum_of_no(*lst))

numbers=range(10,21)
print(list(numbers))
arg=[10,21]
no=range(*arg)
print(no)

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin,sew,*rest=countries
print(fin,sew,rest)

#names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*first_five,est,rus=names
nordic_countries=first_five
es=est
ru=rus
print(nordic_countries)
print(es)
print(ru)