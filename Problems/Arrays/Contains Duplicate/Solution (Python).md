## Thought Process
1. My initial approach was to create a separate list and check if it matches the provided `nums` list.
2. However, using a `set` is more efficient, as it allows for faster lookup and ensures uniqueness.
####  **What is a Set:** 
>Sets in Python are a collection data type that is unordered, unchangeable, and indexed. They are similar to lists or dictionaries but with a key difference that they only contain unique elements and do not support duplicates.

### Solution
```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for each in nums:
            if each in my_set:
                return True
            my_set.add(each)
        return False 
```
