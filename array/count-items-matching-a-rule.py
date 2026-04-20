class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        RULE_KEY_MAP = {
            "type": 0,
            "color": 1,
            "name": 2
        }
        
        index = RULE_KEY_MAP[ruleKey]
        count = 0
        
        for item in items:
            if item[index] == ruleValue:
                count += 1
                
        return count