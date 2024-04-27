#you can run this file, feel free to alter n and p 

import bloomfilter
from wonderwords import RandomWord
r = RandomWord()

#number of items to be added
n = 50

# prob of false positive 
p = 0.02

mybloom = bloomfilter.BloomFilter(n,p)

print("Number of items = ", n)
print("Probability of false positive = ", p)
print("Bit array length is" , mybloom.bitarray_size)

#random input of strings 
items=[]
for i in range(n):
    items.append(r.word() + " " + r.word())
    
def basic_test(lst):
    """can you add something and then look up to see if its there"""
    for i in range(len(lst)):
        mybloom.add(lst[i])
        presence = mybloom.is_present(lst[i])
        if presence == False:
            print ("failed to add")
            return
    print("add + lookup successful")
    return
    
def fp_test(present, trials):
    '''test for false positives, does it match expected?'''
    fp=0
    for i in range(trials):
        wrd = r.word() + " " + r.word()
        if wrd not in present:
            test = mybloom.is_present(wrd)
            if test == True:
                fp += 1
    print("false positive rate is: ", fp/trials)
    return fp

#does everything insert and lookup properly?
basic_test(items)
      
#does the false positive rate match the entered probability?
fp_test(items, 100)
