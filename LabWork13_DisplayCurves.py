import matplotlib.pyplot as plt
import math


def sine_curve():
    sine_values = [math.sin(math.radians(i)) for i in range(0, 361)]
    plt.plot(sine_values)
    plt.xlabel('Degree')
    plt.ylabel('Sine Values')
    plt.title('Sine Curve')
    plt.axhline(0, color='black',linewidth=0.05)
    plt.show()


def cosine_curve():
    cosine_values = [math.cos(math.radians(i)) for i in range(0, 361)]
    plt.plot(cosine_values)
    plt.xlabel('Degree')
    plt.ylabel('Cosine Values')
    plt.title('Cosine Curve')
    plt.axhline(0, color='black',linewidth=0.05)
    plt.show()


# def polynomial_curve():
#
#
# def exponential_curve():


if __name__ == '__main__':
    sine_curve()
    cosine_curve()
