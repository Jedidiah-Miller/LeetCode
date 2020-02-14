class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        if len(word) < 2:
            return True

        startsWithCapital = word[0].isupper()
        prevIsCapital = word[1].isupper()
        
        if not startsWithCapital and prevIsCapital:
            return False

        word = word[2:]

        for c in word:

            currentIsCaptial = c.isupper()

            if not startsWithCapital and currentIsCaptial:
                return False

            if startsWithCapital == currentIsCaptial and prevIsCapital != currentIsCaptial:
                return False

            if [startsWithCapital, prevIsCapital, currentIsCaptial] == [True, True, False]:
                return False

            prevIsCapital = currentIsCaptial

        return True


    def _detectCapitalUse(self, word: str) -> bool:
        return word == word.capitalize() or word == word.lower() or word == word.upper()



solution = Solution().detectCapitalUse

test, expected = solution('qwertyuiop'), True
print('test: ', test, test == expected)
test, expected = solution('Capital'), True
print('test: ', test, test == expected)
test, expected = solution('capItal'), False
print('test: ', test, test == expected)
test, expected = solution('ALLCAPS'), True
print('test: ', test, test == expected)
test, expected = solution('INcoRRECT'), False
print('test: ', test, test == expected)
test, expected = solution('FFFFFFFFFFFFFFf'), False
print('test: ', test, test == expected)