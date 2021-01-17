# Find the maximum number in a list
#  return max(numbers) --> Using Max Function
lst_nums = [23, 45, 67, 35, 89, 999, 4, 467]


def max_num(numbers):
    biggest_num = numbers[0]
    for current_num in numbers:
        if current_num > biggest_num:
            biggest_num = current_num
    return biggest_num


print(max_num(lst_nums))

def min_num(numbers):
    mini = numbers[0]
    for num in numbers:
        if num < mini:
            mini = num
    return mini

print(min_num(lst_nums))

