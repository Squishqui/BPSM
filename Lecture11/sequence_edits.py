#!/usr/bin/python3

sequence = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

#Count the number of A's and T's and add them together
a_count = sequence.count("A")
t_count = sequence.count("T")
a_t_total = a_count + t_count

#print(a_count, t_count)
#print(a_t_total)

#find the total length of the sequence
sequence_length = len(sequence)

#find the percentage of A's and T's in the sequence
a_t_percentage = (a_t_total/sequence_length)*100
print("The percentage of A's and T's in the provided sequence is", a_t_percentage)

#Use find and replace to replace all A's with T's, T's with A's, C's with G's, and G's with C's
#We are converting to lowercase letter so that next steps don't interfere with already replaced letters
Seq1 = sequence.replace("A","t")
Seq2 = Seq1.replace("T","a")
Seq3 = Seq2.replace("C","g")
Seq4 = Seq3.replace("G","c")

#print as upper case
print(Seq4.upper())

motif = "AATTC"

#find the position of the motif in the sequence
cut_site = sequence.find(motif)
#print(cut_site)

splice1 = sequence[0:cut_site]
splice2 = sequence[cut_site:len(sequence)]
#print(splice2)
#print("First fragment has sequence", splice1, \
#        "Second fragment has sequence", splice2) 
print("The length of the second fragment is", len(splice2))
