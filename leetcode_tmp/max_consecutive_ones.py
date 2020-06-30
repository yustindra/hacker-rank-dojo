class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxc = 0
        current = 0
        
        for i in nums:
            if i == 1:
                current += 1
            else:
                maxc = max(maxc, current)
                current = 0
        
        return max(maxc, current)
