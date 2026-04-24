class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str_ref = strs[0]

        for i in range(len(str_ref)):
            for other_str in strs[1:]:
                if i >= len(other_str) or other_str[i] != str_ref[i]:
                    return str_ref[:i]
        