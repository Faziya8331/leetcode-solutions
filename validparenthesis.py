class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        d={')':'(',']':'[','}':'{'}
        for ch in s:
            if ch in d:
                if st:
                    top=st.pop()
                else:
                    top="#"
                if d[ch]!=top:
                    return False
            else:
                st.append(ch)
        return not st
