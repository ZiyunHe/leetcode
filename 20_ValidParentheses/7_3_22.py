# 这个答案错误没有考虑乱序的case
# def isValid(self, s: str) -> bool:
#         if not s:
#             return False
#         store = {}
#         left = {'(', '{', '['}
#         right = {')': '(', '}': '{', ']':'['}
#         for char in s:
#             if char in left:
#                 if char not in store:
#                     store[char] = 0
#                 store[char] += 1
#             else:
#                 r = right[char]
#                 if r not in store:
#                     return False
#                 store[r] -= 1
#                 if store[r] == 0:
#                     del store[r]
#         return len(store) == 0

def isValid(self, s: str) -> bool:
        if not s:
            return False
        store = []
        right = {')': '(', '}': '{', ']':'['}
        for char in s:
            if char not in right:
                store.append(char)
            else:
                # 这个判断是corner case "]"
                if not store:
                    return False
                last = store[-1]
                if right[char] != last:
                    return False
                store.pop()
        return len(store) == 0