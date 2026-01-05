"""There are four collection data types in Python :
List: is a collection which is ordered and changeable(modifiable). Allows duplicate members. Can have items of different data types
Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members."""

lst=["apple","banana","cherrie","mango","pineapple","lemon","oranges"]
print(lst)
print(len(lst))
print(lst[-1])
print(lst[0])
print(lst[0:6:3])
fruits=lst[0:2]
print(fruits)
exist="Mango" in lst
print(exist)
#To add item to the end of an existing list we use the method append().
lst.append("grapes")
print(lst)
#We can use insert() method to insert a single item at a specified index in a list. Note that other items are shifted to the right. The insert() methods takes two arguments:index and an item to insert.
lst.insert(2,"kiwi")
print(lst)
#The remove method removes a specified item from a list
lst.remove("lemon")
print(lst)
#Removing Items Using : pop() method removes the specified index, (or the last item if index is not specified)
lst.pop(3)
print(lst)
#Removing Items Using Del. The del keyword removes the specified index and it can also be used to delete items within index range. It can also delete the list completely
del lst[1]
print(lst)
#The clear() method empties the list:
#lst.clear()
#print(lst)
lst.sort()      #ascending
print(lst)
lst.sort(reverse=1)     #descending
print(lst)
#sorted(): returns the ordered list without modifying the original list 
print(sorted(lst))

#Exercises: Level 1

#Declare an empty list
ls=[]
#Declare a list with more than 5 items
ls=["pen","scale","eraser","ink","book"]
#Find the length of your list
print(len(ls))
#Get the first item, the middle item and the last item of the list
print(ls[0::2])
#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types=["KP",20,5.6,"Unmarried","Talegaon"]
#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
#Print the list using print()
print(it_companies)
print(mixed_data_types)
#Print the number of companies in the list
print(len(it_companies))
#Print the first, middle and last company
print(it_companies[0::3])
#Print the list after modifying one of the companies
it_companies[0]="TCS"
print(it_companies)
#Add an IT company to it_companies
it_companies.append("Infosys")
print(it_companies)
#Insert an IT company in the middle of the companies list
it_companies.insert(4,"Meta")
print(it_companies)
#Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1]="GOOGLE"
print(it_companies)
#  Join the it_companies with a string '#;  '
kill=['#; ']
print(it_companies+kill)
#Check if a certain company exists in the it_companies list.
chk="Apple" in it_companies
print(chk)
#Sort the list using sort() method
it_companies.sort()
print(it_companies)
#Reverse the list in descending order using reverse() method
it_companies.sort(reverse=1)
print(it_companies)
#Slice out the first 3 companies from the list
print(it_companies[0:3])
#Slice out the last 3 companies from the list
print(it_companies[6:])
#Slice out the middle IT company or companies from the list
print(it_companies[4])
#Remove the first IT company from the list
del it_companies[0]
print(it_companies)
#Remove the middle IT company or companies from the list
del it_companies[4]
print(it_companies)
#Remove the last IT company from the list
del it_companies[-1]
print(it_companies)
#Remove all IT companies from the list
it_companies.clear()
print(it_companies)
#Destroy the IT companies list
del it_companies
#Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full=front_end+back_end
print(full)
#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack=full.copy()
print(full_stack)
full_stack.insert(5,"Python")
full_stack.insert(5,"SQL")
print(full_stack)

#Exercises: Level 2

#The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Sort the list and find the min and max age
ages.sort()
print(ages)
min_age=min(ages)
max_age=max(ages)
print(min_age,max_age)
#Add min and max age again to the list
ages.append(min_age)
ages.append(max_age)
ages.sort()
print(ages)
#Find the median age (one middle item or two middle items divided by two)
n=len(ages)
median=(ages[n//2-1] + ages[n//2])/2
print(int(median))
#Find the average age (sum of all items divided by their number )
avg=sum(ages)/len(ages)
print(avg)
# Find the range of the ages
ages.sort()
print(ages)
range=ages[-1] - ages[0]
print(range)

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
n=len(countries)
middle=countries[n//2]
print(middle)