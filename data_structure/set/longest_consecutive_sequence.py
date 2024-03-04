def longest_consecutive_sequence(nums):
    nums_set = set(nums)
    sorted_nums = sorted(list(nums_set), reverse=True)

    dif = []
    for i in range(len(sorted_nums) - 1):
        dif.append(sorted_nums[i] - sorted_nums[i + 1])

    max_length = 0
    length = 0

    for i in range(len(dif)):
        if dif[i] == 1:
            length += 1
        else:
            if length != 0:
                length = 0
        if length > max_length:
            max_length = length

    return max_length + 1


print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))
