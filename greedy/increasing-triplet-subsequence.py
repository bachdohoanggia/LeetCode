class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        x, y = inf, inf
        for num in nums:
            if num < x:
                x = num
            elif x< num <y:
                y = num
            else:
                return True
        return False