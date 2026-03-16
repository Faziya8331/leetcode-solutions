class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        nge={}
        for i in reversed(nums2):
            while st and st[-1]<=i:
                st.pop()
            if st:
                nge[i]=st[-1]
            else:
                nge[i]=-1
            st.append(i)
        res=[]
        for j in nums1:
            res.append(nge[j])
        return res
        
        
