# Problem Name

3. Longest Substring Without Repeating Characters

# Difficulty

Medium

# Pattern Used

Sliding Window (Two Pointers + Hash Set)

# Approach Explanation

### Brute Force

Generate every possible substring.

For each substring:

- Check whether all characters are unique.
- If they are, update the maximum length.

Since there are many possible substrings and each uniqueness check takes additional time, this approach is inefficient.

Time Complexity:

```text
O(n³)
```

Even with optimization using a set for checking duplicates, it still becomes:

```text
O(n²)
```

which is too slow for the given constraints.

---

### Optimal Approach (Used)

We use a **Sliding Window**.

Maintain two pointers:

```text
left
right
```

The window represents the current substring without repeating characters.

Also maintain a hash set:

```text
char_set
```

which stores every character currently inside the window.

Move `right` one character at a time.

If the new character already exists in the set:

- Remove characters from the left side.
- Move `left` forward.
- Continue until the duplicate is removed.

Then:

- Add the new character.
- Update the maximum window size.

---

### Why This Works

The window always contains unique characters.

Whenever a duplicate appears, we shrink the window just enough to remove the duplicate instead of restarting from scratch.

Each character:

- enters the window once
- leaves the window once

Therefore, the entire string is processed efficiently in one traversal.

---

### Why I Used This Pattern

Indicators:

- Need the **longest** valid substring.
- The substring must be **continuous**.
- Need to expand and shrink a range dynamically.
- Duplicate detection must be fast.

These are classic signs that the Sliding Window technique is appropriate.

Using a Hash Set allows duplicate checks in constant time.

---

### Could There Be A Better Version?

Current solution:

Time:

```text
O(n)
```

Space:

```text
O(min(n, m))
```

where `m` is the number of unique characters.

This is optimal.

Every character must be processed at least once.

---

### Alternative Version

Instead of a Hash Set, use a Hash Map.

The map stores:

```text
character -> last seen index
```

When a duplicate appears:

Move `left` directly to:

```text
last_seen + 1
```

instead of removing characters one by one.

Example:

```text
a b c a
      ^
```

Instead of shrinking step-by-step,

jump directly to:

```text
left = last_seen['a'] + 1
```

Complexities:

Time:

```text
O(n)
```

Space:

```text
O(min(n, m))
```

Why is it not used?

The Hash Set approach is simpler and easier to understand.

The Hash Map version is slightly more optimized because it avoids unnecessary removals.

---

### Walkthrough

Input:

```text
"abcabcbb"
```

Initially:

```text
Window = ""
left = 0
max_length = 0
```

Read:

```text
a
```

Window:

```text
"a"
```

Length:

```text
1
```

Read:

```text
b
```

Window:

```text
"ab"
```

Length:

```text
2
```

Read:

```text
c
```

Window:

```text
"abc"
```

Length:

```text
3
```

Read:

```text
a
```

Duplicate found.

Remove characters from the left until `a` is removed.

Window becomes:

```text
"bca"
```

Length remains:

```text
3
```

Continue similarly until the string ends.

Final answer:

```text
3
```

---

# Time Complexity

```text
O(n)
```

Reason:

Each character enters and leaves the sliding window at most once.

---

# Space Complexity

```text
O(min(n, m))
```

Reason:

The Hash Set stores only the unique characters currently inside the window.

---

# Key Learning Points

- Sliding Window is useful for contiguous subarray or substring problems.
- Hash Sets provide constant-time duplicate checking.
- Expand the window when valid.
- Shrink the window only when necessary.
- Every character is processed at most twice, leading to linear time complexity.

---

# Similar Problems

- Longest Repeating Character Replacement
- Minimum Window Substring
- Permutation in String
- Find All Anagrams in a String
- Maximum Erasure Value

---

# Interview Takeaway

Whenever a problem asks for:

```text
The longest or shortest contiguous substring/subarray satisfying a condition.
```

Think:

```text
Can I solve it using a Sliding Window?
```

If the condition involves checking duplicates or membership, combine the Sliding Window with a Hash Set or Hash Map for efficient lookups.