class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        for i in range(len(strs[0])):

            for other_str in strs[1:]:
                if i >= len(other_str) or strs[0][i] != other_str[i]:
                    return strs[0][:i]
        return strs[0]

        