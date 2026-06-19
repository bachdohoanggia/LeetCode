class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        check = []
        max_candies = max(candies)
        for candy in candies:
            if candy + extraCandies >= max_candies:
                check.append(True)
            else:
                check.append(False)
        return check
        