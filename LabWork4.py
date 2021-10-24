# 4. Write a function that takes a number(>=10) as an input and return the digits of the number as a set.


def digits(n):
    digit_set = set()

    while n != 0:
        digit = n % 10
        digit_set.add(digit)
        n //= 10

    return digit_set


def main():
    while True:
        number = int(input("Enter a number (Greater than 10): "))
        if number >= 10:
            break

    print("\nThe digits are ", end="")
    print(digits(number))


if __name__ == "__main__":
    main()
