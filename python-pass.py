
def find(s):
 
  string_word = ""
  max_repeat = s[0];
  

  length= len(s)  

  for i in s:
    num = s.count(i)

    if s.count(max_repeat) < num:
      max_repeat = i 
      
 
  for i in range(length):
    if(s[i] == max_repeat):
      for j in range(i,length):
        
        if(string_word.count(max_repeat) < s.count(max_repeat)):
         
          string_word += s[j] 
          print(string_word.count(max_repeat))

  print("the longest Palindromic =  ",string_word)

x = input("enter the string: ")
find(x)
