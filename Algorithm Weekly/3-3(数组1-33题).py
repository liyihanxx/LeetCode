#1.两数之和
#给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
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
                    
#11. 盛最多水的容器()
#给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
#在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#双指针法（时间复杂度为0（n））
class Solution:
    def maxArea(self, height):
        i=len(height)-1
        j=0
        sum=0
        while j<i:
            sum=max(sum,(i-j)*min(height[j],height[i]))
            if(height[j]<height[i]):
                j=j+1
            else:
                i=i-1
        return sum
    
    
#26. 删除排序数组中的重复项
#给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
#不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

class Solution:
    def removeDuplicates(self, nums):
        i=0
        while i<(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums.remove(nums[i+1])
            else:
                i=i+1
        return(len(nums))
    
#27. 移除元素
#给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
#不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
#元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

class Solution:
    def removeElement(self, nums, val):
        i=0
        while i<len(nums):
            if nums[i]==val:
                nums.remove(nums[i])
            else:
                i=i+1
        return len(nums)
        
