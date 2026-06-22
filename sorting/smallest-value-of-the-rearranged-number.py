class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        if num > 0:
            strnum = str(num)
            s_str = sorted(strnum)
            for i in range(len(s_str)):
                if s_str[0] == "0" and s_str[i] != "0":
                    s_str[0], s_str[i] = s_str[i], s_str[0]
            ans = ''.join(s_str)
        elif num < 0:
            s = str(num)[1:]
            sort_s = sorted(s, reverse = True)
            ans = "-" + ''.join(sort_s)
        return int(ans)


            