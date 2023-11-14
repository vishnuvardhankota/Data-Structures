def shell_sort(array):
    gap = len(array) // 2
    while gap > 0:
        for i in range(gap, len(array)):
            current_item = array[i]
            j = i
            while j >= gap and array[j - gap] > current_item:
                array[j] = array[j - gap]
                j -= gap
            array[j] = current_item
        gap //= 2

if __name__ == '__main__':

    numbers = [4,16,42,46,23,34,50,54,7,13,29,38]

    shell_sort(numbers)
    print(numbers)