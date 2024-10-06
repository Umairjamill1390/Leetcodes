## Thought Process

- Since removing or changing the value `val` does not affect the final result, we can choose to either keep it or remove it.
- In this case, I opt to remove it, as the judge will only evaluate up to the expected number of valid elements.

#### Here is my code
```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for _ in range(nums.count(val)):
            if val in nums:
                nums.remove(val)
```
