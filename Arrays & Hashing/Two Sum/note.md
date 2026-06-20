# Problem Name
Two Sum

# Difficulty
Easy

# Pattern Used
Hash Map (Dictionary)

# Approach Explanation

### Brute Force

Check every possible pair of numbers and see if their sum equals the target.

Example:

for i in range(n):
    for j in range(i + 1, n):
        if nums[i] + nums[j] == target:
            return [i, j]

Why not use this?

- Requires checking many pairs.
- Time Complexity = O(n²)
- Fails the follow-up requirement.

---

### Optimal Approach (Used)

Use a Hash Map to store numbers we have already seen.

For each number:

1. Calculate the complement:
   complement = target - current_number

2. Check if complement already exists in the hash map.

3. If it exists:
   - We have found the two numbers.
   - Return their indices.

4. Otherwise:
   - Store current number and its index.

Example:

nums = [2,7,11,15]
target = 9

i = 0
num = 2
complement = 7

7 not found
store {2:0}

i = 1
num = 7
complement = 2

2 found in hashmap

return [0,1]

---

### Why This Works

For every number x:

target = x + y

If we already know y exists,
we immediately have the answer.

Hash maps provide O(1) average lookup time,
allowing us to find complements instantly.

---

### Why I Used This Pattern

Indicators that suggest Hash Map:

- Need fast lookup.
- Looking for a pair.
- Need to find complement values.
- Array is unsorted.
- Follow-up asks for better than O(n²).

Hash Maps are one of the most common interview tools for these situations.

---

### Could There Be A Better Version?

Not asymptotically.

Current:
- Time: O(n)
- Space: O(n)

Since every element must be examined at least once,
O(n) is the theoretical lower bound.

Possible Alternative:

Sort + Two Pointers

Time:
O(n log n)

Space:
O(1) or O(n)

Why not use it?

- Sorting destroys original indices.
- Slower than O(n).
- Requires extra bookkeeping.

Therefore Hash Map remains the best solution.

# Time Complexity

O(n)

Reason:

- Traverse array once.
- Hash Map lookup is O(1) average.

Total:
O(n)

# Space Complexity

O(n)

Reason:

- In worst case we store all numbers in the Hash Map.

# Key Learning Points

- Hash Maps are useful when fast lookups are needed.
- Complement-based thinking is a common interview pattern.
- Trading space for speed is often worthwhile.
- When asked for better than O(n²), think about lookup structures.
- Single-pass solutions are generally preferred.

# Similar Problems

- Contains Duplicate
- Two Sum II
- 3Sum
- 4Sum
- Subarray Sum Equals K
- Longest Consecutive Sequence

# Interview Takeaway

Whenever you see:

"Find two elements satisfying a condition"

Ask yourself:

"Can I store previously seen values in a Hash Map and look up the complement in O(1)?"

This thought process solves many array-based interview questions.