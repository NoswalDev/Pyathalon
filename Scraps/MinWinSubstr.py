class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #case for shortness
        if len(t) > len(s):
            return ""
        if s == t:
            return s
        '''     
        if doesn't contain letters: expand
        if contains letters: shrink
        check if letter in bank
        '''
        #put t in dict
        bank = {}
        for i in t:
            bank[i] = bank.get(i,0) + 1
        f = 0
        e = 0
        
        outp = [0,len(s)]
        complete = 0
        while f < len(s):
            #process F
            if s[f] in bank:
                bank[s[f]] = bank[s[f]] - 1
                if bank[s[f]] == 0:
                    complete +=1
            
            #check completion
            while complete == len(bank.keys()):
                #record
                if f - e < outp[1] - outp[0]:
                    outp[0] = e
                    outp[1] = f
                #progress E
                if s[e] in bank:
                    bank[s[e]] = bank[s[e]] + 1
                    if bank[s[e]] == 1:
                        complete -= 1
                e+=1
            f+=1
        if outp[1] - outp[0] == len(s):
            return ""
        return s[outp[0]:outp[1]+1]
        