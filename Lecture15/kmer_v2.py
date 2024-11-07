#!/usr/bin/python3

def kmer(sequence, k=2, n=2, o=1): #where k is kmer size, n is minimum frequency, o is window offest
    len_sequence = int(len(sequence))
    starting_positions = list(range(0,len_sequence,o)) #list all starting positions of each kmer
    created_segments = [] #start a new list of created kmers
    for seg_start in starting_positions:
        if (seg_start+k)<len_sequence+1: #do not include any kmers that go over the end of the sequence
            temp_seg = sequence[seg_start : seg_start+k].upper()
            created_segments = created_segments+[temp_seg]
            #print(temp_seg)
    options = set(created_segments) # create a non-redundant list of all created segments
    for seq in options:
        count = created_segments.count(seq)
        if count > n:
            print(seq, "occurs", count, "times")

test_seq = str(input("What is the sequence of interest? "))
test_kmer = int(input("What is the kmer length? "))
test_freq = int(input("What is the threshold frequence of kmers found? "))

test = kmer(test_seq, test_kmer, test_freq)

