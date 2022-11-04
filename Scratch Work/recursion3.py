name_list = [x.strip() for x in open("super_villains.txt").readlines()]

print(name_list)

def binary_search_nonrecursive(search_list, key):
    lower_bound = 0
    upper_bound = len(search_list) - 1
    found = False
    while lower_bound < upper_bound and found == False:
        middle_pos = (lower_bound + upper_bound) // 2
        if search_list[middle_pos] < key:
            lower_bound = middle_pos + 1
        elif search_list[middle_pos] > key:
            upper_bound = middle_pos
        else:
            found = True

    if found:
        print("The name is at position", middle_pos)
    else:
        print("The name was not in the list.")


binary_search_nonrecursive(name_list, "Morgiana the Shrew")


def binary_search_recursive(search_list, key, lower_bound, upper_bound):
    if lower_bound == upper_bound:
        print("Name not found.")
        return

    middle_pos = (lower_bound + upper_bound) // 2
    if search_list[middle_pos] < key:
        # Recursively search top half
        binary_search_recursive(search_list, key, middle_pos + 1, upper_bound)

    elif search_list[middle_pos] > key:
        # Recursively search bottom half
        binary_search_recursive(search_list, key, lower_bound, middle_pos)
    else:
        print("Found at position", middle_pos)


lower_bound = 0
upper_bound = len(name_list) - 1
binary_search_recursive(name_list, "Arachne the Gruesome", lower_bound, upper_bound)
