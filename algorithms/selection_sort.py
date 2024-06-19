def selection_sort(nums):
    for i in range(len(nums)):
        smallest_idx = i
        for j in range(smallest_idx + 1, len(nums)):
            if nums[j] < nums[smallest_idx]:
                print(
                    "CURRENT IDX: ",
                    i,
                    "| SMALLEST_IDX: ",
                    smallest_idx,
                    "| INNER NUM: ",
                    nums[j],
                    "| SMALLEST IDX NUM: ",
                    nums[smallest_idx],
                )
                smallest_idx = j
        print("BEFORE SWAP: ", nums)
        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
        print("AFTER SWAP: ", nums)
    return nums


if __name__ == "__main__":
    nums = [2, 5, 1, 9, 8, 4]
    result = selection_sort(nums)
    print(result)
