class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edges0 = set(edges[0])
        edges1 = set(edges[1])
        return list(edges0 & edges1)[0]