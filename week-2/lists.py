#Creating an empty list in python.
my_list = []

#Adding multiple items in the list using a for loop and append method.
other_list = [10,20,30,40,50]
for x in other_list:
    my_list.append(x)

#inserting an item in a specific index using the insert method.
my_list.insert(1,15)

#Taking another list and combining them with another with extent method.
other_list = [50, 60, 70]
my_list.extend(other_list)

#removing the last element in a list using te pop method which deletes the last index by default
my_list.pop()

#Sorting the items based on numbers from the lowest to highest.
my_list.sort()

#Checking the index of item inside a list using the index method.
my_list.index(30)
