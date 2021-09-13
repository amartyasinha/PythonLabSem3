"""1.Write a function that takes the lengths of three sides: side1, side2 and side3 of the triangle as the
input from the user using input function and return the area and perimeter of the triangle as a tuple. Also,
assert that sum of the length of any two sides is greater than the third side"""


def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area


def side_verification(a, b, c):
    if a + b >= c and b + c >= a and c + a >= b:
        return True
    else:
        return False


def usr_input():
    side1, side2, side3 = 0, 0, 0
    data_type_verify = False
    while not data_type_verify:
        side1 = input("Enter first side: ")
        try:
            side1 = float(side1)
            data_type_verify = True
        except:
            print("Enter Numeric value only")

    data_type_verify = False
    while not data_type_verify:
        side2 = input("Enter second side: ")
        try:
            side2 = float(side2)
            data_type_verify = True
        except:
            print("Enter Numeric value only")

    data_type_verify = False
    while not data_type_verify:
        side3 = input("Enter third side: ")
        try:
            side3 = float(side3)
            data_type_verify = True
        except:
            print("Enter Numeric value only")

    if side_verification(side1, side2, side3):
        print("The required area is %0.2f sq. units" % triangle_area(side1, side2, side3))
    else:
        print("Sides are not correct")


if __name__ == "__main__":
    usr_input()
