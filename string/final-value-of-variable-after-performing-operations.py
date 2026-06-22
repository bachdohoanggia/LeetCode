class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        total = 0
        for operation in operations:
            if operation == "++X" or operation == "X++":
                total += 1
            else:
                total -= 1
        return total