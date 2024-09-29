### Thought Process
1. The first step is to check the length of both strings. If the lengths differ, they cannot be anagrams, so we can immediately return false.
2. If the lengths are equal, the order of characters doesn't matter for an anagram. Therefore, we can sort both strings and compare them. If the sorted versions are identical, the strings are anagrams.

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        return sorted(s) == sorted(t)
```
