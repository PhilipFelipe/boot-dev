def binary_search(target, arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        median = (low + high) // 2
        print(median)
        if arr[median] == target:
            return True
        elif arr[median] < target:
            low = median + 1
        else:
            high = median - 1
    return False


if __name__ == "__main__":
    print(binary_search(30, [3, 5, 15, 23, 30, 50]))
