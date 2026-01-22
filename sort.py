def sort_nums(nums: list[int]) -> list[int]:
    n = len(nums)
    for i in range(n):
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

number = [3, 2, 5, 1, 0]
print(sort_nums(number))
