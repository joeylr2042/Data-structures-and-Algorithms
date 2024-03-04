def find_pairs(arr1, arr2, target):
    dif1 = [target - x for x in arr1]
    set1 = set(dif1)
    set2 = set(arr2)
    duplicates = list(set1.intersection(set2))
    res = [[target - x, x] for x in duplicates]
    return res


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print(pairs)

"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""
