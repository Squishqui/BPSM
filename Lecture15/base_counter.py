#!/usr/bin/python3

#define your function
def base_counter(seq, threshold = 10):
    print("Threshold is", threshold, "%")
    len_sequence = len(seq)
    #initialise a count
    count = 0
    #for each base in the uppercase sequence
    for base in seq.upper():
        #if base is not A, T, C, or G
        if base not in ['A', 'T', 'C', 'G']:
            count = count + 1 #count increases by 1
    #number of undetermined bases/total bases *100
    perc_undetermined = (count/len_sequence)*100
    #is the percentage above the threshold or not?
    if perc_undetermined <= threshold:
        passed_test = True
    else:
        passed_test = False
    return passed_test

print(base_counter("atucgtgractanctgactg", 50))

#assertions used to test the function, first two pass and second two fail
#assert base_counter("atcg") == True
#assert base_counter("uuuu") == False
#assert base_counter("atcg") == False
#assert base_counter("uuuu") == True

