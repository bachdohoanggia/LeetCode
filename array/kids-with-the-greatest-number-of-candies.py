class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        arr = []
        max_candy = max(candies)
        for candy in candies:
            if candy + extraCandies < max_candy:
                arr.append(False)
            else:
                arr.append(True)
        return arr
