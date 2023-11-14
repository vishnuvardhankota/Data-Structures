

def linear_search(data,value_to_find):
    for i in range(len(data)):
        if data[i] == value_to_find:
            return i
    

  
def binary_search(data, value_to_find):
    lower_index = 0
    higher_index = len(data) - 1

    while higher_index >= lower_index:
        middle_index = (lower_index + higher_index) // 2

        if data[middle_index] == value_to_find:
            return middle_index
        
        if data[middle_index] < value_to_find:
            lower_index = middle_index + 1
        else:
            higher_index = middle_index -1
    return -1


if __name__ == '__main__':

    numbers = [4,9,11,17,21,25,29,32,38,43,47,49,51,55,60,64,71,76,80,90,95]
    
    value_to_find = 47
    
    ls = linear_search(numbers,value_to_find)
    print("From Linear search value index is {}".format(ls))

    bs = binary_search(numbers,value_to_find)
    print("From Binary search value index is {}".format(bs))