def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t:
            return False
        hashset = set()
        for char in s:
            hashset.add(char)
        for char_t in t:
            if char_t not in hashset:
                return False
        return True