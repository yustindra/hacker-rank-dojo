class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort(reverse=True)
        if len(nums) < 3:
            return max(nums)
        else:
            return nums[2]
