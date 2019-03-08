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
                    
                    
#4. 寻找两个有序数组的中位数(????????)
#给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
#请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
#你可以假设 nums1 和 nums2 不会同时为空

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()
        length = len(nums)
        if length == 2:
            return (nums[0] + nums[1])/2
        if length % 2 == 0:
            return (nums[length // 2 - 1] + nums[(length // 2)])/2
        return nums[length // 2]        

    
                    
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
    
    
    
#15. 三数之和
#给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 存储结果列表
        res_list = []
        # 对nums列表进行排序，无返回值，排序直接改变nums顺序
        nums.sort()
        for i in range(len(nums)):
            # 如果排序后第一个数都大于0，则跳出循环，不可能有为0的三数之和
            if nums[i] > 0:
                break
            # 排序后相邻两数如果相等，则跳出当前循环继续下一次循环，相同的数只需要计算一次
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 记录i的下一个位置
            j = i + 1
            # 最后一个元素的位置
            k = len(nums) - 1
            while j < k:
                # 判断三数之和是否为0
                if nums[j] + nums[k] == -nums[i]:
                    # 把结果加入数组中
                    res_list.append([nums[i], nums[j], nums[k]])
                    # 判断j相邻元素是否相等，有的话跳过这个
                    while j < k and nums[j] == nums[j+1]: j += 1
                    # 判断后面k的相邻元素是否相等，是的话跳过
                    while j < k and nums[k] == nums[k-1]: k -= 1
                    # 没有相等则j+1，k-1，缩小范围
                    j += 1
                    k -= 1
                # 小于-nums[i]的话还能往后取
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    k -= 1
        return res_list


if __name__ == '__main__':
    s = Solution()
    result_list = s.threeSum([-1, 0, 1, 2, -1, -4])
    print(result_list)

#16. 最接近的三数之和
#给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
#找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
class Solution:
    def threeSumClosest(self, nums, target):
        mindiff = 10000
        nums.sort()
        res = 0
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left < right:
                sum = nums[left] + nums[right] + nums[i]
                diff = abs(target - sum)
                if diff < mindiff:
                    mindiff = diff
                    res = sum
                if target == sum:
                    return sum
                elif sum < target:
                    left += 1
                else:
                    right -= 1                      

        return res
    
    


    
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
        
