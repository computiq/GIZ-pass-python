# Given a string s, return the longest palindromic substring in s.
#
# Example 1:
#
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
# Example 2:
#
# Input: s = "cbbd"
# Output: "bb"
#
# Example 3:
#
# Input: s = "a"
# Output: "a"
#
# Example 4:
#
# Input: s = "ac"
# Output: "a"


class Solution:

    @staticmethod
    def longest_palindromic(s: str) -> str:
        # Create a string to store our resultant palindrome
        palindrome = ''

        # loop through the input string
        for i in range(len(s)):

            # loop backwards through the input string
            for j in range(len(s), i, -1):

                # Break if out of range
                if len(palindrome) >= j - i:
                    break

                # Update variable if matches
                elif s[i:j] == s[i:j][::-1]:
                    palindrome = s[i:j]
                    break

        return palindrome
