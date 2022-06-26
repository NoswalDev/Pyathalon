output = []
from typing import List
'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

'''
arr = [-1,0,1,2,-1,-4]
# nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
# nums = [-2,0,1,1,2]

def threeSum(self, nums: List[int]) -> List[List[int]]:
    outp = []
    done = {}
    dupes = {}
    complement = {}
    t_arr = []
    k = 0
    mn = 0
    mx = 0
    for i in range(0,len(nums)-2):
        complement = {}
        if nums[i] in done:
            continue
        done[nums[i]] = -1
        for j in range(i+1,len(nums)):
            k = -nums[i] - nums[j]
            if nums[j] in complement:
                mn = min(nums[i],nums[j],k)
                mx = max(nums[i],nums[j],k)
                #check dupes
                t_arr = dupes.get(mn,[])
                if mx in t_arr:
                    continue
                t_arr.append(mx)
                dupes[mn] = t_arr
                outp.append([mn, -mn-mx, mx])
            else:
                complement[k] = -1
    return outp
'''
def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
        
        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res
'''

print(threeSum(arr))

    