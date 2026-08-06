# Find the First Non-Repeating Character in a Stream

Given an input stream of characters consisting only of lowercase alphabets.  
Find the first non-repeating character in the input string each time a new character is inserted into the stream. 
If there is no non-repeating character, then append '#' to the answer.

### Example 1
```sh
Input: "aabcbc"
Output: "a#bbc#"
Explanation: 
When the input stream is "a,"  the first non-repeating character, "a," is appended.
When the input stream is "aa,"  there is no first non-repeating character, so "#" is appended.
When the input stream is "aab,"  the first non-repeating character, "b," is appended.
When the input stream is "aabc,"  the first non-repeating character, "b," is appended.
When the input stream is "aabcb,"  the first non-repeating character, "c," is appended.
When the input stream is "aabcbc," there is no first non-repeating character, so "#" is appended.
```
