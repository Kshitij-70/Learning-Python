"""fruits=("apple","mango","orange","banana","pineapple")
first=fruits[1]
last=fruits[-1]
print(first)
print(last)
fruit=list(fruits)
print(fruit)
print("kiwi" in fruits)
tpl2=("lichi","guava","grapes","lemon")
tpl3= tpl2 + fruits
print(tpl3)
#del tpl3"""
tpl = tuple()
print(tpl)
brothers=("Atharva","Durvas")
sisters=("Anjali","rashi")
siblings=brothers+sisters
print(siblings)
print(len(siblings))
mom="vidya"
dad="parmeshwar"
family_members=siblings + (mom,dad)
print(family_members)
parents=(mom,dad)
print(siblings)
print(parents)
#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits=("apple","mango")
vegis=("Palak","Ladyfinger","Tomato")
animals=("Lion","tiger")
food_stuff_tp=fruits+vegis+animals
print(food_stuff_tp)
#Change the about food_stuff_tp tuple to a food_stuff_lt list
print(list(food_stuff_tp))
#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(food_stuff_tp[3])
print(food_stuff_tp[len(food_stuff_tp)//2 -1 : len(food_stuff_tp)//2+1])
#Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_tp[:3])
print(food_stuff_tp[-3:])
#Delete the food_staff_tp tuple completely
del food_stuff_tp
#Check if an item exists in tuple:
"""Check if 'Estonia' is a nordic country
Check if 'Iceland' is a nordic country"""
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)