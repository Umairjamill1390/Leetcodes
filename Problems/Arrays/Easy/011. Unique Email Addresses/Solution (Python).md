## Thought Process
- First, I separated the email into two parts: the local name (before `@`) and the domain (after `@`).
- I cleaned the local name by ignoring everything after the `+` symbol and removing periods (`.`).
- Finally, I added the domain back to form the cleaned email and checked if it was already in the set of unique emails.

#### What is `split()`?
The `split()` function in Python divides a string into a list based on a specified delimiter. In this case, I used it to separate the local name and domain of the email by splitting at the `@` symbol. For example:

```python
"example@domain.com".split("@")
# Output: ['example', 'domain.com']
```
#### What is `replace()`?
The `replace()` function in Python replaces all occurrences of a substring with another substring. In this case, I used it to remove all periods (`.`) from the local part of the email. For example:
```python
"hello.world".replace(".", "")
# Output: 'helloworld'
```

#### Here is my code
```python
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]  
            local = local.replace('.', '') 
            
            cleaned_email = local + '@' + domain  
            unique_emails.add(cleaned_email)
        
        return len(unique_emails)
```
