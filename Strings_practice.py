lalist = "Interstellar"
#this seperates the lalist, but only takes every other item from begining (0)
# to the sixth (6) item.

liste1 = lalist[0:6:2]
liste2 = lalist[6::2]
print(liste1)
print(liste2)

# This returns the id/location in the coputer of the item
print(id(lalist))
# this allows us to find which item is at a specific index
print(lalist.find("t"))
# Here we are adding the lenghts of both lists together
print(len(liste1) + len(liste2))
# This gives us what type of object it is
print(type(lalist))

greeting = "Hello there"
user = "mashur"
# Here we are adding the two strings together and puting a space in between
print(greeting +" " + user.capitalize())
# Here we wanted to split the list with "-"
print(greeting.split("-"))
# Here we are putting "-" between every itmes of the string.
print("-".join(user))
# Here we are printing the first list in all upper charaters
#then seperating them by a space
# then we are printing the first list in all lower charaters
print(greeting.upper() + " " + user.lower())


#price = 120
#print(f"today's stock is{price}")

# "\" this character is used for viewing purpose if you want to index a text in your code
# but not in the actual code/output
print("hi my name\
is roger\
I am cool")
# Here by using the "\n" it's like using the ENTER on the keypad and it index it in the return
print("hi my name\n is roger\n I am cool")
# Here by using the "\t" it's like using the TAB on the keypad and it indet it in the return
print("Hi\t my name is Roger")
