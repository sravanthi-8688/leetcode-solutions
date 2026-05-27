class Solution(object):
    def numberOfSpecialChars(self, word):
        u = []
        
        for i in word:
            if i not in u:
                u.append(i)
        
        count = 0
        
        for ch in u:
            if ch.islower():
                if ch.upper() in word:
                    # check condition: all lowercase before first uppercase
                    if word.rfind(ch) < word.find(ch.upper()):
                        count += 1
        
        return count