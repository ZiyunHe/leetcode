# 这个是错误答案，因为没有想到重复字母的case，用了set就不会记录
# def isAnagram(self, s: str, t: str) -> bool:
#         if not s or not t:
#             return False
#         # 这里应该添加一个长短对比 corner case
#         if len(s) != len(t):
#             return False
#         hashset = set()
#         for char in s:
#             hashset.add(char)
#         for char_t in t:
#             if char_t not in hashset:
#                 return False
#         return True

# def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         dic = {}
#         for char in s:
#             if not char in dic:
#                 dic[char] = 1
#             else:
#                 dic[char] = dic[char] + 1
#         for char_t in t:
#             if char_t in dic:
#                 dic[char_t] = dic[char_t] - 1
#                 # 这里可以拿出来。看下个演变
#                 if dic[char_t] == 0:
#                     del dic[char_t]
#             else:
#                 return False
#         return len(dic) == 0

def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        for char in s:
            if not char in dic:
                dic[char] = 1
            else:
                dic[char] = dic[char] + 1
        for char_t in t:
            if char_t in dic:
                dic[char_t] = dic[char_t] - 1
            else:
                return False
            if dic[char_t] == 0:
                del dic[char_t]
        return len(dic) == 0