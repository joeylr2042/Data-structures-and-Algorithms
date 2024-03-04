def first_non_repeating_char(string):
    repeat_dict = {}

    for idx, item in enumerate(string):
        if item in repeat_dict.keys():
            repeat_dict[item] = None
        else:
            repeat_dict[item] = idx

    min_idx = 100000
    first_non_repeating_item = None
    for key, val in repeat_dict.items():
        if val is not None:
            if val < min_idx:
                min_idx = val
                first_non_repeating_item = key

    return first_non_repeating_item


print(first_non_repeating_char('leetcode'))

print(first_non_repeating_char('hello'))

print(first_non_repeating_char('aabbcc'))

"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""