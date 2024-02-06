class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashSet = set()
        x = []

        for i in nums:
            if (target - i) in hashSet:
                if nums.index(i) == nums.index(target - i):
                    x.append(nums.index(i))
                    nums.remove(i)
                    x.append(nums.index(target - i) + 1)
                    return x
                else:
                    return [nums.index(i), nums.index(target-i)]
                
            else:
                hashSet.add(i)

#Optimal Solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]] 