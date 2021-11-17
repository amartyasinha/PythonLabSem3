# 11. Write a menu-driven program to accept a list of student names and perform the following
# a. search an element using linear search / binary search.
# b. Sort the elements using bubble sort / insertion sort / selection sort

def linear_search(lst, element):
    for i in lst:
        if i == element:
            return True
    return False


def binary_search(lst, element):
    beg = 0
    end = len(lst) - 1
    while beg <= end:
        mid = (beg + end) // 2
        if lst[mid] == element:
            return mid
        elif element < lst[mid]:
            end = mid - 1
        else:
            beg = mid + 1
    return -1


def bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                (lst[j], lst[j + 1]) = (lst[j + 1], lst[j])
    return list


def insertion_sort(lst):
    for i in range(1, len(lst)):
        x = lst[i]
        j = i - 1
        while j >= 0 and x < lst[j]:
            lst[j + 1] = lst[j]
            j = j - 1
        lst[j + 1] = x
    return lst


def selection_sort(lst):
    size = len(lst)-1
    for x in range(size):
        min_idx = x
        for y in range(x+1, size):
            if lst[min_idx] > lst[y]:
                min_idx = y
        (lst[min_idx], lst[x]) = (lst[x], lst[min_idx])
    return lst


def main():
    lst = []
    ele = '-'
    while ele != '':
        ele = input('Enter the name (ENTER to quit): ')
        if ele != '':
            lst.append(ele)

    while True:
        print("Choose your option from the list")
        print("0. Exit\n1. Linear Search\n2. Binary Search\n3. Bubble Sort\n4. Insertion Sort\n5. Selection Sort\n")
        choice = int(input("Enter you choice: "))

        match choice:
            case 1:
                print(lst)
                key = input('Enter key to search: ')
                if linear_search(lst, key):
                    print('{} is found.'.format(key))
                else:
                    print('{} is not found.'.format(key))

            case 2:
                print(lst)
                key = input('Enter key to search: ')
                index = binary_search(lst, key)
                if index != -1:
                    print('{} is found at index {}.'.format(key, index))
                else:
                    print('{} is not found'.format(key))
            case 3:
                print('List before sorting: {}'.format(lst))
                bubble_sort(lst)
                print('List after sorting: {}'.format(lst))
            case 4:
                print('List before sorting: {}'.format(lst))
                insertion_sort(lst)
                print('List after sorting: {}'.format(lst))
            case 5:
                print('List before sorting: {}'.format(lst))
                selection_sort(lst)
                print('List after sorting: {}'.format(lst))
            case 0:
                exit(0)
            case _:
                print('Invalid choice - please refer to list')


if __name__ == '__main__':
    main()
