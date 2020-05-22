# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 03:08:56 2019

@author: setat
"""

import numpy as np
import pandas as pd
from itertools import permutations
import re


#24D = 23D
#23D = np.sqrt(30A-1)
#30A = 2 * (12A**4)

# =============================================================================
# 14A The product of the digits of this number is 70. (4)
# =============================================================================

70 == 2*5*7
# 4 digits => 1 digit has to be 1

A14 = list(permutations([1,2,5,7])) 
print(A14)

# =============================================================================
# 27A, 28A, 39D, 44A This number is equal to the sum of the cubes of its digits (3)
# =============================================================================

D39_num = list(range(100,1000))
D39_cub = [int(str(i)[0]) ** 3 + int(str(i)[1]) ** 3
           + int(str(i)[2]) ** 3 for i in D39_num]
D39_check = [D39_num[i] == D39_cub[i] for i in range(0,len(D39_num))]
for i in range(0,len(D39_num)):
    if D39_check[i] == True:
        print(D39_num[i])

# =============================================================================
# 18A,35A This number is equal to the sum of the fourth powers of its digits. (4)
# =============================================================================

A18_num = list(range(1000,10000))
A18_cub = [int(str(i)[0]) ** 4 + int(str(i)[1]) ** 4
           + int(str(i)[2]) ** 4 + int(str(i)[3]) ** 4 for i in A18_num]
A18_check = [A18_num[i] == A18_cub[i] for i in range(0,len(A18_num))]
for i in range(0,len(A18_num)):
    if A18_check[i] == True:
        print(A18_num[i])

# =============================================================================
# 12A, 30A, 23D
# =============================================================================

A12 = np.array([11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79,
       83, 89, 97])
A30 = (A12 ** 4) * 2
D23 = np.sqrt(A30 - 1)
A12A30 = pd.DataFrame([A12, A30, D23], index=['A12', 'A30', 'D23'])
A12A30 = A12A30.transpose()
A12A30 = A12A30.loc[(A12A30['A30'] > 9999) & (A12A30['A30'] < 100000) &
                    (A12A30['D23'] > 99) & (A12A30['D23'] < 1000)]

# =============================================================================
# 31D A prime equal to average of above and below prime (3)
# =============================================================================

primes3long = [101, 103, 107, 109, 113, 127, 131, 137, 139,
    149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227,
    229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311,
    313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401,
    409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,
    499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
    601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683,
    691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
    809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887,
    907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009]

matchprimes = []
for i in range(1,len(primes3long)-1):
    if (primes3long[i] - primes3long[i-1] == primes3long[i+1] - primes3long[i]):
        matchprimes.append(primes3long[i])
print(matchprimes)

# =============================================================================
# 1D: A multiple of 12A = 13 [6]
# =============================================================================

D1 = [13*i for i in range(7693,76923+1)]
D1_check = [str(i)[3] == '1' and str(i)[4] == '6'
             and sum(int(digit) for digit in str(i)) == 36
             and str(i)[0] == '2' for i in D1]
D1_cutdown = []
for i in range(0,len(D1)):
    if D1_check[i] == True:
        D1_cutdown.append(D1[i])
print(D1_cutdown)

# =============================================================================
# 21D: Not a multiple of 3 (6)
# =============================================================================

D21 = np.array([int(str(i) + '12339') for i in range(1,10)])
D21_div3 = D21 / 3
#D21_div3 = [isinstance(i,int) for i in D21_div3]

# =============================================================================
# 5D, 9D, 11D, 8A, 10A
# =============================================================================
A10 = set([int('6' + str(i) + '6') for i in range(1,10)]) # can't have 0 in middle
D11 = set([])
for i in range(1,10):
    for j in [1,2,7]:
        D11.add(int(str(i) + str(j) + '6'))

# Does 5D | 10A?
D5_cut = set([])
A10_cut = set([])
D5 = range(20,30)
for i in D5:
    for j in A10:
        if j % i == 0:
            D5_cut.add(i)
            A10_cut.add(j)
            #print(i,j)

D11_cut = set([])
for i in D11:
    if str(i)[0] == '1' or str(i)[0] == '7' or str(i)[0] == '9':
        D11_cut.add(i)

D5_ends = [str(i)[-1] for i in D5_cut]
A8 = set([int('8' + i) for i in D5_ends])

# Does 8A | 10A?
A8_cut = set([])
A10_cut2 = set([])
for i in A8:
    for j in A10_cut:
        if j % i == 0:
            A8_cut.add(i)
            A10_cut2.add(j)
            print(i,j)

# Fix those that are now defined
A8 = 0
A10 = 0
if len(A8_cut) == 1:
    A8 = min(A8_cut)
if len(A10_cut2) == 1:
    A10 = min(A10_cut)
D5 = int('2' + str(A8)[1])
D9 = A10

# Final one
D11_cut2 = set([])
for i in D11_cut:
    if str(i)[0] == str(A10)[1]:
        D11_cut2.add(i)
D11_cut3 = set([])
for i in D11_cut2:
    if i % A8 == 0:
        D11_cut3.add(i)
if len(D11_cut3) == 1:
    D11 = min(D11_cut3)
    
print('5D:',D5,'\n','9D:',D9,'\n','11D:',D11,'\n','8A:',A8,'\n','10A:',A10)
print('5D|10A?',A10 % D5 == 0,'\n',
      '8A|10A?',A10 % A8 == 0,'\n',
      '8A|11D?',D11 % A8 == 0,'\n')

# =============================================================================
# Last few bits
# =============================================================================

answers5 = [[35538,35838], 57122]
D40 = [int(str(33) + str(i)) for i in range(0,10)]
answers3 = set([616, 153, 371, 407, 616, 176, 605, 239, 239, 263, 370, 'D40'])
# 37D = a 3 and a 3, _34 and __9
D40 = 334
answers3.remove('D40')
answers3.add(D40)
D37_1 = D40
D37_2 = set([])
for i in answers3:
    if str(i)[-1] == '9':
        D37_2.add(i)
print(D37_2)
if len(D37_2) == 1:
    D37_2 = min(D37_2)
D37 = int(str(D37_1) + str(D37_2))
D26_2 = D37_2

# =============================================================================
# D6: A multiple of 3, digits sum to 69
# =============================================================================

D6 = []
# Sum to 69 => A25[2] can't be 2, or it can't sum to 69
# Actually can only have all 9s!
D6_check = 299968899 % 3 == 0
print(D6_check)

# => fixes all but 1 of 32A

A32 = np.array([91912292,91922292])
for i in A32:
    if i % 3 == 0:
        A32 = i

D21_check = 212339 % 3 != 0
print(D21_check)



# =============================================================================
# D2, D3, D20
# =============================================================================

D2 = []
for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            for l in range(0,10):
                D2.append(int('2' + str(i) + str(j) + str(k) + '6' + str(l) + '9'))
print(len(D2))

D20 = []
for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            for l in range(0,10):
                D20.append(int('1' + str(i) + '113' + str(j) + str(k) + str(l) + '9'))
print(len(D20))

D3 = [int('24616' + str(i) + '9') for i in range(0,10)]
D3_cut = []
for i in D3:
    if i % 3 == 0:
        D3_cut.append(i)
print(D3_cut)

# Didn't work, no idea why
#for i in D2:
#    if '0' in list(str(i)):
#        D2.remove(i)
#    elif '3' in list(str(i)):
#        D2.remove(i)
#    elif '7' in list(str(i)):
#        D2.remove(i)

D2 = [x for x in D2 if "0" not in str(x)]
D2 = [x for x in D2 if "3" not in str(x)]
D2 = [x for x in D2 if "7" not in str(x)]

D2_cut = []
for i in range(0,len(D2)):
    if (str(D2[i]).count('1') == 1) and (str(D2[i]).count('4') == 1) and (str(D2[i]).count('6') == 2) and (str(D2[i]).count('9') == 1):
        D2_cut.append(D2[i])
D2 = D2_cut

D2_D20 = []
for i in D2:
    for j in D20:
        if j % i == 0:
            D2_D20.append([i,j])
print(len(D2_D20),D2_D20)

# =============================================================================
# Totals
# =============================================================================
to_sum = [222222222222222, 88, 616,13,1725,666666666666666, 8208,91922292,35838,
          153,371,57122,91922292,1634,333333333333333,9474,74,407,64,999999999999999]
print(sum(to_sum))