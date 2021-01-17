# Strings - 'the things with quotes around them'
# Store numbers you're not doing math on as a string

movie = 'TheGodFather'
print(movie)

Billy = '999-533-4455'
print(Billy)
print('_________________________________________')
# Store numbers you're not doing math on as a string

# todo : len() -> Number of characters in a string

str_test = 'Hello my name is megan'
print(len(str_test))
print('_________________________________________')

# todo: looping strings -> iterates through each char in the String
for letter in movie:
    print(letter)
print('_________________________________________')


# count = 0
# for letter in 'helper':
#     count = count + 1
# print(count)  # outside of loop
# print('_________________________________________')


def str_length(word):
#  word = input('Enter a word: ')
    count = 0
    for char in word:
        count = count + 1
    return count


print(str_length('Hello'))
print('_________________________________________')

# todo: string slicing

# Indexing
print('Orange'[3])
print('Orange'[-1]) # Reads from the right

# Searching for letters/ phrases
# [START:STOP:STEP]
print('Orange'[2:5])
print('Grapefruit'[2:-2])
