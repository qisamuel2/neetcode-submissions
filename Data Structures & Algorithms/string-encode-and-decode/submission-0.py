class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(",".join(str(ord(c)) for c in s) + "|" for s in strs)
    def decode(self, s: str) -> List[str]:
        parts = s.split("|")[:-1]
        result = []
        for p in parts:
            if p == "":
                result.append("")
            else:
                result.append("".join(chr(int(n)) for n in p.split(",")))
        return result