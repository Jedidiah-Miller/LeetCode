class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        magazine = [x for x in magazine]
        for x in ransomNote:
            didFind = False
            for i in range(len(magazine)):
                if magazine[i] == x:
                    didFind = True
                    magazine = magazine[0:i:] + magazine[i+1::]
                    magazine.pop(i)
                    break

            if not didFind:
                return False

        return True