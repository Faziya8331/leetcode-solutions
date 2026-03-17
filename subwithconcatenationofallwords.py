from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        n=len(s)
        word_len=len(words[0])
        num_words=len(words)
        total_length=word_len*num_words
        word_count=Counter(words)
        result=[]
        for i in range(n-total_length+1):
            seen=[]
            for j in range(0,total_length,word_len):
                word=s[i+j:i+j+word_len]
                seen.append(word)
            if Counter(seen)==word_count:
                result.append(i)
        return result  
