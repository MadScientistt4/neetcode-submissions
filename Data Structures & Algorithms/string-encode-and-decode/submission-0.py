class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        for string in strs:
            encode_str += string + "|"
        return encode_str
    def decode(self, s: str) -> List[str]:
        decoded_str = s.split("|")
        decoded_str.pop()
        return decoded_str