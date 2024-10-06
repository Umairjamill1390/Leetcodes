## Thought Process 
- Use a dictionary to quickly look up previously seen numbers and their indices.
- For each number, calculate the remainder (target - number).
- If the remainder is in the dictionary, return the indices. If not, store the current number and its index in the dictionary for future reference.

####  **What is a Set:** 
>Sets in Python are a collection data type that is unordered, unchangeable, and indexed. They are similar to lists or dictionaries but with a key difference that they only contain unique elements and do not support duplicates.

### Solution
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for key, value in enumerate(nums): 
            diff = target - value
            if diff in my_dict: return[my_dict[diff], key]
            my_dict[value] = key
        return []
```
