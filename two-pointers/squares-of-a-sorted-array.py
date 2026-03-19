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

        negative.reverse()

        i = j = 0
        while i < len(positive) and j < len(negative):
            if positive[i] <= negative[j]:
                ans.append(positive[i])
                i += 1
            else:
                ans.append(negative[j])
                j += 1
        ans.extend(positive[i:])
        ans.extend(negative[j:])

        return ans
        