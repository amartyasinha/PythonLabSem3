import matplotlib.pyplot as plt


def histogram(lst):
    n_bin = [i for i in range(min(lst), max(lst) + 2)]
    plt.hist(lst, bins=n_bin, ec='grey', color='skyblue')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.title('Age Group of your Class')
    plt.show()


def main():
    lst = []
    n = int(input('Enter the total number of students: '))

    for i in range(0, n):
        ele = input('Enter the age of student [{}]: '.format(i+1))
        lst.append(int(ele))
    histogram(lst)


if __name__ == '__main__':
    main()
