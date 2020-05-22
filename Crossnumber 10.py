# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 10:26:50 2019

@author: setat
"""

import numpy as np

int2list = lambda x: [str(x)[i] for i in range(len(str(x)))]
int2intlist = lambda x: [int(str(x)[i]) for i in range(len(str(x)))]
digsum = lambda n: sum([int(i) for i in int2list(n)])

# =============================================================================
# 1A: 9 times this number is an anagram of this number [5]
# =============================================================================

a1 = []
a1len = 5
for i in range(int('1'+(a1len-1)*'0'),int('1'+(a1len)*'0')//9+1):
    anag = np.unique(int2list(i),return_counts=True)
    ninex = np.unique(int2list(9*i),return_counts=True)
    if np.array_equal(anag,ninex):
        print(i,9*i)
        a1.append(i)
print(len(a1)) # 5

# =============================================================================
# Palindromes
# =============================================================================

def palindromes(n):
    """Generate list of all palindromes of length n"""
    palins = []
    for i in range(int('1'+(n-1)*'0'),int('1'+n*'0')):
        if str(i) == str(i)[::-1]:
            palins.append(i)
    return palins
print(palindromes(3))
print(len(palindromes(7)))

# =============================================================================
# 17D: sum(digits of 17D) = (17D[0])^2 [5]
# =============================================================================

d17min = 10000
d17max = 99999

d17 = []
for i in range(d17min,d17max+1):
    i_list = int2intlist(i)
    if sum(i_list) == int(i_list[0])**2:
        d17.append(i)
print(len(d17)) # 1227

# =============================================================================
# 6D - side length for a triangle with hyp 2665 and with int length sides [4]
# =============================================================================

d6 = []
d6len = 4
d6hyp = 2665
for i in range(d6hyp):
    for j in range(i,d6hyp):
        if i**2 + j**2 == d6hyp ** 2:
            print(i,j)
            d6.append(i)
            d6.append(j)
d6 = [i for i in d6 if len(str(i)) == d6len]
d6first = set([str(i)[0] for i in d6]) # 1 or 2
d6second = set([str(i)[1] for i in d6]) # all digits, dammit
d6 = [i for i in d6 if str(i)[1] != "0"]
print(len(d6)) # 18

# =============================================================================
# 7D and 8D: Solutions of x^2 - (50D)*x + (11A) = 0 [2][2]
# 50D: More than 8D [2]
# 11A: A multiple of 8D [3]
# =============================================================================

quad = lambda a,b,c: (
        (-b+np.sqrt(b**2 - 4*a*c))/(2*a),
        (-b-np.sqrt(b**2 - 4*a*c))/(2*a)
        )
# solutions are ints => (50D)^2 > 4*(11A)
# => (50D)^2 > 4*(11A) > 4*100 = 400
# => 50D >= 20
# solutions are ints => b**2-4ac is a square
# in this ex, a=1 => b**2-4*c is a square

# b^2-4c < 99*2 = 9801 (if b is two digits)
d78_sq = [i**2 for i in range(99)]

d78 = []
for b in range(20,100):
    for c in range(100,1000):
        if (b**2-4*c) in d78_sq:
            d78.append([(b,c),quad(1,-b,c)])

print(len(d78)) # 1314

# Both roots 7D and 8D are 2 digits
d78 = [el for el in d78 if el[1][0]>=10 and el[1][1]>=10] # 744
# 11A is a multiple of 8D
d78 = [el for el in d78 if ((el[0][1]%el[1][0])==0 or (el[0][1]%el[1][1])==0)]
# len is exactly the same - not surprising! as
# (x-x1)(x-x2)=x^2-(x1+x2)+(x1*x2) i.e. one coeff is the sum, one is the product
# + 50D (cf 11A) adds no info - it's a sum of the roots, of course it's bigger

# 3A => 7D[1] == 8D[1]
d78 = [el for el in d78 if str(int(el[1][0]))[0]==str(int(el[1][1]))[0]] # 116
# 6D => they = 1 or 2
d78 = [el for el in d78 if int(str(int(el[1][0]))[0]) in [1,2]] # 110

# N.B. 11A crosses 7D and 8D
# 11A[1] = 7D[1], 11A[2] = 8D[1]
d78_2 = []
for el in d78_4:
    c = max(el[0])
    x1 = int(el[1][0])
    x2 = int(el[1][1])
    if set(int2list(c)[1:]) == set([str(x1)[1],str(x2)[1]]):
        d78_2.append(el)
d78 = [x for x in d78_2] # 12!

# 6D[1]=11A[0]=1 => given remaining roots, 7A[0]=8A[0]=1 => 6D[0]=1
[x for x in d6 if str(x)[:2] == '11'] # empty
# => 6D[1]=11A[0]!=1
d78 = [el for el in d78 if str(max(el[0]))[0] != '1'] # 2!!

# 50D = 40 or 52. 50D=40 => 52A=000000000000000
# => 50D=52
d78 = [el for el in d78 if el[0][0]==52] # finished!
# [[(52, 675), (27.0, 25.0)]] == 50D, 11A, 7D, 8D

# => 11A[0] = 4 or 6 => 7A[0]=8A[0]=2 => 6D[:2] = 24 or 26
d6 = [el for el in d6 if str(el)[:2]=='24' or str(el)[:2]=='26'] # 5 left
# Last number starts a new number => can't be 0
d6 = [el for el in d6 if str(el)[-1] != '0'] # 3 left
# 11A = 675
d6 = [el for el in d6 if str(el)[1] == '6'] # 2

# =============================================================================
# 44D: 1 more than a palindrome [4]
# =============================================================================

# Last digit is 2
d44 = [el+1 for el in palindromes(4)]
d44 = [el for el in d44 if str(el)[-1]=='2'] # 10 options

# =============================================================================
# 43A: 25A reversed [3]
# 25A: diff(31D,15A) [3]
# 15A: 31D reversed [3]
# => 25A = diff(31D,31Dreverse)
# 31D = digsum=7 [3]
# =============================================================================

d31 = [n for n in range(100,1000) if digsum(n)==7]
#31D's last digit is 4 or 5 => 31D=115,124,214
d31 = [n for n in d31 if int2list(n)[-1] in ['4','5']]
d31 = [n for n in d31 if int2list(n)[1] != '0'] # as it starts another num
messed_up = {'31D': d31}
messed_up['15A'] = [int(str(n)[::-1]) for n in messed_up['31D']]
messed_up['25A'] = [a-b for (a,b) in zip(messed_up['15A'],messed_up['31D'])]
messed_up['43A'] = [int(str(n)[::-1]) for n in messed_up['25A']]

# 43A[-1] = 1 from 44D
a43 = [el for el in messed_up['43A'] if str(el)[-1] == '1'] # 1!
for k in messed_up.keys():
    print(k,messed_up[k][messed_up['43A'].index(a43[0])]) # get the assoc els
#31D 214
#15A 412
#25A 198
#43A 891
    
# => 6D[-1] = 4
d6 = [el for el in d6 if str(el)[-1]=='4'] # 1: 2664

# =============================================================================
# 21A: HCF of 26A and 34A [2]
# 26A: HCF of 21A and 34A [2]
# 34A: HCF of 21A and 26A [2]
# =============================================================================

# They're all equal??
for a in range(10,100):
    for b in range(a,100):
        for c in range(b,100):
            if b//a==b/a and c//b==c/b and a//c==a/c:
                print(a,b,c)
# Confirmed
                
# 34A[0]=1 => 21A[0]=26A[0]=1
                
# =============================================================================
# 16D: Each dif is either the sum or diff of the digits on either side [6]
# 17D: digsum = square of 17D[0] [5]
# =============================================================================

# 17D[0]=2 => digsum(17D)=4
d17 = [d for d in range(10000,100000) if digsum(d)==4 and int2list(d)[0]=='2']

#17D[1]=21A[1], 17D[3]=26A[1]. 21A=26A => 17D[1]=17D[3]
d17 = [d for d in d17 if int2list(d)[1]==int2list(d)[3]]
# [20002, 20101, 20200, 21010]
# => 34A[1]=26A[1]=21A[1] in [0,1] => 16D[-1] in [0,1]
# By direct calc, 16D=[1][1][02][1][13][01]
# 3 isn't the sum or diff of 1,1 => 16D[-1] = 0
# => 34A=21A=26A=10

# 17D rule => as 17D ends ....21?, it has to end 211 => 17D ends 1
d17 = [d for d in d17 if int2list(d)[-1]=='1']
# 20101
# => 16A's missing dig is a 0, to fulfil 23A's rule

# =============================================================================
# 23A: Each dig is one more or three less than the previous dig [9]
# 51A: digsum of 23A [2]
# =============================================================================

# 23A = ????[159][26][3][0][1]
a23 = []
for i in ['1','5','9']:
    for j in ['2','6']:
        for k in range(1000,10000):
            a23.append(str(k)+i+j+'301')
#54000
a23 = [int(d) for d in a23 if 10<=digsum(int(d))<100] # 53995

passed = []
for m in a23:
    trial = int2intlist(m)
    trialb = []
    for i in range(1,len(trial)):
        if trial[-i] != trial[-(i+1)]+1 and trial[-i] != trial[-(i+1)]-3:
            break
        trialb.append(trial[-i])
    if trial == [trial[0]] + trialb[::-1]:
        passed.append(m)
a23 = passed # 28
a51 = [digsum(i) for i in a23]

# =============================================================================
# 37A: Diff between 49A and 13A [3]
# 13A: 49A reversed [3]
# => 37A = diff(49A, 49Areverse)
# 49A: Each digit is strictly less than the prev [3]
# 47A: 37A reversed [3]
# 48A: 47A+37A [4]
# => 48A = 37A+37Areverse
# =============================================================================




# 10A: Not 32A or 40A [2]
# 24A: Not 32A or 40A [2]
# 32A: HCF of 10A and 24A [2]
# 40A: LCM of 10A and 24A [2]

