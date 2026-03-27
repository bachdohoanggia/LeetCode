class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(account) for account in accounts) # đây k phải O(1) ạ? e khum bt nx