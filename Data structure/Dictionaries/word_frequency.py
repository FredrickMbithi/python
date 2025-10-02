def word_frequency(s):
    words = s.split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq
print(word_frequency("hello word word word  hello")) # {'hello': 2, 'world': 1}

#alternative ways
def word_frequency(s):
    words = s.split()
    freq = {}
    for w in words:
        if w in freq:
            freq[w] = freq[w] +1
        else:
            freq[w] = 1
    return freq

#Method 2: Using defaultdict (cleaner)
from collections import defaultdict

def word_frequency(s):
    words = s.split()
    freq = defaultdict(int)  # Defaults to 0
    for w in words:
        freq[w] += 1
    return dict(freq)

#Method 3: Using Counter (easiest!)
from collections import Counter

def word_frequency(s):
    words = s.split()
    return dict(Counter(words))

# Or even simpler:
def word_frequency(s):
    return dict(Counter(s.split()))