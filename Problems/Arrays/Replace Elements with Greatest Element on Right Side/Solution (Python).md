## Thought Process
### First Attempt
- My immediate thought was to create sublists, find the maximum among them, and then replace them, as Python allows creating sublists.
- Which did solve the problem, but it wasn't fast enough
#### Here is the code (Sublists):
```python
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        start = 0 
        while start != len(arr) -1: 
            right_largest = max(arr[start + 1:])
            arr[start] = right_largest
            start += 1
        arr[start] = -1
        return arr
```
