# Frequency Word Counter

movies = {'Shawshank Redemption': 5.8, 'The God Father': 8.0}
print(movies)

# add elements to dictionary
movies['X-Men'] = 5.5
movies['Mad Max'] = 9.0
print(movies)

# length of dictionary
print(len(movies))

# Change dictionary value
movies['Mad Max'] = 3.0
print(movies)

# Unique keys (Cannot have 2 = keys)
# Unordered
sentence = 'whoop dee whoop scoop de scoop  Hey there what are you doing hey what'
final_answer = {
    'hey': 1,
    'Hey': 1,
    'what': 2,
    'are': 1,
    'you': 1,
    'doing': 1,
    'there': 1
}
print('_____________________________')
# .split() Method
print(sentence.split())
print(len(sentence.split()))
print('_____________________________')


def word_count(a_sentence):
    final_dict = {}
    for word in a_sentence.split():
        if word not in final_dict:
            final_dict[word] = 1
        else:
            final_dict[word] += 1

    return final_dict


print(word_count(sentence))
