class Solution:
    def addDigits(self, num: int) -> int:
        
        while num > 9:
            num = sum([int(x) for x in str(num)])

        return num
# recursive
    def _addDigits(self, num: int) -> int:
        return num if num < 10 else self.addDigits(sum([int(x) for x in str(num)]))

# one line O(n) runtime
# I found this one and it bothered me how good it is
    def add_digits(self, num: int) -> int:
        return num if num < 10 else num % 9 or 9