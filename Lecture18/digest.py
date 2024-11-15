#!/usr/bin/python3
import re

#start last_cut at 0
last_cut = 0

#start number of matches at 0
match_num = 0

#create a list to store cut positions of both enzyme
all_cuts = []

#create a variable that the string of the input file is loaded into
inputfile = open("/localdisk/home/s2760053/Exercises/Lecture18/long_dna.txt").read().rstrip('\n')
print(inputfile)

#for each matching BpsmI sequence in the file, add the start position to the all_cuts list
for matching in re.finditer(r'A.TAAT',inputfile):
    all_cuts.append(matching.start()+3)

#do the same for BpsmII
for match in re.finditer(r'GC[AG][AT]TG',inputfile):
    all_cuts.append(match.start()+4)

#sort the list in sequence order
all_cuts.sort()

#for each cut in the list
for cut in all_cuts:
    match_num += 1
    #the length will be the location of the cut - last cut
    fragment_length = cut - last_cut
    print("Fragment "+str(match_num)+" size is "+str(fragment_length)+": "+str(last_cut)+" to "+str(cut))
    print(inputfile[last_cut:cut])
    last_cut = cut #iterate last_cut for next loop

#for the last cut, find the length between end of sequence and final cut
fragment_length = len(inputfile) - last_cut
match_num += 1
print("Fragment "+str(match_num)+" size is "+str(fragment_length)+": "+str(last_cut)+" to "+str(len(inputfile)))
print(inputfile[last_cut:len(inputfile)])


