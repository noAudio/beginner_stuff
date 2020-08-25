def fib(number):
    starting_number = 0
    previous_number = 1
    for i in range(number):
        yield starting_number
        temp = starting_number
        starting_number = previous_number
        previous_number += temp

for x in fib(20):
    print(x)