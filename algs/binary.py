import math

def search(arr: list[int], needle: int) -> int:    
    start = 0
    end = len(arr) - 1

    while (end - start) > 0:
        middle = math.floor((end + start) / 2)

        if arr[middle] == needle:
            return middle
    
        if arr[middle] > needle:
            end = middle
        else:
            start = middle + 1

    return -1

if __name__ == '__main__':
    arr1 = [0, 1, 2, 3, 4]
    print(arr1, 3, search(arr1, 3))
    print(arr1, 1, search(arr1, 1))
    print(arr1, 7, search(arr1, 7))