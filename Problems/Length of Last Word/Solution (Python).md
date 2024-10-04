## Thought Process
- Python offers a convenient feature called **negative indexing**, which allows accessing elements from the end of a list. This enhances the language’s simplicity and ease of use compared to many other languages.
- I utilized the `split()` function, which splits a string into a list of words, and then applied negative indexing (`[-1]`) to directly access the last word. Finally, I used the `len()` function to return the length of this last word.

#### What is Negative Indexing?
> **Negative Indexing**: In Python, `-1` refers to the last element of a list, making it easy to access elements from the end without needing to calculate the length.

#### What is `split()`
> This built-in function splits a string by whitespace (or a specified delimiter) and returns a list of substrings. It can be modified to split based on different needs.
>
> Here's an axample: `split(",")` means split based on `,`.

#### Here is my code
```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
