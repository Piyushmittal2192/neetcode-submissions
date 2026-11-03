class Solution:
    def isPalindrome(self, s: str) -> bool:
        # palindrom: reads strings same forward and backward
        # case insensitive and ignores non alpha characters

        # two pointer approach 
        # left pointer -> at the start of the string
        # right pointer -> at the end of the string

        # compare the left and right pointer characters
        # if the characters are same then the increament left and decrement right to iteratively check the chanracters of the string
        # if the character is non alpha then ignore it by inrementing and decrementing the left/right pointers respectively
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left +=1
            while left < right and not s[right].isalnum():
                right -=1

            if s[left].lower() == s[right].lower():
                left +=1
                right -=1
            else:
                return False
        return True

        