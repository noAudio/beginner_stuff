def highest_even(a_list):
    even_numbers = []
    highest = 0

    for number in a_list:
        if not(number % 2):
            even_numbers.append(number)
    
    for even_number in even_numbers:
        if even_number > highest:
            highest = even_number

    return highest

print(highest_even([10, 2, 3, 4, 8, 11]))