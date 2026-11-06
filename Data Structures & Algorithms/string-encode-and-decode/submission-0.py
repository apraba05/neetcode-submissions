class Solution:
    def encode(self, strs: List[str]) -> str:
        # Prefix each string with its length and a separator.
        return "".join(f"{len(word)}#{word}" for word in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            # Read the length before the separator.
            separator = s.index("#", i)
            length = int(s[i:separator])

            # Extract exactly that many characters.
            start = separator + 1
            end = start + length
            result.append(s[start:end])

            # Continue at the next length prefix.
            i = end

        return result
