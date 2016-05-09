# For the two sum question, the brute force method is go through the list twice and find all two number combinations.
# And the worst time complexity is O(n^2).

# Other conditions that should be considered are:
#	1. duplicate
#	2. negative number
#	3. return number value or index
#	4. return should be sorted or not

# improved method 1 - sort the list
# If sort the list at first, then can use the two pointers method to find the result
# One pointer start from index 0 and another start from end.
# If two values sum smaller than target, move the start pointer to next
# If two values sum bigger than target, move the end pointer to previous one
# Until two pointers meet and do not found the result pair
# Time complexity is O(n*logn)(sort) + O(n)(find pair) -> O(n*logn)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if (target == None or nums == None or len(nums) < 2):
            return []
        
        nums.sort()
        start = 0
        end   = len(nums) - 1
        
        while (start < end):
            if ((nums[start] + nums[end]) == target):
                return [start, end]
            elif (nums[start] + nums[end] < target):
                start += 1
            else:
                end -= 1
        
        return []
       
# But this method isn't suitable for this question because this question need return indexs, sort the list will change the index
# Otherwise need another data structure to store the relationship between value and original index. Need O(n) space complexity.

# improved method 2 - use dict(map) to store all previous number and index
# This method need O(n) space complexity and O(n) time complexity

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if (target == None or nums == None or len(nums) < 2):
            return []
        
        num_map = dict()
        
        for index, value in enumerate(nums):
            left = target - value
            if (left in num_map):
                return [num_map[left], index]
            else:
                num_map[value] = index
                
        return []
