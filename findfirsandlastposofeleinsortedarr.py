class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        first=nums.index(target)
        last=len(nums)-1-nums[::-1].index(target)
        return [first,last]



            
