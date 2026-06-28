class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        cell_map ={
            (0, 0): ["row1", "col1" , "diag1"],
            (0, 1): ["row1", "col2"],
            (0, 2): ["row1", "col3", "diag2"],
            (1, 0): ["row2", "col1"],
            (1, 1): ["row2", "col2", "diag1", "diag2"],
            (1, 2): ["row2", "col3"],
            (2, 0): ["row3", "col1", "diag2"],
            (2, 1): ["row3", "col2"],
            (2, 2): ["row3", "col3", "diag1"]
        }
        check = defaultdict(int)
        for i, (a,b) in enumerate(moves):
            if i % 2 == 0:
                val = 1
            else:
                val = -1
            for path in cell_map[(a,b)]:
                check[path] += val

                if abs(check[path]) == 3:
                    return "A" if val == 1 else "B"
        if len(moves) == 9:
            return "Draw"
        return "Pending"
