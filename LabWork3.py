# 3. Write a Python function to find the nth term of Fibonacci sequence and its factorial. Return the result as a list.


def fibonacci(n):
    if n <= 0:
        print("Wrong input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):
    if n < 0:
        print("Wrong Input")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def return_fib_fact(n):
    fib = fibonacci(n)
    fact = factorial(fib)

    return [fib, fact]


def ordinal(number):
    if number == 1:
        return 'st'
    elif number == 2:
        return 'nd'
    elif number == 3:
        return 'rd'
    else:
        return 'th'


def main():
    number = int(input("Enter the positive number : "))
    term = fibonacci(number)

    [fib, fact] = return_fib_fact(number)

    print("\nThe {0}{1} number in the Fibonacci sequence is {2}".format(number, ordinal(number), fib))
    print("The factorial of {0} is {1}".format(fibonacci(number), fact))


if __name__ == "__main__":
    main()
