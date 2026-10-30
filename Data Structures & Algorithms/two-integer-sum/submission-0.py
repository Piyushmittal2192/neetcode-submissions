class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        # a + b = Target
        # given a value like 4 if Target - 4 is already seen
        # then we have identified the two numbers that sum 
        # to target

        # in the hashmap i will store number which is already checked and the index of that number
        
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in hash_map:
                return [hash_map[dif], i]
            hash_map[nums[i]] = i
        return []