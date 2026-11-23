class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_chars = defaultdict(int)
        for c in s:
            s_chars[c] += 1

        t_chars = defaultdict(int)    
        for c in t:
            t_chars[c] += 1
        return s_chars == t_chars