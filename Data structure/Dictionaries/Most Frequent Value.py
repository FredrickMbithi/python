from collections import Counter

def most_frequent_value(d):
    counts = Counter(d.values())
    return counts.most_common(1)[0][0]

grades = {"Alice": "A", "Bob": "B", "Charlie": "A"}
print(most_frequent_value(grades))  # 'A'
