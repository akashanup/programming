"""
# Intuition
The main idea is to first ignore all existing dashes since they are not needed in the final formatting. After removing them, we convert all characters to uppercase so the final license key follows the required format.
To create groups of size k, it is easier to process the string from the end because every group except possibly the first one must contain exactly k characters.
# Approach
1. Replace all '-' characters with '' from the string.
2. Convert the resulting string to uppercase.
3. Start creating groups of size k from the end of the string.
4. Store each group in a list.
5. Add the remaining characters (if any) as the first group.
6. Reverse the list because groups were collected from right to left.
7. Join all groups using '-'.
# Complexity
- Time complexity: $$O(n)$$. We traverse the string a constant number of times.

- Space complexity: $$O(n)$$. Extra space is used to store the cleaned string and the groups.

"""

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:        
        # Remove dashes and convert to uppercase
        cleaned = s.replace("-", "").upper()
        
        # Store groups
        groups = []
        
        # Create groups from the end
        while len(cleaned) > k:
            groups.append(cleaned[-k:])
            cleaned = cleaned[:-k]
        
        # Add remaining characters
        groups.append(cleaned)
        
        # Reverse because we built from the end
        return "-".join(groups[::-1])
