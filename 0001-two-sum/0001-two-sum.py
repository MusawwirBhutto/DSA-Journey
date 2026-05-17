class Solution(object):
    def twoSum(self, nums, target):
        for n in range(len(nums)):
            for a in range( n+1 , len(nums) ):
                if nums[n] + nums[a] == target:
                    return [n,a]
        
                    
    