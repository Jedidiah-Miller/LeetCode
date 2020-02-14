class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:

        S = S.replace('-', '')

        i = len(S) - 1
        count = 1

        while i > 0:
            if count == K:
                S = S[:i] + '-' + S[i:]
                count = 1
            else:
                count += 1

            i -= 1

        return S.upper()



solution = Solution().licenseKeyFormatting

test, expected = solution("444444444444", K = 4), "4444-4444-4444"
print('test:', test, test == expected)
test, expected = solution("5F3Z-2e-9-w", K = 4), "5F3Z-2E9W"
print('test:', test, test == expected)
test, expected = solution("2-5g-3-J", K = 2), "2-5G-3J"
print('test:', test, test == expected)