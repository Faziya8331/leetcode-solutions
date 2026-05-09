class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=set()
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                left=j+1
                right=n-1
                while left<right:
                    total=nums[i]+nums[j]+nums[left]+nums[right]
                    if total==target:
                        res.add((nums[i],nums[j],nums[left],nums[right]))
                        left+=1
                        right-=1
                    elif total<target:
                        left+=1
  
                    else:
                        right-=1
        return [list(t) for t in res]

        
