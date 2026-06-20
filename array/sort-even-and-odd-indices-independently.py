class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        evenli = sorted(nums[::2])
        oddli = sorted(nums[1::2], reverse = True)
        x, y = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = evenli[x]
                x += 1
            else:
                nums[i] = oddli[y]
                y += 1
        return nums