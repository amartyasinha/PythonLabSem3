import matplotlib.pyplot as plt
import math


def sine_curve():
    sine_values = [math.sin(math.radians(i)) for i in range(0, 361)]
    plt.plot(sine_values)
    plt.xlabel('Degree')
    plt.ylabel('Sine Values')
    plt.title('Sine Curve')
    plt.grid()
    plt.show()


def cosine_curve():
    cosine_values = [math.cos(math.radians(i)) for i in range(0, 361)]
    plt.plot(cosine_values)
    plt.xlabel('Degree')
    plt.ylabel('Cosine Values')
    plt.title('Cosine Curve')
    plt.grid()
    plt.show()


# def polynomial_curve():
#     polynomial_values = []
#     plt.plot(polynomial_values)
#     plt.xlabel('X Axis')
#     plt.ylabel('Y Axis')
#     plt.title('Polynomial Curve')
#     plt.axhline(0, color='black',linewidth=0.05)
#     plt.axvline(0, color='black',linewidth=0.05)
#     plt.show()
#
#
# def exponential_curve():
#     exponential_values = []
#     plt.plot(exponential_values)
#     plt.xlabel('Degree')
#     plt.ylabel('Exponential Values')
#     plt.title('Exponential Curve')
#     plt.axhline(0, color='black',linewidth=0.05)
#     plt.show()


if __name__ == '__main__':
    sine_curve()
    cosine_curve()
