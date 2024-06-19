nums = [10, 200, 3000, 5000, 4]

def median_followers(nums):
    nums.sort()
    elements_qty = len(nums)
    print((elements_qty + 1) / 2)
    if elements_qty % 2 == 0:
        first_el = nums[elements_qty / 2]
        second_el = nums[(elements_qty / 2) + 1]
        median = (first_el + second_el) / 2
    else:
        median = nums[(elements_qty + 1 / 2) - 1]
    return median

if __name__ == "__main__":
    a = [7, 4, 3, 100, 2343243, 343434, 1, 2, 32]
    a.sort()
    print(a)
    b = [10, 200, 3000, 5000, 4]
    b.sort()
    print(b)
    # print(median_followers(nums))
