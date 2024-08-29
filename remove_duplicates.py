# task url: https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        sets = set(nums)
        nums.clear()
        nums.extend(list(sets))
        nums.sort()
        return len(sets)
