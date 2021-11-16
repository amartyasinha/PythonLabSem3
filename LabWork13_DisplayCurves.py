import matplotlib.pyplot as plt
import numpy as np


def sine_curve():
    x = np.linspace(0, 360, endpoint=False)
    y = np.sin(np.radians(x))
    plt.plot(x, y)
    plt.xlabel('Degree')
    plt.ylabel('Sine Values')
    plt.title('Sine Curve')
    plt.grid()
    plt.show()


def cosine_curve():
    x = np.linspace(0, 360, endpoint=False)
    y = np.cos(np.radians(x))
    plt.plot(x, y)
    plt.xlabel('Degree')
    plt.ylabel('Cosine Values')
    plt.title('Cosine Curve')
    plt.grid()
    plt.show()


def polynomial_curve():
    size = int(input('Enter Size (2 for linear eq, 3 for quadratic, 4 for cubic, and so on): '))
    coefficients = []
    for i in range(size):
        coefficients.append(int(input('Enter Coefficient for x^{0}'.format(size-i-1))))
    print(type(np.array(coefficients)))
    poly_func = np.poly1d(coefficients)
    x = np.linspace(-10, 10, endpoint=True)
    y = poly_func(x)
    plt.plot(x, y)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend(['Curve of y = \n' + str(poly_func)])
    plt.title('Polynomial Function Curve')
    plt.grid()
    plt.show()


def exponential_curve():
    x = np.linspace(-2, 10, endpoint=False)
    y = np.exp(x)
    plt.plot(x, y)
    plt.xlabel('Degree')
    plt.ylabel('Exponential Values')
    plt.title('Exponential Curve')
    plt.grid()
    plt.show()


def main():
    choice = -1
    while choice != 5:
        choice = int(input("Choose from the followings:\n\t1. Sine Curve\n\t2. Cosine Curve\n\t3. Polynomial "
                           "Curve\n\t4. Exponential Curve\n\t5. Exit\nChoice: "))
        match choice:
            case 1:
                sine_curve()
            case 2:
                cosine_curve()
            case 3:
                polynomial_curve()
            case 4:
                exponential_curve()
            case 5:
                print('Exiting...')
            case _:
                print('Wrong Choice!')


if __name__ == '__main__':
    main()
