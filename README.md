# bloomfilter_2270final

Title - Bloom Filters 2270 Final Project 

**Intro**

This project implements and explores the bloom filter data structure. Bloom filters are a probabilistic data structure which stores items similar to a hash table. They can store large data sets and enable fast insertion and lookup of items. Items are run through a series of hash functions, then hashed into an array of bit integers, and the presence or absence of the item is stored rather than the item itself. Bloom filters support insertion and lookup functions. Upon insertion, each item is run through multiple hash functions and the mod operator then maps that value to a corresponding bit in the bit array. So each time a hash function is run, a bit in the bitarray becomes marked as true. Later if we go to search whether an item is presence, we need only do some quick hash calculations and if all corresponding bits are marked true then we assume that item is present. Deletion is not possible from a bloom filter because it is possible that two or more entries overlap with which bits are marked true and to delete one would also invalidate the other(s).

False positives - one thing that must be noted when talking about bloom filters is the possibility of false positives. A false positive would occur if an item entered into the lookup function happens to hash to values that have already been marked as true from other entries. In this case, it would appear that the item is present when it is not. For this reason, bloom filters should be used strategically in situations where a false positive would not be catastrophic. On the other hand, a false negative is never possible since all bits start at 0 and only become true if something hashes to them. Again, used strategically, this is an advantage of a bloom filter. 

Probability is an important aspect to bloom filters since we want to be able to "control" the prevalence of false positives. Based on the desired probability of a false postiive, the bloom filter should set up with an appropriately sized bit array and number of hash functions. In the notebook file titled "Walthrough", I explain the equations involved in calculating these values. 

An example of a real world application of a bloom filter is a username database. When users are attempting to create a new account, they must chose a username. That potential username needs to be quickly run against the large database of existing usernames to determine whether or not its available. In this scenario speed is important and presence/absence is the only thing that matters, so a bloom filter is the perfect application. It also is not really a problem if we get a false positive - the worst case scenario is someone doesn't get the username they wanted but no real harm is done. And on the other hand, a negative result can be trusted and that system can know for sure that proposed username is available. 

Complexity - Bloom filters have a space complexity of O(m) where m is the length of the bit array. The time complexity of both insertion and lookup is O(k) where k is the number of hash functions. This is a very fast lookup time for a potentially very large dataset.


**Project Summary**

Some notable feautres of this project:
- bloomfilter.py contains all the class information to set up a bloom filter
- bloomfilter_tests.py contains code testing functionality of the filter 
- walthrough.ipynb is a notebook file which contains 
    1. discussion of python modules used
    2. bloom filter equation breakdown 
    3. probability exploration
    4. walkthrough of program using the example scenario of an extensive book collection 
    5. reflection 
    
**Instructions to Run **

The walkthrough notebook file includes a section which shows how the bloom filter class and functions can be utilized. You're welcome to run this yourself and adjust the inputs or just observe the scenario I ran (you might have to install some modules). Same for the probability section - feel free to alter the probability and input sizes. The bloomfilter_tests file can also be run. I entered a preset input (n), probability (p), and number of trials, but you're welcome to enter your own values here. 