"""1. Write a function that takes the lengths of three sides: side1, side2 and side3 of the triangle as the input from
the user using input function and return the area and perimeter of the triangle as a tuple. Also, assert that sum of
the length of any two sides is greater than the third side"""


def triangle_area_perimeter(a, b, c):
    perimeter = a + b + c
    s = perimeter / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return (area, perimeter)


def main():
    side1 = float(input("Enter first side: "))
    side2 = float(input("Enter second side: "))
    side3 = float(input("Enter third side: "))

    assert (side1 > 0 and side2 > 0 and side3 > 0), "Sides cannot be zero or negative"
    assert ((side1 + side2) > side3 and (side1 + side3) > side2 and (side2 + side3) > side1), "Sum of any two sides " \
                                                                                              "of triangle must be " \
                                                                                              "greater than zero "
    (area, perimeter) = triangle_area_perimeter(side1, side2, side3)
    print("Area of the Triangle is {} sq. units".format(area))
    print("Perimeter of the Triangle is {} units".format(perimeter))


if __name__ == "__main__":
    main()
