def bubble_sort(arr: list[int]) -> None:
    """Bubble sort implementation
    Running time: O(n^2) | Omega(n)
    """
    swap_count = -1
    iteration_count = 0

    while swap_count != 0:
        swap_count = 0
        for i in range(0, len(arr) - 1 - iteration_count):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap_count += 1

def selection_sort(arr: list[int]) -> None:
    """Selection sort implementation
    Running time: O(n^2) | Omega(n^2)

    Although it still faster than Bubble Sort since Selection Sort
    doesn't have to swap elements so many times per iteration
    """
    for i in range(0, len(arr)):
        min = arr[i]
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < min:
                min = arr[j]
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


if __name__ == '__main__':
    import random as r

    arr = [r.randint(0, 1000) for x in range(5000)]
    print(arr)

    # bubble_sort(arr)
    selection_sort(arr)
    print(arr)
