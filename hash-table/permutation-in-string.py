class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = defaultdict(int)
        count2 = defaultdict(int)

        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        for i in range(n1):
            count1[s1[i]] += 1
            count2[s2[i]] += 1

        if count1 == count2:
            return True
        
        for right in range(n1, n2):
            count2[s2[right]] += 1
            count2[s2[right- n1]] -= 1
            if count2[s2[right- n1]] == 0:
                del count2[s2[right- n1]]
            if count1 == count2:
                return True
        return False
        
        
