import string
import random
letters = list(string.ascii_lowercase)
rlist  = []
key = 0
password = "empty"

# Index : Letter
# 0  : a,  1  : b,  2  : c,  3  : d, 4  : e, 5  : f, 6  : g, 7  : h, 8  : i, 9  : j, 10 : k
# 11 : l, 12 : m, 13 : n, 14 : o, 15 : p, 16 : q, 17 : r, 18 : s, 19 : t, 20 : u
# 21 : v, 22 : w, 23 : x, 24 : y, 25 : z


# Generate and print a random integer between 0 and 25 and add it to "rlist"
for _ in range(10):
    random_index = random.randint(0, 25)
    rlist.append(random_index)

#printing the random list
print(rlist)
ra_string = letters[rlist[1]]+letters[rlist[0]]+letters[rlist[8]]+letters[rlist[5]]+letters[rlist[7]]
print(" 0  : a,  1  : b,  2  : c,  3  : d, 4  : e, 5  : f, 6  : g, 7  : h, 8  : i, 9  : j, 10 : k")
print(" 11 : l, 12 : m, 13 : n, 14 : o, 15 : p, 16 : q, 17 : r, 18 : s, 19 : t, 20 : u")
print(" 21 : v, 22 : w, 23 : x, 24 : y, 25 : z")


while key == 0:
    password = str(input("script key?:"))
    if password == str(ra_string):
        key = 1
    else:
        key = 0
        print("lol try again buddy")


for i in range(1):
 print("script open")

#all hw scripts here:

script = str(input("what scipt do you want to run?:"))

if script == "print multiple fucks":
    for i in range(500):
        print("fuck")



