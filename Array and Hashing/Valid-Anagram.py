# MY SOLUTION
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        hashSet1 = set()
        hashSet2 = {}

        for i in s:
            if i in hashSet1:
                hashSet2[i] += 1
            else:
                hashSet1.add(i)
                hashSet2[i] = 1


        for i in t:
            if i not in hashSet1:
                return False
            hashSet2[i]-= 1

        for i,j in hashSet2.items():
            if j != 0:
                return False
        return True

#OPTIMAL SOLUTION
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True
