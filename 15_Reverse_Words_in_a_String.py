class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = []
        temp = ''
        cnt = 0
        
        for i in range(len(s)):
            if s[i] != ' ':
                temp += s[i]
            elif temp:
                words.append(temp)
                temp = ''
                cnt += 1
        words.append(temp)
        cnt += 1
        
        final = ''
        for word in reversed(words):
            final += word
            cnt -= 1
            if cnt == 0:
                break
            final += ' '
        
        return final