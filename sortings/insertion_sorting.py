def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

if __name__ == '__main__':

    numbers = [7,4,12,9,24,6,15,34,21,3]
    sorted_array = insertion_sort(numbers)

    print(sorted_array)