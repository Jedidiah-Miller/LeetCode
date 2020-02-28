class Solution:
    # first try
    # 116 ms 12.8MB
    def firstUniqChar(self, s: str) -> int:
        
        checked = {}

        for x in s:
            if x not in checked:
                checked[x] = 1
            else:
                checked[x] += 1

        for i in range(len(s)):
            if checked[s[i]] == 1:
                return i

        return -1

    # refractored a little
    # 88ms 12.8MB
    def _firstUniqChar(self, s: str) -> int:

        if s == "":
            return -1

        checked = {}

        for x in s:
            if x not in checked:
                checked[x] = 1
            else:
                checked[x] += 1

        min_key = min(checked.keys(), key=(lambda k: checked[k]))

        return s.find(min_key) if checked[min_key] == 1 else -1




solution = Solution()._firstUniqChar

test, expected = solution('leetcode'), 0
print(test, test == expected)
test, expected = solution('loveleetcode'), 2
print(test, test == expected)
test, expected = solution('lleetcode'), 4
print(test, test == expected)
test, expected = solution('lololpppppjjjj'), -1
print(test, test == expected)
test, expected = solution('lololpppppjjjjx'), 14
print(test, test == expected)
test, expected = solution(''), -1
print(test, test == expected)
test, expected = solution('qqaazzwwssxxeeddccrrffvvttggbbyyhhnnuujjmmikkoollpp'), 42
print(test, test == expected)