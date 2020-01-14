'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

#My 5800ms answer:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if target==nums[i]+nums[j]:
                    return [i,j]
        return [0,0]
    

#The 50ms solution:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return list()
        indices = dict()
        for i, n in enumerate(nums):
            other_index = indices.get(target - n)
            if other_index is not None:
                return [other_index, i]
            else:
                indices[n] = i
        return list()

#Lesson learned: Python is very different from .net languages