from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # a = 0
        # for x in nums:
        #     a +=1
        #     for y in nums[a:]:
        #         if x == y:
        #             return True
        # return False
        return len(nums) != len(set(nums))   # set does not have duplicate