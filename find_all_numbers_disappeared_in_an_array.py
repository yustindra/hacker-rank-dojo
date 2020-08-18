class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        all_set = set(range(1, len(nums) + 1))
        for i in nums:
            if i in all_set:
                all_set.remove(i)
        return list(all_set)
