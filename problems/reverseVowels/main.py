import re

class Solution:
    def reverseVowels(self, s: str) -> str:
        
        s = [x for x in s]
        vowelIndexes = []

        for i in range(len(s)):
            if self.isVowel(s[i]):
                vowelIndexes.append(i)

        for i in range(len(vowelIndexes) // 2):
            front = vowelIndexes[i]
            back = vowelIndexes[(len(vowelIndexes) - i) - 1]
            s[front], s[back] = s[back], s[front]

        return ''.join(s)

    def isVowel(self, c: str) -> bool: 
        return c.lower() in 'aeiou'


    # not mine
    def reverse_vowels(self, s: str) -> str:
        vowels = (c for c in reversed(s) if c in 'aeiouAEIOU')
        return re.sub('(?i)[aeiou]', lambda m: next(vowels), s)