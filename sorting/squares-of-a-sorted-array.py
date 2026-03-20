class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        ans = []
        for num in nums:
            if num < 0:
                negative.append(num*num)
            else:
                positive.append(num*num)

        i = 0
        j = len(negative) - 1
        while i < len(positive) and j >= 0:
            if positive[i] <= negative[j]:
                ans.append(positive[i])
                i += 1
            else:
                ans.append(negative[j])
                j -= 1
        ans.extend(positive[i:])
        
        while j >= 0:
            ans.append(negative[j])
            j -= 1
        return ans
        