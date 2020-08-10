class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_sort = sorted(heights)
        move = 0
        for i in range(len(heights)):
            if heights[i] != heights_sort[i]:
                move += 1
        return move
