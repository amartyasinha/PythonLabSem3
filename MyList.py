def input_list():
    size = int(input("Enter the size of the list:"))
    lst = list()

    for i in range(0, size):
        element = input()
        lst.append(element)

    return lst


def check_number_in_list(lst):
    for i in lst:
        if not (str(i).isdigit()):
            return False

    return True


def count_odd_values(lst):
    count = 0

    for i in lst:
        if i % 2 != 0:
            count += 1

    return count


def display_largest_string(lst):
    largest = lst[0]

    for i in range(len(lst)):
        if lst[i] > largest:
            largest = lst[i]

    return largest


def lst_rev(lst):
    rev_list = lst[::-1]

    return rev_list


def find_element(lst, ele):
    if ele in lst:
        return ele, " is found"

    return "Element not found"


def remove_element(lst, ele):
    if ele in lst:
        rem_lst = lst.remove(ele)
        return True

    else:
        return False


def sort_dec(lst):
    for i in range(0, len(lst)):
        lst[i] = eval(lst[i])

    lst.sort(reverse=True)


def common_members(lst1, lst2):
    lst = []

    for i in lst1:
        if i in lst2:
            lst.append(i)

    return lst
