def merge_sort(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left,right,array)

def merge_two_sorted_lists(list_a, list_b,array):
    len_a = len(list_a)
    len_b = len(list_b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if list_a[i] <= list_b[j]:
            array[k] = list_a[i]
            k += 1
            i += 1
        else:
            array[k] = list_b[j]
            k += 1
            j += 1

    while i < len_a:
        array[k] = list_a[i]
        k += 1
        i += 1

    while j < len_b:
        array[k] = list_b[j]
        k += 1
        j += 1


if __name__ == '__main__':
    numbers = [4,16,42,46,23,34,50,54,7,13,29,38]

    merge_sort(numbers)

    print(numbers)