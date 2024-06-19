def quick_sort(nums, low, high):
    if low < high:
        partition_index = partition(nums, low, high)
        # quick sorting left side
        quick_sort(nums, low, partition_index - 1)
        # quick sorting rigth side
        quick_sort(nums, partition_index + 1, high)
    return nums


def partition(nums, low, high):
    pivot = nums[high]
    i = low
    print("LOW: ", low, " | HIGH: ", high, " | PIVOT: ", pivot)
    for j in range(low, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    print("NEW NUMS[I]: ", nums[i], "| NEW NUMS[HIGH]: ", nums[high], "| NUMS: ", nums)
    print("RETURNING I: ", i)
    return i


if __name__ == "__main__":
    nums = [2, 1, 5, 7, 3, 9, 8]
    result = quick_sort(nums, 0, len(nums) - 1)
    print(result)
