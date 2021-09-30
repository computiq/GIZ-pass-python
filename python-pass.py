#TASK2!!!

#definition a function for find the longest Palindromic
def find(s):
  #define a string variable that represnt the longest Palindromic which it found in end
  longestPalindromic = ""
  
  #define a variable called length , and the value of it is equal to the length of substring..
  length= len(s)  #using len() function to take the length...
  
  for i in s:     #start for loop, to move on evry letter of substring
    check=i       #the variable "check" represant the letter which checking
    
    #num variable represant the number of letter repetition in the substring
    num = s.count(check,0,-1)   #use count function to find letter repetition
    
    #If the letter is repeated more than once
    if  num>1:
        longestPalindromic +=i
    
    #If the substring is two or less characters long, and the letter is repeated once or less
    elif length <= 2 and num<=1:
          longestPalindromic+=i
          break
    else:
          pass
  print("the longest Palindromic = ",longestPalindromic)


s = input("enter the substring:")
find(s)
