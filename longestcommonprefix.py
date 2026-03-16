class Solution:
    def longestCommonPrefix(self,strs:List[str])->str:
        prefix=strs[0]
        x=len(prefix)
        for i in strs[1:]:
            while prefix!=i[0:x]:
                x-=1
                if x==0:
                    return ""
                prefix=prefix[0:x]
        return prefix
