def merge_sort(nums):
    if len(nums) < 2:
        return nums
    half = len(nums) // 2
    array_a = nums[:half]
    array_b = nums[half:]
    array_a = merge_sort(array_a)
    array_b = merge_sort(array_b)
    return merge(array_a, array_b)


def merge(first, second):
    final = []
    i, j = 0, 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    while i < len(first):
        final.append(first[i])
        i += 1
    while j < len(second):
        final.append(second[j])
        j += 1
    return final


if __name__ == "__main__":
    result = merge_sort([5, 2, 9, 1])
    print(result)
