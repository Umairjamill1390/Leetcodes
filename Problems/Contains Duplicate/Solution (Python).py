class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for each in nums:
            if each in my_set:
                return True
            my_set.add(each)
        return False 
