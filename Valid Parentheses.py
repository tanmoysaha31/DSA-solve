class Solution:
    def isValid(self, s):
        opn=["(","{","["]
        clos=[")","}","]"]
        stack=[]
        top=-1
        if len(s)==0 or len(s)%2!=0:
            return False
        for i in s:
             if i in opn:
                stack.append(i)
                top+=1
             elif i in clos:
                    if top==-1:
                        return False
                    idx=clos.index(i)
                    if stack[top]==opn[idx]:
                        stack.pop()
                        top-=1
                    else:
                        return False
             else:
                return False

        if len(stack)==0:
            return True
        else:
            return False