#Challenge 3: Find Duplicates
#Given a list, return all duplicate elements.
numbers = [1,2,2,3,4,2,3,2,1,3]

#def find_duplicates(arr):
#    seen = set()          # keeps track of elements we’ve already seen
#    duplicates = set()    # keeps track of elements that appear more than once
    
#    for item in arr:
#        if item in seen:          # if we’ve seen it before → it’s a duplicate
#            duplicates.add(item)
#        else:
#            seen.add(item)        # if it’s the first time → add to seen
    
#    return list(duplicates)       # convert set to list for output

#print(find_duplicates(numbers))

#Using Counter
from collections import Counter
def find_duplicates(list):
    counts = Counter(list)
    return [item for item, count in counts.items() if count > 1]