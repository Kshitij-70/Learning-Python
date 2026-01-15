from statistics import *
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))

import math
print(math.pi)
print(math.sqrt(2))
print(math.pow(4,2))

import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

from random import *
print(random())
print(randint(100000,999999))

#Write a function which generates a six digit/character random_user_id.
import random
import string
def random_user_id():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))
print(random_user_id())

#Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
#print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form
from random import *
def rgb_color_gen():
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    return f"rgb({r},{g},{b})"
print(rgb_color_gen())
    
#Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
import random
def list_of_hexa_colors(n):
    hexacolor=[]
    char="0123456789abcdef"
    for _ in range(n):
        color = "#"+"".join(random.choice(char) for _ in range (6))
        hexacolor.append(color)
    return hexacolor
print(list_of_hexa_colors(7))

#Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(n):
    clr=[]
    for _ in range(n):
        r= randint(0,255)
        g=randint(0,255)
        b=randint(0,255)
        clr.append(f"rgb({r},{g},{b})")
    return clr
print(list_of_rgb_colors(5))

print("Hello")
#Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(name,n):
    type=["hexa","rgb"]
    hexacolor=[]
    char="0123456789abcdef"
    if "hexa" in type:
        for _ in range(n):
            col="#"+"".join(random.choice(char) for _ in range(6))
            hexacolor.append(col)
        return hexacolor
    elif "rgb" in type:
        clr=[]
        for _ in range(n):
            r=randint(0,255)
            g=randint(0,255)
            b=randint(0,255)
            clr.append(f"rgb({r},{g},{b})")
        return clr
print(generate_colors("hexa",7))

#Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lst):
    random.shuffle(lst)
    return(lst)
print(shuffle_list([10,11,23,12,43]))

#Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def array():
    return random.sample(range(10),7)
print((array()))