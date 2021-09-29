class Soulution:
    @staticmethod
    def longestpalindrome (self, s:str) ->str:
        
        def holder(l,r):
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            return s[l+1 : r]
        result = ""
        for i in range(len(s)):
            test = holder(i,i)
            if len(test) > len (result): result = test
            
        return result
    def results(self, s:str) :
        
        answer = Soulution().longestpalindrome()
        print (answer)
        results("babad")
