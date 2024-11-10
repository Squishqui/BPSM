#!/usr/bin/python3
import os

def kmer(sequence, k=2, n=2, o=1): #where k is kmer size, n is minimum frequency, o is window offest
    if k > len(sequence) :
        return "Sorry, your kmer length is longer than your DNA (" + str(len(sequence)) +" bases)." 
    if k < 2 or k > 50 :
        return "Sorry, inappropriate kmer length, only 2 to 50 accepted here."
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

#ask the user for inputs
test_seq = str(input("What is the sequence of interest? "))
if test_seq:
    test_kmer = int(input("What is the kmer length? ") or 2)
    #if the kmer length provided is silly, reset to the default
    if (test_kmer < 2 or test_kmer >= len(test_seq) or test_kmer > 50):
        test_kmer = 2
        print("Inappropriate value chosen, resetting to 2")
test_freq = int(input("What is the threshold frequence of kmers found? "))
#run the function
test = kmer(test_seq, test_kmer, test_freq)


myfilename="kmerouts"+"_KMER"+str(test_kmer)+"_MIN"+str(test_freq)+".txt"
outputfilepipe = open(myfilename,"w")

print("Results:\n")
print(test)

outputfilepipe.write("### Kmer analysis\n#SQ "+str(test_seq)+"\n#KMER "+str(test_kmer)+"\n#MIN "+str(test_freq)+"\n")

if test is not None:
    for freqseq in test :
        outputfilepipe.write(str(freqseq)+"\n")

outputfilepipe.write("\n")
outputfilepipe.close()

print("\n\nContents of the output:\n")

syscmd="cat " + myfilename
os.system(syscmd)
