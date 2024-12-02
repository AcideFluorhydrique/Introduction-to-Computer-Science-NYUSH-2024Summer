#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 09:32:47 2019

@author: xg7
"""



# You will complete the Contacts class, which is essentially 
# a hash table for storing contacts and their phone numbers. 
# Specifically, the Contact class has a set of buckets and a hash function. 
# It uses the hash function to convert the contact's name to the label of a 
# bucket and then stores the contract's information in the bucket. 
# When one needs to retrieve the information, he/she can input the name of the contact, 
# and it will return the information. 

"""
It has four methods:

    __init__: the method for initializing an instance of the Contacts class. 
                It has two attributes:

        self.buckets: it is a list of “buckets”; a bucket is a list, 
                    and its elements are the contacts' information, 
                    which is a tuple of (name, phonenumber). 
        self.numBuckets is a variable that represents the number of buckets. 
                    You need to specify a number for it when creating an 
                    instance of the Contacts class.
    
    _hash: it is the hash function. In this case, it returns the remainder 
            of sumNameUnicode/numBuckets, where sumNameUnicode is the sum of 
            the Unicode of each character in the name, and numBuckets is the number 
            of buckets.
    
    addEntry appends the tuple (name, phone number) to a bucket in self.buckets. 
            The hash function computes the bucket's index (i.e., the label).
    
    getValue: it returns the phone number of the input name.

"""


class Contacts:
    """
    A class for storing contacts and their phone numbers
    You can refer the textbook: [MIT text], 
    Introduction to Computation and Programming Using Python 
    Chapter 10.3 Figure 10.7
    """

    def __init__(self, numBuckets):
        """Create an empty dictionary"""
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])
        return

    def _hash(self, name):
        """Convert the name to the label of a bucket
        1. get the unicode of each character in the name[hint: you can use ord()]
        2. compute the remainder of (the_sum_of_all_unicodes/the_number_of_buckets)
        3. return the remainder 
        """
        # insert your code here
        sumNameUnicode = 0
        for i in name:
            sumNameUnicode += ord(i)
        
        numBuckets = len(self.buckets)
        return sumNameUnicode % numBuckets

    def addEntry(self, name, phoneNumber):
        """adding the contact information to a bucket. 
        1.find the label of the bucket;
        2.append the (name, phoneNumber) to it.
        """
        # insert your code here
        index = self._hash(name)
        self.buckets[index].append((name,phoneNumber))
        return

    def getValue(self, name):
        """retrive the contact information
        1. find the bucket where the name is stored
        2. get the phone number of the name in the bucket; 
           if there is collision, take the phone number 
           of the first element in the bucket.
        """
        bucketIndex = self._hash(name)
        for contact in self.buckets[bucketIndex]:
            if contact[0] == name:
                return contact[1]
        return None
        
        


# no need to modify the following code
# But please read them carefully so that you will know what you need to do.
if __name__ == "__main__":

    import random

    random.seed(100)

    celebrities = ["John Lennon", "Paul MaCartney", "George Harrison",
                   "Ringo Starr", "Michael Jackson", "Kim Kardashian",
                   "John Snow", "Arya Stark", "Daenerys Targaryen",
                   "Tyrion Lannister", "Jaime Lannister", "Sansa Stark",
                   "Petyr Baelish", "Lord Varys", "Hodor", "Ygritte",
                   "Gilly", "Davos Seaworth", "Cersei Lannister",
                   "Khal Drogo", "Bran Stark", "Theon Greyjoy"]

    # code for generating the my contacts
    # the elements in myContacts are lists of [name, phone numbers]
    myContacts = []
    for name in celebrities:
        phone = random.choice(range(10**5))
        myContacts.append([name, phone])

    print("My contacts are:\n", myContacts)

    # build an instance of Contacts
    numOfBucket = 17
    D = Contacts(numOfBucket)
    for contact in myContacts:
        D.addEntry(contact[0], contact[1])

    # print("\n", "The buckets are:")
    # for hashBucket in D.buckets:
    #     print(' ', hashBucket)
    print("The phone of Tyrion Lannister is ", D.getValue("Tyrion Lannister"))
