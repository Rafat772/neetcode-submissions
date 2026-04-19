class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check lenght od both string
        if len(s)!= len(t):
            return False
        #counting freq of s
        count={}
        for ch in s:
            count[ch]=count.get(ch,0)+1
        # reducing count using t
        for ch in t:
            if ch not in count or count[ch]==0:
                return False
            count[ch]-=1    
        return True                
            
        