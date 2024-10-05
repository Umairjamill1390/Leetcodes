## Thought Process
- I choose the shortest word as the reference for comparison. As it would take fewer loops and less time.
- I then iterate through each character of the `shortest` word and compare it with the corresponding character in all other words.
- If there's a mismatch, return the result as is. If not, update res and move to next char.  


#### Here is my code
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        shortest = min(strs, key=len)
        for i in range(len(shortest)): 
            for j in range(len(strs)):
                if strs[j][i] != shortest[i]: return res
            res += shortest[i]
        return res
```
