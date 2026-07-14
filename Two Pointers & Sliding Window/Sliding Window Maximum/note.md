# Problem Name

239. Sliding Window Maximum

# Difficulty

Hard

# Pattern Used

Sliding Window + Monotonic Deque

# Approach Explanation

### Brute Force

For every window of size `k`:

- Traverse all `k` elements.
- Find the maximum.
- Store it in the answer.

Example:

```text
Window: [1,3,-1]

Maximum = 3
```

Then move the window one step and repeat.

Time Complexity:

```text
O(n × k)
```

When

```text
n = 100000
```

this becomes far too slow.

---

### Optimal Approach (Used)

Instead of recalculating the maximum for every window,

maintain a deque that always stores indices of elements in **decreasing order of their values**.

The deque satisfies two properties:

1.

```text
Front = Largest element in current window
```

2.

```text
Values inside deque remain in decreasing order.
```

For every new element:

- Remove smaller elements from the back.
- Insert the current index.
- Remove the front index if it leaves the window.
- Once the window reaches size `k`,
  the front of the deque is the maximum.

---

### Why This Works

Suppose the current number is larger than numbers behind it.

Example:

```text
Deque:

5 3 2

New value:

6
```

Neither

```text
5

3

2
```

can ever become the maximum again because

```text
6
```

is larger and will remain in the window longer.

Therefore they can safely be removed.

This guarantees that the deque always contains only useful candidates.

The front always stores the largest value in the current window.

---

### Why I Used This Pattern

Indicators:

- Need the maximum of every sliding window.
- Window size is fixed.
- Need better than O(n × k).
- Maximum changes dynamically.

A Monotonic Deque efficiently maintains the maximum element while the window slides.

This is the standard solution for sliding-window maximum problems.

---

### Could There Be A Better Version?

Current solution:

Time:

```text
O(n)
```

Space:

```text
O(k)
```

This is optimal.

Each index enters the deque once and leaves once.

---

### Alternative Version

Use a Max Heap (Priority Queue).

Steps:

- Push every element into the heap.
- Remove outdated elements whose indices are outside the window.
- The heap top gives the current maximum.

Complexities:

Time:

```text
O(n log k)
```

Space:

```text
O(k)
```

Why is it not used?

The heap performs extra logarithmic operations.

The Monotonic Deque achieves linear time, making it more efficient.

---

### Walkthrough

Input:

```text
nums = [1,3,-1,-3,5,3,6,7]

k = 3
```

Start:

```text
Deque = []
```

Insert:

```text
1

Deque:

[1]
```

Insert:

```text
3
```

Since

```text
3 > 1
```

remove

```text
1
```

Deque:

```text
[3]
```

Insert:

```text
-1
```

Deque:

```text
[3,-1]
```

First window:

```text
[1,3,-1]
```

Maximum:

```text
3
```

Slide window.

When

```text
5
```

arrives,

remove

```text
-3

-1

3
```

because they are smaller.

Deque becomes:

```text
[5]
```

Maximum:

```text
5
```

Continue until the end.

Final answer:

```text
[3,3,5,5,6,7]
```

---

# Time Complexity

```text
O(n)
```

Reason:

Each index is inserted into the deque once and removed at most once.

---

# Space Complexity

```text
O(k)
```

Reason:

The deque stores indices belonging to the current window.

At most `k` indices are stored.

---

# Key Learning Points

- A Monotonic Deque maintains elements in sorted order.
- Store indices instead of values to know when elements leave the window.
- Remove smaller elements from the back because they can never become future maximums.
- The front of the deque always represents the current window's maximum.
- Each element is processed only once, giving linear time complexity.

---

# Similar Problems

- Sliding Window Maximum II
- Minimum Window Substring
- Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
- Daily Temperatures
- Largest Rectangle in Histogram

---

# Interview Takeaway

Whenever a problem asks:

```text
Find the minimum or maximum for every fixed-size sliding window.
```

Think:

```text
Monotonic Deque
```

Instead of recomputing the maximum for every window, maintain a deque in decreasing order. This allows constant-time access to the current maximum while keeping the overall solution linear.