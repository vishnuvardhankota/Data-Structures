def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    less = [x for x in array[1:] if x <= pivot]
    high = [x for x in array[1:] if x > pivot]

    return quick_sort(less) + [pivot] + quick_sort(high)

if __name__ == '__main__':
    numbers = [7,4,12,9,24,6,15,34,21,3]

    sorted_array = quick_sort(numbers)
    print(sorted_array)