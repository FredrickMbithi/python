# Counting occurrences
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Or better yet (use Counter!)
from collections import Counter
word_count = Counter(words)

# Dictionary as a cache/lookup (O(1) speed!)
user_lookup = {user.id: user for user in users}

# Merging dictionaries (Python 3.9+)
combined = dict1 | dict2