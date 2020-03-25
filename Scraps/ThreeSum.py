output = []
from typing import List
'''
[a,b,c]
a+b+c = 0
-a = b+c

[-1,0,1,2,-1,-4]
[0,-1,-1,1,2,-4]
[2,1,-1,-1,0,-4]
[3,-1,-2,-2,-1]

[-4,-1,-1,0,1,2]
[-2,-2,-1,-1,3]

loop1: if in list(sets(nums[0:-2]))
loop2: unique
loop3: if in nums[k:]

no dupe entries
solution sets are sorted
are inputs sorted? yes

meth2
list to dict
    dict = {val:ind,val:ind}
    get unique and get correct pos when jumping
use filter() to get subdict of specific range
lv1[0:-2]
lv2[lv1:-1]
lv3[lv2:] unique
'''
nums = [-1,0,1,2,-1,-4]
nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
nums = [-2,0,1,1,2]

# dict1 = {v : i for i,v in enumerate(snums)}

output = []
snums = sorted(nums)
dict1 = {}
for i,v in enumerate(snums[0:-2]):
    if not v in dict1:
        dict1[v] = i
for v in dict1:
    dict2 = {w:j for j,w in enumerate(snums[1+dict1[v]:-1])}
    for w in dict2:
        if -v-w in snums[dict1[v]+dict2[w]+2:]:
            output.append([v,w,-v-w])
return output


    