class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        brackets = list(s)


        if len(brackets) % 2: return False

        others = [0]*(len(brackets))
        idx = 0
        for i in range(len(brackets)):
            if brackets[i] in pairs.keys():
                others[idx] = brackets[i]
                idx += 1
            else:
                if (not idx) or (not others[idx-1]): return False

                if pairs[others[idx-1]] == brackets[i]:
                    others[idx-1] = 0
                    idx -= 1
                else:
                    return False

        for other in others:
            if other: return False

        return True

# 충격적인 코드야..
class Solution(object):
    def isValid(self, s):
        while "()" in s or "{}" in s or '[]' in s:
            s = s.replace("()", "").replace('{}', "").replace('[]', "")
        return s == ''

