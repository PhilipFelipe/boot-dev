# My solution, by far the worst one, but somehow it works.
# Here I try to find the duplicates and remove by the index
# With the list of 'ones' example, It only worked when I reversed the main loop with [::-1], yet I do not understand correctly why :)
def my_remove_duplicates(nums):
    for num in nums[::-1]:
        count = 0
        for i, num_2 in enumerate(nums):
            if num == num_2:
                count += 1
                if count > 1:
                    nums.pop(i)
    return nums


# This is the solution gave by boot.dev, it is way efficient and faster than my solution
# It basically creates a new list and insert unique values in it by verifying if the current number is not in the list yet
def remove_duplicates(nums):
    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums


if __name__ == "__main__":
    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    print(my_remove_duplicates(nums))
    print(remove_duplicates(nums))
