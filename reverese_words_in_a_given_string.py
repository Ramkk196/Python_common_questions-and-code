
 # Input:
# S = i.like.this.program.very.much
# Output: much.very.program.this.like.i
# Explanation: After reversing the whole
# string(not individual words), the input
# string becomes
# much.very.program.this.like.i
# original question :https://www.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card


class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
       list1=list(s.split("."))
       list1.reverse()
       S=".".join(list1)
       return S
