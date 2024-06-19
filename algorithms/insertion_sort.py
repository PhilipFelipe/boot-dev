def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            print(j)
            j -= 1
    return nums


if __name__ == "__main__":
    print(insertion_sort([3, 9, 1, 7, 5]))
