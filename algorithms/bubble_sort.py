# Bubble sort is simple to write, but is one of the slowest sorting algorithms
# It basically iterates over the nums and check if the previous element is greater than the current, if so, then it swap their values
# until there is no more swap to be made
def bubble_sort(nums):
    swapping = True
    end = len(nums)
    while swapping is True:
        swapping = False
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                temp = nums[i]
                nums[i] = nums[i - 1]
                nums[i - 1] = temp
                swapping = True
        end -= 1
    return nums


if __name__ == "__main__":
    arr = [1, 7, 3, 2, 5]
    print(bubble_sort(arr))
