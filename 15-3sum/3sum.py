class Solution(object):
    def threeSum(self, nums):
        nums.sort() 
        n = len(nums)
        target = set()
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                
                if total == 0:
                    target.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif total < 0:
                    j += 1  
                else:
                    k -= 1 
        return [list(triplet) for triplet in target]