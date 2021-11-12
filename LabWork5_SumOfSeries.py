"""5. Write a function that finds the sum of the n terms of the following series. Import the factorial function
created in question 4.
    1–x^2/2!+x^4/4!–x^6/6!+...x^n/n!"""


from LabWork3_FiboFact import factorial


def series_sum(x, n):
    store = 1
    for i in range(1, n):
        store += ((x ** (2 * i)) / factorial(2 * i)) * ((-1) ** i)
    return store


def main():
    print("""This program is to calculate the sum of the following series
                1–x^2/2!+x^4/4!–x^6/6!+...x^n/n!""")
    x = int(input("Enter x : "))
    n = int(input("Enter n : "))
    assert(x > 0 and n > 0), "Cannot take Negative Input"

    print("The sum of the series is : ", series_sum(x, n))


if __name__ == "__main__":
    main()
