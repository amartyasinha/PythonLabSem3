# 11. Write a menu-driven program to accept a list of student names and perform the following
# a. search an element using linear search / binary search.
# b. Sort the elements using bubble sort / insertion sort / selection sort

def linear_search(lst, element):
    for i in lst:
        if i == element:
            return True
    return False


def binary_search(lst, element):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) / 2
        if lst[mid] == element:
            return True
        elif lst[mid] < element:
            low = mid + 1
        elif lst[mid] > element:
            high = mid - 1
    return False


def bubble_sort(lst):
    for i in range(len(lst)):
        flag = False
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                (lst[j], lst[j + 1]) = (lst[j + 1], lst[j])
                flag = True
        if not flag:
            break
    return list


def insertion_sort(lst):
    for i in range(1, len(list)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j = j - 1
        lst[j + 1] = key
    return lst


def selection_sort(lst):
    size = len(lst)-1
    for x in range(0, size):
        min_idx = x
        for y in range(x+1, size):
            if lst[min_idx] > lst[y]:
                min_idx = y
        (lst[min_idx], lst[x]) = (lst[x], lst[min_idx])
    return lst


def main():
    print("Select your option from the list")
    print("1. Linear Search\n2. Binary Search\n3. Bubble Sort\n4. Insertion Sort\n5. Selection Sort\n")
    choice = int(input("Enter you choice: "))


if __name__ == '__main__':
    main()
