# FizzBuzz: loop through every number from 1 to 100.
# The rule is: Fizz for multiples of 3, Buzz for multiples of 5,
# FizzBuzz for multiples of both, and the number itself for everything else.

for number in range(1, 101):   # range(1, 101) gives 1 through 100 inclusive

    # Check the combined condition FIRST.
    # If we checked 'divisible by 3' first, a multiple of both (e.g. 15)
    # would print "Fizz" and never reach the FizzBuzz branch.
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    # The % (modulo) operator returns the remainder after division.
    # If the remainder is 0, the number divides evenly — i.e. it's a multiple.
    elif number % 3 == 0:
        print("Fizz")

    elif number % 5 == 0:
        print("Buzz")

    else:
        # The number is not a multiple of 3 or 5, so just print it as-is.
        print(number)
