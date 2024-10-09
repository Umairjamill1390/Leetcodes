## Thought Process
- My initial approach was to compare each word in the list with the remaining words by sorting them, as anagrams have the same sorted sequence.
- I created a set to track the indices of words that had already been grouped, ensuring no duplicates are processed.
- For each word, I created a temporary list to store the anagrams found, adding the word and its matching anagrams to this list.
- This does solve for most cases, but it’s insufficient for larger datasets, resulting in a runtime error.


#### Here is my code
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        removed = set()
        for i in range(len(strs)):
            if i not in removed: 
                removed.add(i)
                temp = [strs[i]]
                for j in range (i+1, len(strs)):
                    if sorted(strs[i]) == sorted(strs[j]):
                        removed.add(j)
                        temp.append(strs[j])
                res.append(temp)
        return res
```
