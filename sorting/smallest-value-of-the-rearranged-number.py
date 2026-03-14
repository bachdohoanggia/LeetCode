class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
            
        if num > 0:
            strnum = str(num)
            sortstr = sorted(strnum)
            for i in range(len(sortstr)):
                if sortstr[0] == '0' and sortstr[i] != '0':
                    sortstr[0], sortstr[i] = sortstr[i], sortstr[0]
            ans = ''.join(sortstr)
        elif num < 0:
            S = str(num)[1:]
            sortS = sorted(S, reverse = True)
            ans = '-' + ''.join(sortS)
        return int(ans)

                