# Problem Name
Valid Anagram

# Difficulty
Easy

# Pattern Used
Frequency Counting (Hash Map)

# Approach Explanation

### Brute Force

Sort both strings and compare them.

Example:

s = "anagram"
t = "nagaram"

sorted(s) = "aaagmnr"
sorted(t) = "aaagmnr"

Return True

Why not use this?

- Sorting takes O(n log n).
- There is a more efficient linear-time solution.

---

### Optimal Approach (Used)

Count how many times each character appears in both strings.

If both frequency counts are identical,
the strings are anagrams.

Example:

s = "anagram"

Frequency:

a → 3
n → 1
g → 1
r → 1
m → 1

t = "nagaram"

Frequency:

n → 1
a → 3
g → 1
r → 1
m → 1

Both frequency maps are identical.

Return True.

---

### Why This Works

An anagram must contain:

- The same characters
- The same number of occurrences of each character

Order does not matter.

Therefore comparing character frequencies is sufficient.

---

### Why I Used This Pattern

Indicators that suggest Frequency Counting:

- Comparing character occurrences.
- Order of characters is irrelevant.
- Need to verify whether two strings contain identical elements.
- Hash maps provide efficient counting.

This is one of the most common string interview patterns.

---

### Could There Be A Better Version?

Current Solution:

Time: O(n)
Space: O(n)

For this problem's constraints, this is already optimal.

---

### Alternative Version (Lower Space)

Since the problem states:

- Only lowercase English letters

We can use an array of size 26.

Example:

count = [0] * 26

Increment for s.
Decrement for t.

If all values become zero,
the strings are anagrams.

Complexities:

Time: O(n)
Space: O(1)

Why not use it here?

- Less readable.
- Counter is cleaner and easier to explain in interviews.

However, the 26-array approach is technically more optimized.

---

### Walkthrough

Input:

s = "rat"
t = "car"

Frequency of s:

r → 1
a → 1
t → 1

Frequency of t:

c → 1
a → 1
r → 1

Maps differ because:

t exists in s but not in t
c exists in t but not in s

Return False.

# Time Complexity

O(n)

Reason:

- Counter traverses each string once.

Total:
O(n)

# Space Complexity

O(n)

Reason:

- Hash map stores character frequencies.

# Key Learning Points

- Frequency counting is a powerful string technique.
- When order does not matter, think about counts instead of positions.
- Hash maps are excellent for counting occurrences.
- Always look for constraints that allow fixed-size arrays.
- Character frequency comparison appears frequently in interviews.

# Similar Problems

- Group Anagrams
- Find All Anagrams in a String
- Ransom Note
- Permutation in String
- First Unique Character in a String

# Interview Takeaway

Whenever you see:

"Do two strings contain the same characters?"

Think:

"Can I compare character frequencies?"

Frequency counting is usually the simplest and most efficient solution.