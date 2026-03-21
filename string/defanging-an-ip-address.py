class Solution:
    def defangIPaddr(self, address: str) -> str:
        li_add = list(address)
        for i, num in enumerate(li_add):
            if num == ".":
                li_add[i] = "[.]"
        return "".join(li_add)
        