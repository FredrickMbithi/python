# Remove duplicates (instant)
unique = list(set(my_list))

# Check membership (SUPER fast)
allowed_users = {'alice', 'bob', 'charlie'}
if username in allowed_users:  # O(1) time!
    pass

# Set operations (powerful!)
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1 & set2  # Intersection: {2, 3}
set1 | set2  # Union: {1, 2, 3, 4}
set1 - set2  # Difference: {1}