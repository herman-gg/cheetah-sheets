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


def merge_sort(arr: list[int]) -> list[int]:
    """Selection Sort implementation
    Running Time: O(n log n); Omega(n log n)
    """
    if len(arr) == 1:
        return arr

    middle_idx = len(arr) // 2
    left_part = arr[0:middle_idx]
    right_part = arr[middle_idx:]

    left = merge_sort(left_part)
    right = merge_sort(right_part)

    sorted_part = []
    left_counter = 0
    right_counter = 0
    for i in range(0, (len(left) + len(right))):
        if left_counter >= len(left):
            sorted_part.append(right[right_counter])
            right_counter += 1;
            continue
        if right_counter >= len(right):
            sorted_part.append(left[left_counter])
            left_counter += 1;
            continue

        left_el = left[left_counter]
        right_el = right[right_counter]

        if left_el < right_el:
            sorted_part.append(left_el)
            left_counter += 1;
        else:
            sorted_part.append(right_el)    
            right_counter += 1;
    return sorted_part


if __name__ == '__main__':
    import random as r

    arr = [r.randint(0, 1000) for x in range(5000)]
    print(f"arr len: {len(arr)}")

    # bubble_sort(arr)
    # print("Bubble Sorted!")

    # selection_sort(arr)
    # print("Selection Sorted!")

    arr_sorted = merge_sort(arr)
    print("Merge Sorted!", arr_sorted)
