# 4. Write a function that takes a number(>=10) as an input and return the digits of the number as a set.


def digits(n):
    a = str(n)
    for i in a:
        print(i, end=", ")


def main():
    while True:
        number = int(input("Enter a number : "))
        if number >= 10:
            break

    print("\nThe digits are ", end="")
    digits(number)
    print("\b\b")


if __name__ == "__main__":
    main()
