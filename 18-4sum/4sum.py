class Solution(object):
    def fourSum(self, nums, target):
        nums.sort() 
        n = len(nums)
        res = set()  
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                k = j + 1
                l = n - 1
                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    
                    if total == target:
                        res.add((nums[i], nums[j], nums[k], nums[l]))
                        k += 1
                        l -= 1
                    elif total < target:
                        k += 1 
                    else:
                        l -= 1 
        
        return [list(q) for q in res]