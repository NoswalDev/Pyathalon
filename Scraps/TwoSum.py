
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = nums
        for i in range(0, len(a)-1):
            for j in range(i+1, len(a)):
                if a[i] + a[j] == target:
                    return [i,j]
        return [0,0]
    def threeSum(self, nums: List[int], target: int) -> List[int]:
        solutions = dict({})
        for i in range(len(nums)):
            num = nums[i]
            solve = target - num
            solution_index = solutions.get(num, -1)
            if solution_index >= 0:
                return [solution_index, i]
            solutions[solve] = i
'''

nums = [1,2,3,4]
dict1 = {'a':'one'}
if 'one' in dict1.values():
    print('true')
print('end')
# for i,v in enumerate(nums):
#     # print(i,v)