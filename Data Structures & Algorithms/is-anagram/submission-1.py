class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # sort and compare the strings

        return ''.join(sorted(t)) == ''.join(sorted(s))

        # use the hashkey to create a key for the strings

        # if len(s) != len(t):
        #     return False
        
        # n = len(s)
        # s_hash = [0] * 26
        # t_hash = [0] * 26
        # for i in range(n):
        #     s_hash[ord(s[i]) - ord('a')] +=1
        #     t_hash[ord(t[i]) - ord('a')] +=1
        
        # return '#'.join([str(x) for x in s_hash]) == '#'.join([str(x) for x in t_hash])



        