class Solution:

    # I DID NOT SOLVE THIS ONE MYSELF
    # not mine
    def is_ugly(self, num: int) -> bool:
        
        for x in [2, 3, 5]:
            while num % x == 0:
                num /= x

        return num == 1