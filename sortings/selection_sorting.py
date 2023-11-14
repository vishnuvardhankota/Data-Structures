def selection_sort(array):
    size = len(array)
    for i in range(size - 1):
        min_index = i
        for j in range(min_index+1,size):
            if array[j] < array[min_index]:
                min_index = j
        if i != min_index:
            array[i], array[min_index] = array[min_index], array[i]

if __name__ == '__main__':

    numbers = [4,16,42,46,23,34,50,54,7,13,29,38]

    selection_sort(numbers)
    print(numbers)