class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a key and store all the pairs for the key that are anagram to the key. Return the values of the keys. The values will be the groups of the anagrams

        anagram_map = {}
        """
        {"abc": ['abc', 'bac', 'cba']}
        """
        # # T.C: n * k * log k
        # # S.C: n * k
        # for i in range(len(strs)):
        #     # identify the key
        #     key = ''.join(sorted(strs[i]))
        #     # check if the key is present in the map
        #     if key not in anagram_map:
        #         # if the key is not present then create an empty list w.r.t. the key in the map
        #         anagram_map[key] = []
        #     # append the string that belong to key
        #     anagram_map[key].append(strs[i])
        # return  list(anagram_map.values())  


        for i in range(len(strs)):
            key = [0] * 26
            for j in range(len(strs[i])):
                key[ord(strs[i][j]) - ord('a')] +=1
            if tuple(key) not in anagram_map:

                anagram_map[tuple(key)] = []
            anagram_map[tuple(key)].append(strs[i])

        return list(anagram_map.values())

                 

