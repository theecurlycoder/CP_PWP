# if/then statements

# boolean values
likes_pizza = True
likes_cats = False

print(True)
print(False)

is_john_killer = True
is_bob_killer = False

if is_bob_killer == True:
    print("Bob is the killer")

if is_john_killer == True:
    print("John is the killer")
print()

#Equality Operators

print(5 == 5)
print(5 > 5)
print(5 <= 5)
print('___________________________________')

x = -1

if x < 5:
    print('smaller than 5')
elif x == 10:
    print('equal to 10')
elif x > 15:
    print('greater than 15')
else:
    print('is it even a number?')

