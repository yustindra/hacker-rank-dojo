class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        sqrd = [a**2 for a in A]
        sqrd.sort()
        return sqrd
