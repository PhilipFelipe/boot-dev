def subset_sum(nums, target):
    return find_subset_sum(nums, target, len(nums) - 1)


def find_subset_sum(nums, target, index):
    if target == 0:
        return True
    if index < 0 and target != 0:
        return False
    if nums[index] > target:
        return find_subset_sum(nums, target, index - 1)
    result = find_subset_sum(nums, target, index - 1)
    if result == True:
        return True
    result = find_subset_sum(nums, target - nums[index], index - 1)
    if result == True:
        return True
    return False


if __name__ == "__main__":
    print(subset_sum([1, 2, 3], 7))
