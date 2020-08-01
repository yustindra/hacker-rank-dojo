class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[idx] = nums[i]
                idx += 1
        for j in range(idx, len(nums)):
            nums[j] = 0
