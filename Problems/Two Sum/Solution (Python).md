## Thought Process 
- I need to create a list taht i can lookup quickly and in this case a set.
- check to see if the remainder is in the set, if so then ... of not then ...

####  **What is a Set:** 
>Sets in Python are a collection data type that is unordered, unchangeable, and indexed. They are similar to lists or dictionaries but with a key difference that they only contain unique elements and do not support duplicates.

### Solution
```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_set = set()
```
