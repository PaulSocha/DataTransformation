import py
import collections


user1 = ["(Name) JohnDoe", "(Age) 20", "(City) Ashtabula", "(Flags) NYN"]
user2 = ["Name:Jane Doe", "City:Kingsville, OH", "Flags:YNY"]
user3 = ["Name:Sally Jones", "Age:25", "City:Paris", "Flags:YYY"]

# build has table structure to index key value pair from string.
# split from " " between Key and Value

#Name -> UserName
#Age -> UserAge
#City -> UserCity
#Flags -> UserFlag

my_dict = dict()

# loop through the string array split strings in to key value pairs

for s in user1: 
    key, value = s.split(' ')
    if key in my_dict.keys(): 
        my_dict[key] += int(value)
        continue
    my_dict[key] = str(value)

# create function that print out stardard format

def print_inventory(my_dict):
    for index, user in my_dict.items(): 
        print("{}\t{}".format(index, user))


print_inventory(my_dict)


#Output records in standard output formate. 




