class Solution:
    def isPlaindrome(self, num):
        strNum = str(num)
        return strNum == strNum[::-1]
    
    def superpalindromesInRange(self, left: str, right: str) -> int:
        leftNum = int(left)
        rightNum = int(right)

        superPalindromeCount = 0
        
        #Since the max number is 10**18 so its sqrt will be of 10**9.
        #Any number greater than 10**9 will have its squre greater than 10**18.
        #So we just need to find all the palindromes in [1, 10**9] and check whose squares are also palindrome..
        #If we try to find all the palindromes in [1, 10**9] then it will be a very lengthy task.
        #So its better to create all the palindromes in [1, 10**9] 

        #Even length palindromes
        for i in range(1, 100001):
            strI = str(i)
            palindrome =  strI + strI[::-1]
            palindromeSqr = int(palindrome)**2
            if palindromeSqr > rightNum:
                break
            if palindromeSqr >= leftNum and self.isPlaindrome(palindromeSqr):
                superPalindromeCount +=1

        #Odd length palindromes
        for i in range(1, 100001):
            strI = str(i)
            palindrome =  strI + strI[len(strI) -2::-1] if len(strI) > 1 else strI
            palindromeSqr = int(palindrome)**2
            if palindromeSqr > rightNum:
                break
            if palindromeSqr >= leftNum and self.isPlaindrome(palindromeSqr):
                superPalindromeCount +=1
        
        return superPalindromeCount