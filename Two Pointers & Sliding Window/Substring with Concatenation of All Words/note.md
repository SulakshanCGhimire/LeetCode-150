# Problem Name

30. Substring with Concatenation of All Words

# Difficulty

Hard

# Pattern Used

Sliding Window + Hash Map (Word-Based Sliding Window)

# Approach Explanation

### Brute Force

For every possible starting position:

- Extract a substring whose length equals:

```text
len(words) × len(each_word)
```

- Divide the substring into equal-sized words.
- Count the frequency of each word.
- Compare it with the given list of words.

Although correct, this repeatedly rebuilds frequency maps for overlapping windows.

Time Complexity:

```text
O(n × number_of_words)
```

with significant repeated work.

---

### Optimal Approach (Used)

Notice that every word has the **same length**.

Instead of sliding one character at a time,

slide one **word** at a time.

Maintain:

```text
target
```

Frequency of the required words.

Maintain another map:

```text
window
```

Frequency of words inside the current window.

Since a valid substring can begin at different alignments,

perform the sliding window starting from:

```text
0

1

2

...

word_length - 1
```

For every extracted word:

- Add it into the window.
- If its frequency becomes too large,
  shrink the window from the left.
- If the number of matched words equals the required count,
  record the starting index.

If an invalid word appears,

clear the window and restart after that word.

---

### Why This Works

Every valid substring consists of complete words.

Instead of checking characters individually,

we process one word at a time.

Each word:

- enters the window once
- leaves the window once

The frequency maps ensure that every required word appears exactly the required number of times.

Trying every starting offset guarantees that every possible alignment is examined.

---

### Why I Used This Pattern

Indicators:

- Fixed-length words.
- Need to examine contiguous substrings.
- Word frequency matters.
- Repeated frequency calculations should be avoided.

This naturally leads to a **Sliding Window over words instead of characters**.

---

### Could There Be A Better Version?

Current solution:

Time:

```text
O(n × word_length)
```

Space:

```text
O(m)
```

where

```text
m
```

is the number of unique words.

This is considered the optimal approach.

Every word-sized block is processed only once for each alignment.

---

### Alternative Version

A straightforward solution is:

For every index:

- Build a new frequency map.
- Extract every word.
- Compare frequencies.

Complexities:

Time:

```text
O(n × number_of_words)
```

Space:

```text
O(m)
```

Why is it not used?

Most of the work is repeated because neighboring windows overlap heavily.

The Sliding Window reuses previous computations.

---

### Walkthrough

Input:

```text
s = "barfoothefoobarman"

words = ["foo","bar"]
```

Word length:

```text
3
```

Required frequency:

```text
bar : 1

foo : 1
```

Start from offset:

```text
0
```

Read:

```text
bar
```

Window:

```text
{bar:1}
```

Read:

```text
foo
```

Window:

```text
{bar:1, foo:1}
```

All required words found.

Record:

```text
0
```

Continue.

Later,

Window becomes:

```text
foo

bar
```

Again all frequencies match.

Record:

```text
9
```

Final answer:

```text
[0,9]
```

---

# Time Complexity

```text
O(n × word_length)
```

Reason:

There are `word_length` starting offsets.

For each offset, every word-sized block is processed at most once.

Overall, this is linear with respect to the input size.

---

# Space Complexity

```text
O(m)
```

Reason:

Two frequency maps store only the unique words.

---

# Key Learning Points

- Sliding Window can operate on words instead of characters.
- Equal-sized words make it possible to move the window in fixed jumps.
- Frequency maps efficiently verify whether all required words are present.
- Multiple starting offsets are necessary because valid words may begin at different positions.
- Reusing the existing window avoids rebuilding frequency maps repeatedly.

---

# Similar Problems

- Minimum Window Substring
- Find All Anagrams in a String
- Permutation in String
- Sliding Window Maximum
- Group Anagrams

---

# Interview Takeaway

Whenever a problem asks:

```text
Find substrings made by concatenating fixed-length words.
```

Think:

```text
Sliding Window over Words
```

Instead of processing individual characters, move the window one word at a time. Combine this with a frequency map to efficiently track required words, reducing repeated work and achieving an optimal solution.