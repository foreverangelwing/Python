def sum_of_list(numbers):
    sum_number = 0
    for num in numbers:
        sum_number += num
    return sum_number 
numbers = sum_of_list([1, 2, 3])
print(numbers)

def sum_of_list(numbers):
    return sum(numbers)
print(sum_of_list([1, 2, 3]))