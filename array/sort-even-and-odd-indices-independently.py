class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        evenarr = sorted(nums[::2])
        oddarr = sorted(nums[1::2], reverse = True)
        ans = [0]*len(nums)
        e = 0
        o = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                ans[i] = evenarr[e]
                e += 1
            else:
                ans[i] = oddarr[o]
                o += 1
        return ans