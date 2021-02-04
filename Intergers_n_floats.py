#abs return absolute = only positive numbers.. it removes the negative "-"
print(abs(-10))

#"//" always results in an interger or whole number instead of a float or decimanl.
print(10//3)

#this gives the remainder of a division
print(23%5)

# this returns the square of something
print(5**2)

#TYPE CASTING - converting intergers into strings
lesnombre = str(123)
print(lesnombre)
print(type(lesnombre))
#-- converting strings into intergers -- it's important to note Here
# that the string must be a string on number already.
lesmot = int("123")
print(lesmot)
print(type(lesmot))

#this is used in order to receive an input from the user
# input will ALWAYS GIVE AND  BE A STRING TYPE
#To turn it into an interger use the "int" function

reponse = input("how old are you? ")
print(reponse)
