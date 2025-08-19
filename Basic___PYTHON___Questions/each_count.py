

from collections import Counter

arr = [1, 2, 2, 3, 1, 4, 2, 3]
freq = Counter(arr)
print(freq)
# Output: Counter({2: 3, 1: 2, 3: 2, 4: 1})

# Access like a dictionary
print(freq[2])  # 3