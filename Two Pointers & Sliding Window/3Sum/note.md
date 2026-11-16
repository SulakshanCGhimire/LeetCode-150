# Problem Name

15. 3Sum

# Difficulty

Medium

# Pattern Used

Sorting + Two Pointers (Two Sum Variation)

# Approach Explanation

### Brute Force

Check every possible combination of three different indices.

For every combination:

- Calculate the sum of the three numbers.
- If the sum equals zero, add the triplet to the answer.
- Avoid adding duplicate triplets.

There are three nested loops involved.

Time Complexity:

```text
O(n³)
```

This is too slow for the given constraint:

```text
n <= 3000
```

Additionally, handling duplicate triplets makes the implementation more complicated.

---

### Better Approach (Hash Set)

Fix the first number and use a Hash Set to find the remaining two numbers.

For every index `i`:

- Create an empty Hash Set.
- Traverse the remaining elements.
- Calculate the required third number:

```text
target = -(nums[i] + nums[j])
```

- Check whether the target already exists in the set.
- If it does, a valid triplet is found.
- Use a set of sorted triplets to avoid duplicates.

Time Complexity:

```text
O(n²)
```

Space Complexity:

```text
O(n)
```

This is much better than brute force, but it requires additional memory and duplicate handling.

---

### Optimal Approach (Used)

First, sort the array.

Then fix one element using a loop:

```text
i
```

For the remaining two elements, use two pointers:

```text
left = i + 1

right = len(nums) - 1
```

Calculate:

```text
total = nums[i] + nums[left] + nums[right]
```

There are three possibilities:

**Case 1:**

```text
total < 0
```

The sum is too small.

Move:

```text
left += 1
```

Since the array is sorted, moving left forward increases the sum.

**Case 2:**

```text
total > 0
```

The sum is too large.

Move:

```text
right -= 1
```

Moving right backward decreases the sum.

**Case 3:**

```text
total == 0
```

We found a valid triplet.

- Add it to the result.
- Move both pointers.
- Skip duplicate values to avoid repeated triplets.

Also skip duplicate values for the fixed element `nums[i]`.

---

### Why This Works

Sorting gives us an important property:

```text
nums[left] <= nums[right]
```

Because the array is sorted, we can determine which pointer to move based on the current sum.

If the sum is too small, moving `left` forward is the only useful direction.

If the sum is too large, moving `right` backward is the useful direction.

This allows us to eliminate unnecessary combinations without checking every possible pair.

Duplicate skipping ensures that each unique triplet is added only once.

---

### Why I Used This Pattern

Indicators:

- Need to find three numbers satisfying a target sum.
- Duplicate triplets are not allowed.
- The order of elements inside a triplet does not matter.
- Sorting can simplify the search.
- After fixing one element, the remaining problem becomes Two Sum.

This is a classic **Sorting + Two Pointers** problem.

An important interview observation:

```text
3Sum = Fix one number + Solve Two Sum
```

Instead of using another nested loop, Two Pointers efficiently find the remaining pair.

---

### Could There Be A Better Version?

Current solution:

Time:

```text
O(n²)
```

Space:

```text
O(1)
```

Auxiliary space, excluding the output list.

Sorting takes:

```text
O(n log n)
```

The nested search takes:

```text
O(n²)
```

Therefore, the overall time complexity is:

```text
O(n log n + n²) = O(n²)
```

This is optimal for the standard 3Sum approach.

The main improvement over brute force is reducing the time complexity from O(n³) to O(n²).

---

### Alternative Version

Use a Hash Set instead of Two Pointers.

For every fixed element:

- Create a Hash Set.
- Traverse the remaining elements.
- Search for the required third value.
- Store valid triplets in a set to eliminate duplicates.

Time Complexity:

```text
O(n²)
```

Space Complexity:

```text
O(n)
```

Why is it not used?

Both approaches have the same asymptotic time complexity.

However, the Two Pointer approach:

- Uses less auxiliary space.
- Takes advantage of sorting.
- Handles duplicates more naturally.
- Is easier to reason about once the pointer movement is understood.

---

### Walkthrough

Input:

```text
nums = [-1,0,1,2,-1,-4]
```

First, sort the array:

```text
[-4,-1,-1,0,1,2]
```

Fix the first element:

```text
nums[i] = -4
```

Initially:

```text
left = 1

right = 5
```

Calculate:

```text
-4 + (-1) + 2 = -3
```

Sum is negative.

Move left forward.

Continue until the fixed element becomes:

```text
nums[i] = -1
```

Now:

```text
left = 2

right = 5
```

Calculate:

```text
-1 + (-1) + 2 = 0
```

Valid triplet:

```text
[-1,-1,2]
```

Move both pointers.

Next:

```text
left = 3

right = 4
```

Calculate:

```text
-1 + 0 + 1 = 0
```

Another valid triplet:

```text
[-1,0,1]
```

Move both pointers again.

The pointers meet, so this search ends.

The remaining fixed elements either produce no valid triplets or are skipped because they are duplicates.

Final result:

```text
[[-1,-1,2],[-1,0,1]]
```

---

# Time Complexity

```text
O(n²)
```

Reason:

- Sorting takes O(n log n).
- The outer loop runs O(n) times.
- For every iteration, the two pointers traverse the remaining array in O(n).

Therefore:

```text
O(n log n + n²) = O(n²)
```

---

# Space Complexity

```text
O(1)
```

Auxiliary space, excluding the output list.

Reason:

Only a few variables and pointers are maintained.

Note: Python's sorting implementation may use O(n) auxiliary space internally.

---

# Key Learning Points

- Sorting can simplify problems involving combinations and duplicate handling.
- Fixing one element can transform 3Sum into a Two Sum problem.
- Two Pointers eliminate unnecessary comparisons.
- If the sum is too small, move the left pointer forward.
- If the sum is too large, move the right pointer backward.
- Skip duplicate fixed elements and duplicate pointer values to avoid repeated triplets.
- Always consider whether sorting can make a brute-force solution more efficient.

---

# Similar Problems

- Two Sum
- Two Sum II - Input Array Is Sorted
- 3Sum Closest
- 4Sum
- Container With Most Water
- Remove Duplicates from Sorted Array

---

# Interview Takeaway

Whenever a problem asks:

```text
Find three numbers that satisfy a given sum.
```

Think:

```text
Sorting + Two Pointers
```

The key transformation is:

```text
3Sum

    ↓

Fix one element

    ↓

Find two remaining elements

    ↓

Two Sum using Two Pointers
```

Also remember that duplicate handling is an important part of this problem.

Skipping duplicate values at the fixed index and after finding a valid triplet ensures that every unique combination appears exactly once.

This reduces the brute-force O(n³) solution to an efficient O(n²) solution.