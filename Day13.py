nums=[1,2,3,4,5]
nu=[i**2 for i in nums]
print(nu)

even=[n%2==0 for n in nums]
print(even)

tvshows=["friends","ParKs and REINCARNATION","Sacred GAMES","rick and Morty","ONLY spider","BOYS"]
captv=[]
for show in tvshows:
    if len(show)>=10:
        showcap=show.title()
        captv.append(showcap)
print(captv)

cap_tv=[i.title() for i in tvshows if len(i)>=20]
print(cap_tv)

totalsq=[i**2 for i in range(1,11)]
print(totalsq)
#For instance if you want to change a string to a list of characters. You can use a couple of methods. Let's see some of them:
language = 'Python'
lst=list(language)
print(lst)
lstt=[i for i in language]
print(lstt)
#For instance if you want to generate a list of numbers
gen_no=[(i,i*2) for i in range(1,11)]
print(gen_no)

## Generating even numbers
even_no=[i for i in range(1,21) if i%2==0]
print(even_no)
## Generating odd numbers
odd_no=[i for i in range(1,21) if i%2!=0]
print(odd_no)

# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
filter=[i for i in numbers if i>0]
print(filter)

# Flattening a two dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [item for sublist in list_of_lists for item in sublist]
print(flattened_list)

x=lambda x: x**2
print(x(10))

def add_two_nums(a,b) :
    return a+b
print(add_two_nums(10,22))

add = lambda a,b:a+b
print(add(12,10))

#Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filter=[i for i in numbers if i<=0]
print(filter)

#Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Flatten=[i for sublst in list_of_lists for i in sublst]
print(Flatten)

#Using list comprehension create the following list of tuples:

[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]