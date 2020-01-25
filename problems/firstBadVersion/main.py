# this is needed for a solution i found
from bisect import bisect_left


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version: int) -> bool:
	return True or False

class Solution:
    # times out
    def firstBadVersion(self, n: int) -> int:
        # if it is bad
            # go to previous version
        # else
            # go to next version

        flag = isBadVersion(n)
        direction = -1 if flag else 1

        while flag == isBadVersion(n):
            n += direction

        return n if isBadVersion(n) else n + 1


    #  not mine but supposedly works
    def first_bad_version(self, n: int) -> int:
        
        low = 1

        while low <= n:
            mid = (low + n) // 2
            if isBadVersion(mid):
                n = mid - 1
            else:
                low = mid + 1

        return low

    #  not mine but supposedly works
    def first_bad_Version(self, n: int) -> int:
        
        self.__getitem__ = isBadVersion
        return bisect_left(self, True, 1, n)



# 1, 2, 3, 4, 5, 6, 7, 8, 9
#          ^ bad