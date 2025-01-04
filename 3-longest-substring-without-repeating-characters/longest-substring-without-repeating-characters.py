class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Dictionary to store the last index of each character
        char_index_map = {}
        left = 0 
        max_length = 0  
        
        for right in range(len(s)):
            # If the character is already in the map and its index is >= left, move left pointer
            if s[right] in char_index_map and char_index_map[s[right]] >= left:
                left = char_index_map[s[right]] + 1
            
            # Update the last seen index of the character
            char_index_map[s[right]] = right
            
            # Calculate the window size and update the max length
            max_length = max(max_length, right - left + 1)
        
        return max_length
