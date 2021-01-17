# Sum the numbers in a list

_numbers = [2, 3, 4, 5, 6]



def sum_of_numbers(number):
    count = 0
    for number in _numbers:
        count = count + number
    return count


print(sum_of_numbers(_numbers))
