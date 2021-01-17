# filter out movies with 7+ ratings
# each element in the list is a tuple (2D array)
my_movies = [('Interstellar', 10), ('Ironman', 8.2), ('I.T', 6.0), ('X-Men', 2.0)]
print(type(my_movies))
print(len(my_movies))
print(my_movies[0])
# 1st element of 1st item
print(my_movies[0][0])
print(my_movies[1][1])
print('_________________________________')


# Filter function

# plural arg name gives a list
def rating_filter(movies, max_rating):
    final_movies = []
    for movie in movies:
        if movie[1] >= max_rating:
            final_movies.append(movie[0])
    return final_movies


print(rating_filter(my_movies, 8))
