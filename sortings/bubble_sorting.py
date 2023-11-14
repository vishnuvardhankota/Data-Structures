def bubble_sort(array):
  for i in range(len(array) - 1):
    for j in range(0, len(array) - i - 1):
      if array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j + 1], array[j]

  return array

if __name__ == '__main__':

    numbers = [7,3,8,14,5,34,16]
    sorted_array = bubble_sort(numbers)
    print(sorted_array)