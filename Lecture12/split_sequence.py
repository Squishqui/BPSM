#!/usr/bin/python
import os
os.chdir("/localdisk/home/s2760053/Exercises/Lecture12")

#Call the sequence data
sequence = open("plain_genomic_seq.txt").read()
len_sequence = len(sequence)
hira_sequence = open("hira.nuc.txt").read()
len_hira = len(hira_sequence)

#print(sequence)

#Split the local DNA sequence into the two exons and intron
exon1 = sequence[0:63]
intron = sequence[63:90]
exon2 = sequence[90:len_sequence]
#print(exon1)
#print(exon2)

#split the remote DNA sequence into the coding and noncoding sequences
hira_coding = hira_sequence[28:409]
hira_coding_len = len(hira_coding)
hira_noncoding1 = hira_sequence[0:28]
hira_noncoding2 = hira_sequence[409:len_hira]

#join the non-coding sequences together and separate by a new line
hira_noncoding = (hira_noncoding1 + hira_noncoding2)
hira_noncoding_len = len(hira_noncoding)

#write the coding sequence into hira_coding.txt file
with open("hira_coding.txt", "w+") as my_file:
    my_file.write(">AJ223353_hira_coding_len " + str(hira_coding_len) + "\n" + hira_coding)
    my_file.close()
#    print(open("hira_coding.txt").read())

#write the non-coding sequence into hira_noncoding.txt file
with open("hira_noncoding.txt", "w+") as my_file2:
    my_file2.write(">AJ223353_hira_noncoding_len " + str(hira_noncoding_len) + "\n" + hira_noncoding)
    my_file2.close()
#    print(open("hira_noncoding.txt").read())

#write exon1 into file
local_exon01_out = open("local_exon01.fasta", "w+")
local_exon01_out.write(">LocalSeq_exon01_length" + str(len(exon1)) + "\n")
local_exon01_out.write(exon1)
local_exon01_out.close()
#print(open("local_exon01.fasta").read())

#write intron into file
local_intron01_out = open("local_intron01.fasta", "w+")
local_intron01_out.write(">LocalSeq_intron01_length" + str(len(intron)) + "\n")
local_intron01_out.write(intron)
local_intron01_out.close()
#print(open("local_intron01.fasta").read())

#write exon2 into file
local_exon02_out = open("local_exon02.fasta", "w+")
local_exon02_out.write(">LocalSeq_exon02_length" + str(len(exon2)) + "\n")
local_exon02_out.write(exon2)
local_exon02_out.close()
#print(open("local_exon02.fasta").read())

# coding_filename = "coding" + str(hira_coding_len) + ".fasta"
# os.rename("hira_coding.txt", coding_filename)
