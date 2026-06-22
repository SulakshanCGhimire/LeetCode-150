# Problem Name

49. Group Anagrams

# Difficulty

Medium

# Pattern Used

Hash Map + String Canonical Representation

# Approach Explanation

### Brute Force

For every word:

- Compare it with every other word.
- Check whether they are anagrams.
- If yes, place them in the same group.

Example:

["eat","tea","tan","ate","nat","bat"]

Compare:

eat ↔ tea
eat ↔ tan
eat ↔ ate
...

Why not use this?

- Too many comparisons.
- Checking every pair becomes expensive.
- Time Complexity can reach O(n² × k).

Where:
- n = number of strings
- k = average string length

---

### Optimal Approach (Used)

Create a unique key that is identical for all anagrams.

Observation:

Anagrams contain the same letters.

If we sort the letters:

eat → aet
tea → aet
ate → aet

All produce the same result.

Use the sorted string as the hash map key.

Example:

word = "eat"

key = "aet"

Store:

{
    "aet": ["eat"]
}

Next:

word = "tea"

key = "aet"

Store:

{
    "aet": ["eat", "tea"]
}

Continue for all words.

Finally return all groups.

---

### Why This Works

Anagrams contain exactly the same characters.

Sorting rearranges every anagram into the same canonical form.

Examples:

eat → aet
tea → aet
ate → aet

Since their sorted forms match,
they belong in the same group.

Hash Map allows us to instantly find the correct group.

---

### Why I Used This Pattern

Indicators:

- Need to group similar strings.
- Anagrams have identical character sets.
- Need efficient lookup and grouping.
- Hash Maps are ideal for categorization problems.

Pattern:

Hash Map + Generated Key

This pattern appears frequently in interview problems.

---

### Could There Be A Better Version?

Current Solution:

Time:
O(n × k log k)

Reason:

Each word must be sorted.

Sorting one word costs:

O(k log k)

For n words:

O(n × k log k)

---

### Better Version For Large Strings

Instead of sorting:

Create a frequency count of 26 letters.

Example:

eat

a = 1
e = 1
t = 1

Key:

(1,0,0,0,1,...)

tea

Produces exactly the same frequency tuple.

Use that tuple as the hash map key.

Advantages:

- No sorting required.
- Faster for long strings.

Complexities:

Time:
O(n × k)

Space:
O(n)

---

### Why Didn't We Use It?

The sorting solution is:

- Easier to understand.
- Easier to implement.
- Commonly accepted in interviews.

For very long strings,
the frequency-array approach is technically more optimal.

---

### Walkthrough

Input:

["eat","tea","tan","ate","nat","bat"]

Step 1:

eat → aet

{
    "aet": ["eat"]
}

---

Step 2:

tea → aet

{
    "aet": ["eat","tea"]
}

---

Step 3:

tan → ant

{
    "aet": ["eat","tea"],
    "ant": ["tan"]
}

---

Step 4:

ate → aet

{
    "aet": ["eat","tea","ate"],
    "ant": ["tan"]
}

---

Step 5:

nat → ant

{
    "aet": ["eat","tea","ate"],
    "ant": ["tan","nat"]
}

---

Step 6:

bat → abt

{
    "aet": ["eat","tea","ate"],
    "ant": ["tan","nat"],
    "abt": ["bat"]
}

Return:

[
    ["eat","tea","ate"],
    ["tan","nat"],
    ["bat"]
]

# Time Complexity

O(n × k log k)

Where:

n = number of strings

k = average string length

Reason:

Each word is sorted once.

# Space Complexity

O(n × k)

Reason:

Hash Map stores every string.

# Key Learning Points

- Grouping problems often use Hash Maps.
- Create a canonical representation (key).
- All anagrams share the same sorted form.
- Hash Map + Generated Key is a powerful pattern.
- Sometimes a frequency array can replace sorting.

# Similar Problems

- Valid Anagram
- Find All Anagrams in a String
- Group Shifted Strings
- Ransom Note
- Permutation in String

# Interview Takeaway

Whenever you see:

"Group strings that are equivalent under some transformation"

Think:

"Can I generate a unique key that represents each group?"

For anagrams:

Sorted string
or
Character frequency count

becomes the grouping key.

This is one of the most important Hash Map patterns for string problems.