#nothing to run here, just the BloomFilter class definition 

import bitarray
import mmh3
import math

class BloomFilter():
    def __init__(self, input_size, fpp):
        """input_size - int - number of expected inputs
        fpp - float - false positive probability"""
    
        self.fpp = fpp
        
        #set up the bitarray but getting size, initializing, and setting all entries to 0
        self.bitarray_size = self.set_size_bitarray(input_size, self.fpp)
        self.BF_array = bitarray.bitarray(self.bitarray_size)
        self.BF_array.setall(0)
        
        #set number of hash functions
        self.hash_num = self.how_many_hash(self.bitarray_size, input_size)
        
    def set_size_bitarray (self, n, p):
        #known equation for computing size of bitarray based `on (# items input) and p (prob of false positive)
        m = -(n * math.log(p))/(math.log(2)**2)
        return int(m) 
    
    def how_many_hash(self, m, n):
        #known equation for computing how many hash functions based on m (size of bitarray) and n (# items input)
        k = (m/n)*math.log(2)
        return int(k)
        
    def add (self, item):
        """record item as present"""
        for i in range(self.hash_num):
            #i is the seed for each different hashfunction  
            hc = mmh3.hash(item, i)
            
            #gets "bucket" it should map into aka bit in the bitarray 
            location = hc % self.bitarray_size
            
            #set that bucket aka bit to True 
            self.BF_array[location] = True
    
    def is_present (self, item):
        """check to see if item is present, remember false positive possible"""
        for i in range(self.hash_num):
            hc = mmh3.hash(item, i) #i is the seed which triggers different hash functions 
            location = hc % self.bitarray_size 
            
            #now check if that spot in the bitarray is false
            if self.BF_array[location] == False:
                return False 
            
        #if no spots come back false, then item is assumed to be present
        return True
        
        
    
    
