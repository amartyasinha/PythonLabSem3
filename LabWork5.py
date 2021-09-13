"""5. Write a function that finds the sum of the n terms of the following series. Import the factorial function
created in question 4.
    1–x^2/2!+x^4/4!–x^6/6!+...x^n/n!"""


from LabWork3 import factorial


def series_sum(x, n):
    store = 1
    for i in range(1, n):
        power = 2 * i
        store += ((x ** power) / factorial(power)) * ((-1) ** i)
    return store


def main():
    x = int(input("Enter the value of x : "))
    n = int(input("Enter the value of n : "))
    print("The sum of the series is : ", series_sum(x, n))


if __name__ == "__main__":
    main()
