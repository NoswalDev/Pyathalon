class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        brute force:
            i = 0
            outp = []
            for i in range(0,len(nums)-(k-1)):
                outp.append(max(nums[i:i+k]))
            return outp
        
        same or increasing:
            store local max and compare with new i
            assign i as new local max
            set countdown for local max
        decreasing:
            a queue:
                [value]
                [expiration]
            keep adding vals
            new max: forget about all the older ones
            when appending: check expiration. If expired, cycle out.
        '''
        stack = deque()
        exp = deque()
        outp = []
        for i,v in enumerate(nums):
            while stack and v>stack[-1]:
                stack.pop()
                exp.pop()
            stack.append(v)
            exp.append(i)
            if i >= k-1:
                if exp and exp[0] < i-(k-1):
                    stack.popleft()
                    exp.popleft()
                outp.append(stack[0])
        return outp