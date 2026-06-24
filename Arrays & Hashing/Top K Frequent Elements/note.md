# Problem Name

347. Top K Frequent Elements

# Difficulty

Medium

# Pattern Used

Hash Map + Bucket Sort

# Approach Explanation

### Brute Force

Count frequencies.

Example:

nums = [1,1,1,2,2,3]

Frequency Map:

{
    1: 3,
    2: 2,
    3: 1
}

Sort elements by frequency.

Result:

[(1,3), (2,2), (3,1)]

Take first k elements.

---

Why not use this?

Sorting requires:

O(m log m)

where:

m = number of unique elements

Although acceptable, the follow-up explicitly asks for a solution better than O(n log n).

---

### Better Approach (Heap)

Count frequencies using a Hash Map.

Maintain a Min Heap of size k.

For each unique element:

- Push frequency into heap.
- If heap size exceeds k, remove smallest.

Finally return heap elements.

Complexities:

Time:
O(n log k)

Space:
O(n)

This is a common interview solution.

---

### Optimal Approach (Used)

Use Bucket Sort.

Observation:

The maximum frequency of any number can never exceed n.

Therefore:

Instead of sorting frequencies,
place numbers into buckets.

Bucket Index = Frequency

Example:

nums = [1,1,1,2,2,3]

Frequency Map:

{
    1: 3,
    2: 2,
    3: 1
}

Buckets:

Index 1 → [3]
Index 2 → [2]
Index 3 → [1]

Visual:

bucket[1] = [3]
bucket[2] = [2]
bucket[3] = [1]

Now iterate backwards:

3 → 2 → 1

Collect numbers until k elements are found.

Return result.

---

### Why This Works

Frequency determines priority.

Instead of sorting all frequencies:

Store numbers directly at their frequency index.

Then process frequencies from largest to smallest.

This naturally gives elements in descending frequency order.

No sorting required.

---

### Why I Used This Pattern

Indicators:

- Need Top K elements.
- Frequency counting involved.
- Follow-up demands better than O(n log n).
- Maximum frequency is bounded by n.

Bucket Sort is ideal when:

- Keys represent frequencies.
- Frequency range is known.

This is one of the most important frequency-based interview patterns.

---

### Could There Be A Better Version?

Current Solution:

Time: O(n)

Space: O(n)

This is already optimal.

Reason:

Every element must be counted at least once.

Therefore:

O(n)

is the theoretical lower bound.

---

### Alternative Version (Heap)

Use:

Heapq

Complexities:

Time:

O(n log k)

Space:

O(n)

Advantages:

- Useful when k is very small.
- Common in production systems.

Disadvantages:

- Slower than Bucket Sort for this problem.

---

### Alternative Version (Sorting)

Use:

sorted(freq.items(), key=lambda x: x[1])

Complexities:

Time:

O(n log n)

Space:

O(n)

Advantages:

- Very simple.

Disadvantages:

- Violates follow-up requirement.

---

### Walkthrough

Input:

nums = [1,1,1,2,2,3]

k = 2

---

Step 1

Count frequencies:

{
    1: 3,
    2: 2,
    3: 1
}

---

Step 2

Build buckets:

bucket[1] = [3]
bucket[2] = [2]
bucket[3] = [1]

---

Step 3

Traverse backwards:

Frequency 3

result = [1]

---

Frequency 2

result = [1,2]

Length == k

Return:

[1,2]

# Time Complexity

O(n)

Reason:

1. Build frequency map → O(n)
2. Fill buckets → O(n)
3. Traverse buckets → O(n)

Total:

O(n)

# Space Complexity

O(n)

Reason:

Frequency map:

O(n)

Bucket array:

O(n)

Result:

O(k)

Overall:

O(n)

# Key Learning Points

- Top K problems often involve Heaps or Bucket Sort.
- Frequency counting is usually the first step.
- Bucket Sort becomes powerful when frequency range is bounded.
- Avoid sorting when only partial ordering is needed.
- Follow-up constraints often hint at the intended solution.

# Similar Problems

- Sort Characters By Frequency
- K Closest Points to Origin
- Find K Pairs With Smallest Sums
- Task Scheduler
- Frequency Sort

# Interview Takeaway

Whenever you see:

"Top K Frequent"

Think:

1. Count frequencies.
2. Consider Heap.
3. If frequency range is bounded, consider Bucket Sort.

For this problem:

Hash Map + Bucket Sort

is the optimal solution and satisfies the follow-up requirement of better than O(n log n).