class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        evenli = []
        oddli = []
        for num in nums:
            if num % 2 == 0:
                evenli.append(num)
            else:
                oddli.append(num)
        evenli.sort()
        oddli.sort(reverse = True)
        x, y = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = evenli[x]
                x += 1
            else:
                nums[i] = oddli[y]
                y += 1
        return nums