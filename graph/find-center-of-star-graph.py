class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edge0 = set(edges[0])
        edge1 = set(edges[1])
        return list(edge0 & edge1)[0]