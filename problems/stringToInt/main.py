class Solution:
    def myAtoi(self, s: str) -> int:

        result = ''

        for i in range(len(s)):
            x = s[i]
            if x.isalpha():
                break
            elif x == '-' and result == '':
                result += x
            elif x.isdigit():
                result += x
            elif x.isspace():
                if len(result) != 0:
                    break
            else:
                if result[:1] == '-':
                    break
                if x == '+':
                    if i != len(s) - 1:
                        if not s[i + 1].isdigit():
                            break
                else:
                    break

        for x in ['', '-', '+']:
            if result == x:
                return 0

        result = int(result)

        return result if result.bit_length() < 33 else 2147483648 if result > 0 else -2147483648




solution = Solution().myAtoi
test, expected = solution('42'), 42
print('test:', test, test == expected)
test2, expected2 = solution("   -42"), -42
print('test2:', test2, test2 == expected2)
test3, expected3 = solution('4193 with words'), 4193
print('test3:', test3, test3 == expected3)
test4, expected4 = solution('words and 987'), 0
print('test4:', test4, test4 == expected4)
test5, expected5 = solution('-91283472332'), -2147483648
print('test5:', test5, test5 == expected5)
test6, expected6 = solution("+-2"), 0
print('test6:', test6, test6 == expected6)
test7, expected7 = solution("+"), 0
print('test7:', test7, test7 == expected7)
test8, expected8 = solution("+1"), 1
print('test8:', test8, test8 == expected8)
test9, expected9 = solution("-+1"), 0
print('test9:', test9, test9 == expected9)
