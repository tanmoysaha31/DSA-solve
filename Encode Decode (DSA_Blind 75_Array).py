class Solution:
    def encode(self, strs):
        s=""

        for i in strs:
            s+="*"
            leni=len(i)
            if leni<10:
                s+=f"00{leni}"
            elif 10<=leni<100:
                s+=f"0{leni}"
            else:
                s+=f"{leni}"
            s+="#"
            s+=i
        if len(strs)<10:
            s+=f"[0{len(strs)}]"
        else:
            s+=f"[{len(strs)}]"
        print(s)
        return s
    
    def decode(self, s):
        strarr=[]
        #print(int(s[len(s)-3]))
        c=int(s[len(s)-3:len(s)-1])
        j=0
        for i in range(c):
            lenstr=int(s[j+1:j+4])
            start=j+5       
            end=start+lenstr
            word=s[start:end:1]
            strarr.append(word)
            j=end
        return strarr
        
S=Solution()
enc=S.encode(["neet","code"])
dec=S.decode(enc)
print(dec)
