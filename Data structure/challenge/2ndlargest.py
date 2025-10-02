#Second Largest Element
def second_largest(lst):
    unique = list(set(lst))  # remove duplicates
    unique.sort()
    return unique[-2] if len(unique) >= 2 else None

print(second_largest([5, 1, 5, 3, 9, 9]))  # 5

