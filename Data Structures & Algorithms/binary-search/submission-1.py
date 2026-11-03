class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # numbers are sorted, identify if Target exist in nums, return true if exist else False

        # two pointers

        left = 0
        right = len(nums) - 1

        while left <= right:
            #mid_value = (nums[left] + num/s[right]) // 2
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1