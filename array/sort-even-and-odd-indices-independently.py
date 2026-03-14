class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        oddarr = []
        evenarr = []
        for i in range(len(nums)):
            if i % 2 == 0:
                evenarr.append(nums[i])
            else:
                oddarr.append(nums[i])
        evenarr.sort()
        oddarr.sort(reverse = True)
        x = 0
        y = 0
        for i in range(len(nums)):
                if i % 2 ==0:
                    nums[i] = evenarr[x]
                    x += 1
                else:
                    nums[i] = oddarr[y]
                    y += 1
        return nums