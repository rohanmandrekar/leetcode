class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups=collections.defaultdict(list)
        for word in strs:
            count=[0]*26
            for c in word:
                count[ord(c)-ord('z')]+=1
            groups[tuple(count)].append(word)
        return groups.values() 