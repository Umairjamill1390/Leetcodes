## Thought Process
- Initially, I considered using nested loops to check each character, but that would result in an inefficient `O(N^2)` time complexity.
- I then shifted focus to a single pass approach, choosing `t` (the larger string) for comparison, as this would lead to a more efficient `O(N)` solution.
- The idea is to iterate through `t` and check for a subsequence match with `s`.

#### Here is my code
```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) < 1: return True
        i = 0 
        for each in t:
            if s[i] == each: 
                i += 1
                if i == len(s): return True
        return i == len(s)
```
