# Problem Name

217. Contains Duplicate

# Difficulty

Easy

# Pattern Used

Hash Set

# Approach Explanation

### Brute Force

Compare every element with every other element.

Example:

nums = [1,2,3,1]

Compare:

1 with 2
1 with 3
1 with 1

Duplicate found.

Why not use this?

- Too many comparisons.
- Nested loops are expensive.

Time Complexity:

O(n²)

Not suitable for large inputs.

---

### Better Approach

Sort the array first.

Example:

[1,2,3,1]

After sorting:

[1,1,2,3]

Now check adjacent elements.

If two consecutive elements are equal,
a duplicate exists.

Time Complexity:

O(n log n)

Space Complexity:

O(1) or O(n) depending on sorting implementation.

Why not use it?

- Sorting changes the array order.
- Still slower than O(n).

---

### Optimal Approach (Used)

Use a Hash Set.

Idea:

A set only stores unique values.

For every number:

1. Check if it already exists in the set.
2. If yes, duplicate found → return True.
3. Otherwise add it to the set.

If traversal finishes without finding duplicates,
return False.

Example:

nums = [1,2,3,1]

Start:

seen = {}

---

num = 1

Not present.

seen = {1}

---

num = 2

Not present.

seen = {1,2}

---

num = 3

Not present.

seen = {1,2,3}

---

num = 1

Already exists.

Return True.

---

### Why This Works

A set guarantees uniqueness.

If a number appears again:

num in seen

will immediately return True.

Therefore the first repeated value confirms a duplicate exists.

---

### Why I Used This Pattern

Indicators:

- Need to detect repetition.
- Fast membership checking required.
- No need to store positions.
- Only existence matters.

Hash Sets provide:

- O(1) average insertion
- O(1) average lookup

making them ideal for duplicate detection.

---

### Could There Be A Better Version?

Current Solution:

Time: O(n)
Space: O(n)

This is already optimal.

Reason:

Every element must be inspected at least once.

Therefore:

O(n)

is the theoretical lower bound.

---

### Alternative One-Liner

return len(nums) != len(set(nums))

Explanation:

Sets remove duplicates automatically.

Example:

nums = [1,2,3,1]

len(nums) = 4

len(set(nums)) = 3

Since lengths differ,
duplicates exist.

Time Complexity:

O(n)

Space Complexity:

O(n)

---

### Why Didn't We Use It?

The explicit set approach:

- Demonstrates understanding.
- Easier to explain during interviews.
- Allows early termination.

Example:

[1,1,2,3,4]

Returns immediately after second element.

The one-liner still processes all elements.

---

### Walkthrough

Input:

nums = [1,2,3,1]

seen = {}

---

1 → add

seen = {1}

---

2 → add

seen = {1,2}

---

3 → add

seen = {1,2,3}

---

1 → already exists

Return True

# Time Complexity

O(n)

Reason:

Each element is visited once.

Set lookup and insertion:

O(1) average.

Total:

O(n)

# Space Complexity

O(n)

Reason:

In the worst case all elements are unique.

Set stores all n elements.

# Key Learning Points

- Hash Sets are perfect for duplicate detection.
- Membership checking is usually faster than repeated searching.
- If only uniqueness matters, prefer a Set over a Hash Map.
- Early termination can improve practical performance.
- Always consider whether positions are needed before choosing a data structure.

# Similar Problems

- Contains Duplicate II
- Contains Duplicate III
- Two Sum
- Longest Consecutive Sequence
- Happy Number

# Interview Takeaway

Whenever you see:

"Does any element repeat?"

Think:

"Can I use a Hash Set to track previously seen values?"

This is one of the most common and important Hash Set patterns in interviews.