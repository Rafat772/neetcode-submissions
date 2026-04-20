class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp ={}
        for words in strs:
            key = ''.join(sorted(words))
            if key in mp:
                mp[key].append(words)
            else:
                mp[key]=[words] 
        return list(mp.values())           
        