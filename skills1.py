# Things you should be able to do.

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    odd_list = []
    for item in some_list:
        if item % 2 == 1:
            odd_list.append(item)
    return odd_list

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    even_list = []
    for item in some_list:
        if item % 2 == 0:
            even_list.append(item)
    return even_list

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    long_word_list = []
    for string in word_list:
        if len(string) >= 4:
            long_word_list.append(string)
    return long_word_list

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    some_list.sort()
    return some_list[0]

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    some_list.sort(reverse=True)
    return some_list[0]

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    halvesies_list = []
    for item in some_list:
        half = float(item)/2
        halvesies_list.append(half)
    return halvesies_list

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    len_list = [] 
    for word in word_list:
        length = len(word)
        len_list.append(length)
    return len_list

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    total_so_far = 0
    for num in numbers:
        total_so_far += num
    return total_so_far

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    product_so_far = 1
    for num in numbers:
        product_so_far *= num
    return product_so_far

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    all_strings = ''
    for string in string_list:
        all_strings += string
    return all_strings

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    number_of_numbers = len(numbers)
    sum_of_numbers = sum_numbers(numbers)
    average_of_numbers = float(sum_of_numbers)/number_of_numbers
    return average_of_numbers





