
class Solution:
    def twoSum(self,nums,target):
        n=len(nums)
        for x in range(n):
            for y in range(x+1,n):
                if nums[y]  ==  target - nums[x]:
                    return x,y
                    break
                else:
                    continue
