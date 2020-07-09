class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2 = 0, 0
        while p2 < n and p1 < m:
            if nums2[p2] <= nums1[p1]:
                nums1.insert(p1, nums2[p2])
                nums1.pop()
                p2 += 1
                m += 1
            p1 += 1
        if p2 < n:
            del nums1[m:]
            nums1.extend(nums2[p2:])
