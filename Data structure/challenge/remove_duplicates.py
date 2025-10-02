
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item in lst:
            if item not in seen:
                seen.add(item)
                result.append(item)
    return result
print(remove_duplicates([1,2,2,3,1,4]))