class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x<0):
            return False
        
        if (x==0):
            return True
        stack = []
        
        while(x!=0):
            if((x%10) in stack):
                if(stack[len(stack)-1]!=(x%10)):
                    return False
                else:
                    stack.pop()
            else:
                stack.insert(-1, x%10)
            
            x = x//10
        
        return True