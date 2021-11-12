# 6.Consider a tuple t1 = {1,2,5,7,9,2,4,6,8,10}. Write a program to perform following operations:
# a) Print another tuple whose values are even numbers in the given tuple.
# b) Concatenate a tuple t2 = {11,13,15} with t1.
# c) Return maximum and minimum value from this tuple.

def even_num(t1):
    even_list = list()
    for i in t1:
        if i % 2 == 0:
            even_list.append(i)
        even_tuple = tuple(even_list)

    return even_tuple


def concat(t1, t2):
    t1 = t1 + t2
    return t1


def min_max(t1):
    minimum = min(t1)
    maximum = max(t1)

    return (minimum, maximum)


def main():
    t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
    t2 = (11, 13, 15)

    print("The even tuple is", even_num(t1))

    t1 = concat(t1, t2)
    print("The concatenated tuple is", t1)

    (minimum, maximum) = min_max(t1)
    print("The Minimum value is {0} and the Maximum value is {1}".format(minimum, maximum))


if __name__ == '__main__':
    main()
