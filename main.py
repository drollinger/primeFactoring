import gmpy
import math

class newValOp:
    def __init__(self, total = 0, vals = []):
        self.total = total
        self.vals = vals
    def __str__(self):
        return 'tot: ' + str(self.total) + ' val: ' + str(self.vals)
    
class option:
    def __init__(self, digs = [], valOptions = [], borrow = 0):
        self.digs = digs
        self.valOptions = valOptions
        self.borrow = borrow
        
class dualOptionObj:
    def __init__(self, highDigs = [], highValOptions = [], highBorrow = 0,
            lowDigs = [], lowValOptions = []):
        self.highOption = option(highDigs, highValOptions, highBorrow)
        self.lowOption = option(lowDigs, lowValOptions, 0)
    def update(self, highDig, highValOptions, highBorrow,
            lowDig, lowValOptions):
        self.highOption.digs.append(highDig)
        self.highOption.valOptions = highValOptions
        self.highOption.borrow = highBorrow
        self.lowOption.digs.append(lowDig)
        self.lowOption.valOptions = lowValOptions
    def __str__(self):
        s = "DUAL OPTION PRINT\n"
        s += "highdigs: " + str(self.highOption.digs) + "\n"
        s += "highValOptions: "
        for op in self.highOption.valOptions:
            s += str(op) + ", "
        s += "\nhighborrow: " + str(self.highOption.borrow) + "\n"
        s += "lowdigs: " + str(self.lowOption.digs) + "\n"
        s += "lowValOptions: "
        for op in self.lowOption.valOptions:
            s += str(op) + ", "
        return s
    #def __str__(self):
    #    s = "DUAL OPTION PRINT\n"
    #    s += "highdigs: " + str(self.highOption.digs) + "\n"
    #    s += "lowdigs: " + str(self.lowOption.digs) + "\n"
    #    return s
        

def detValues(option):
    cDig = len(option.digs)
    nDig = cDig + 1
    posOpt = {}
    for valOp in option.valOptions:
        rTot = valOp.total
        mul = 2*valOp.vals[0]*(10**cDig)
        for i in range(1, (cDig//2)+1):
            if (i == nDig//2):
                rTot += (valOp.vals[i]**2)*(10**cDig)
            else:
                rTot += 2*valOp.vals[i]*valOp.vals[cDig - i]*(10**cDig)
        for i in range(0, 10):
            tot = i*mul + rTot
            pos = (tot//(10**cDig)) % 10
            v = newValOp(tot, valOp.vals+[i])
            if (pos in posOpt):
                posOpt[pos].append(v)
            else:
                posOpt[pos] = [v]
    return posOpt

def solve(dualOptions, sp, cDig, maxDig, fullsp):
    print("current digit: " + str(cDig))
    print("length of options: " + str(len(dualOptions)))
    newDualOptions = []
    for dualOption in dualOptions:
        #print(dualOption)
        hpVals = detValues(dualOption.highOption)
        lpVals = detValues(dualOption.lowOption)
        for hp in hpVals:
            for lp in lpVals:
                pval = hp-dualOption.highOption.borrow - lp
                newBorrow = 0
                while (pval < 0): 
                    pval += 10
                    newBorrow += 1
                if (sp[cDig] == pval):
                    newDualOption = dualOptionObj(dualOption.highOption.digs+[hp], hpVals[hp], newBorrow, dualOption.lowOption.digs+[lp], lpVals[lp])
                    newDualOptions.append(newDualOption)
    if (cDig >= maxDig):
        sol(newDualOptions, fullsp, maxDig)
    else:
        solve(newDualOptions, sp, cDig+1, maxDig, fullsp)

def solver(sp, maxDig):
    bsp = sp
    arSp = []
    while (sp > 0):
        arSp.append(sp % 10)
        sp = sp//10
    print(arSp)
    
    newDualOptions = []
    hpVals = {
              #0: [newValOp(0, [0])],
              1: [newValOp(1, [1]), newValOp(81, [9])],
              4: [newValOp(4, [2]), newValOp(64, [8])],
              9: [newValOp(9, [3]), newValOp(49, [7])], 
              6: [newValOp(16, [4]), newValOp(36, [6])],
              5: [newValOp(25, [5])]
             }
    lpVals = hpVals
    for hp in hpVals:
        for lp in lpVals:
            pval = hp - lp
            newBorrow = 0
            while (pval < 0): 
                pval += 10
                newBorrow += 1
            if (arSp[0] == pval):
                newDualOptions.append(
                    dualOptionObj([hp], hpVals[hp], newBorrow, [lp], lpVals[lp]))
    return solve(newDualOptions, arSp, 1, maxDig, bsp)
    

def sol(allOptions, sp, md):
    lastdigs = []
    for o in allOptions:
        for l in o.highOption.valOptions:
            a = 0
            dig = 0
            for d in l.vals:
                dig += d*(10**a)
                a += 1
            lastdigs.append(dig)
    s = gmpy.sqrt(sp)//(10**(md+1))
    done = False
    #print(lastdigs)
    print(len(lastdigs))
    while (not(done)):
        for d in lastdigs:
            if (gmpy.is_square((((s*(10**(md+1))) + d)**2) - sp)):
                print("DONE:")
                print((((s*(10**(md+1))) + d)))
                done = True
        s += 1


sp = 7231545961 * 55433902591
dig = int(math.log10(gmpy.sqrt(sp))) - 3
print(dig)

solver(sp, dig)
                    
