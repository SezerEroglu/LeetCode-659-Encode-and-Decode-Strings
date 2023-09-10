class Solution:
    def encode(self, strs):
        # write your code here
        res = ""
        for i in range(len(strs)):
            res += f"{len(strs[i])}#{strs[i]}"
        return res

    def decode(self, str):
        # write your code here
        res = []
        for s in range(1, len(str)):
            if str[s] == "#":
                length = int(str[s - 1])
                res.append(str[s + 1 : s + 1 + length])
        return
