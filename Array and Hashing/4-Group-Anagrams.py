class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_groups = {}

        for word in strs:
            # Sort the characters of the word to identify its anagram signature
            sorted_word = ''.join(sorted(word))
            # If the sorted word exists in the dictionary, add the word to its group
            if sorted_word in anagram_groups:
                anagram_groups[sorted_word].append(word)
            else:
                # If it doesn't exist, create a new group with the sorted word as the key
                anagram_groups[sorted_word] = [word]
        
        return list(anagram_groups.values())
