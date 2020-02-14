class Solution:
    # my solution
    def wordPattern(self, pattern: str, string: str) -> bool:

        indexes = {}

        string = string.split(' ')

        for i, key in enumerate(pattern):
            if key in indexes:
                indexes[key] += [i]
            else:
                indexes[key] = [i]

        checked = {}

        for key in indexes:

            i = indexes[key][0]
            if i >= len(string):
                return False

            word = string[i]

            if word in checked:
                return False

            for j in indexes[key]:
                if j >= len(string):
                    return False
                if string[j] != word:
                    return False
                string[j] = key

            checked[word] = True

        return pattern == ''.join(string)



solution = Solution().wordPattern

test, expected = solution('abba', 'dog cat cat dog'), True
print('test:', test, test == expected)
test, expected = solution('abba', 'dog cat cat fish'), False
print('test:', test, test == expected)
test, expected = solution('aaaa', 'dog cat cat dog'), False
print('test:', test, test == expected)
test, expected = solution('aaaa', 'dog dog dog dog'), True
print('test:', test, test == expected)
test, expected = solution('abba', 'dog dog dog dog'), False
print('test:', test, test == expected)