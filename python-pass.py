

"""
* Noaman Monther Mahmood
* Full-Stack Development Bootcamp  (Tasks - 1)
* Python Side 
* Use Better Comments {for better experiance with this task solution}
* https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments

"""


import helper 

class Solution:

    @staticmethod
    def longest_palindromic(s: str) -> str:
        # pass 
        # ! - Here pass is just an placeholder buse initally we don't know what the code that we are working on but we dont want an error in our code if we run this project ,
        # * so we gonna ignore it and start implement this method
        # ! lets do some validations
        if(s==""):
            return "--------\n\nOh wait!\nYou need to type someting first\ntry again\n\n--------"
        
        if(len(s)==1):
            return s

        word = ""
        for i in range(len(s)):
        # ! firstly we want to get the whole word characters 
            for j in range(len(s),i,-1):
                if s[i:j] == s[i:j][::-1]:
        # ! take a string slice of the word and compare it to its reverse to check whether thy are the same or not
                    if len(word) < len(s[i:j]):
        # * if the length of the palindromic word higher than the variable we have declared,
        # * we will assign this palindromic word to our variable and check again for longest 
                        word = s[i:j]
        
        # * whenever we finsh the process and there is no ther character in the parsed word,
        # * simply we return th longest palindromic
        return word

# d=Solution.longest_palindromic(
#         s="baba"
#     )
# print(d)

def checkingAlgorithim(s:str):
    # ! this helper method just for checking all the examples that were given inside the {README} file
    ans=Solution.longest_palindromic(
        s=s
    )
    print(ans)
# * Example 1
checkingAlgorithim('baba')
# * Example 2
checkingAlgorithim('cbbb')
# * Example 3
checkingAlgorithim('a')
# * Example 4
checkingAlgorithim('ac')

# ! this is to check our validation
checkingAlgorithim('')

# fotter= helper.Noaman()
helper.printConsoleFotter()

# ! In the end ,This not the only way to implement it, there are more ways to done it.
# print(len(""))
