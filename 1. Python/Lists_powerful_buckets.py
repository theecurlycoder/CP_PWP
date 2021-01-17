# Lists -> Like Arrays
# multiple data types
# Mutable (can be changed)

# lst = [2,3,4,5,5,6,8]

groceries = ['apple', 'banana', 'oranges']
print(groceries)

movies = ['Batman', 'X-Men', 'Dark Knight', 'Brother Bear']
print(movies)
print('_________________________________________')
# length of list
print(len(movies))
print('_________________________________________')
# Looping through the list
for movie in movies:
    print(movie)
print('_________________________________________')
# add to list
movies.append('Spiderman')
movies.append('Good Burger')

print(movies)
print(len(movies))
print('_________________________________________')
# Slicing ang indexing
print(movies[2])
print(movies[2:5])
