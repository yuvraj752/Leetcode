class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS , countT = {} , {}               # TC = O(n+m)
        if len(s) != len(t):                    # SC = O(n+m)
            return False
        for index in range(len(s)):
            countS[s[index]] = 1 + countS.get(s[index],0)
            countT[t[index]] = 1 + countT.get(t[index],0)
        for key in countS:
            if countS[key] != countT.get(key,0):
                return False
        return True