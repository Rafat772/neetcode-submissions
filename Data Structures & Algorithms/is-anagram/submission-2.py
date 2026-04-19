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

'''import java.util.HashMap;

class Solution {
    public boolean isAnagram(String s, String t) {
        
        // Step 1: Length check
        if (s.length() != t.length()) {
            return false;
        }

        // Step 2: Count frequency of s
        HashMap<Character, Integer> count = new HashMap<>();

        for (char ch : s.toCharArray()) {
            count.put(ch, count.getOrDefault(ch, 0) + 1);
        }

        // Step 3: Reduce using t
        for (char ch : t.toCharArray()) {
            if (!count.containsKey(ch) || count.get(ch) == 0) {
                return false;
            }
            count.put(ch, count.get(ch) - 1);
        }

        return true;
    }
}'''                       
            
        