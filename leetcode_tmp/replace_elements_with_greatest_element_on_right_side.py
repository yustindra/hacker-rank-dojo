class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l, ans = len(arr), []
        
        for i in range(l-1):
            ans.append(max(arr[i+1:]))
        ans.append(-1)
        
        return ans
