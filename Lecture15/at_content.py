#!/usr/bin/python3

#defining our variable to be called later
def get_at_content(some_dna, sig_figs=2):
    length = len(some_dna)
    a_count = some_dna.upper().count('A')
    t_count = some_dna.upper().count('T')
    at_content = (a_count + t_count) / length
    return round(at_content, sig_figs)

#test/assert our function with a condition that we know the answer to
#for base in 'gatcxn':
#    print("Was A or T? "+base.upper() + ": " + str(get_at_content(base) == 1))
assert get_at_content("A") == 1
assert get_at_content("T") == 1
assert get_at_content("C") == 0
assert get_at_content("G") == 0
assert get_at_content("AAA") == 1

#what is our input?
#my_dna = "actgatacatatatatcgatgcgttcat"
dna2 = open('dna2.txt').read()

#encapsulation our output with the new function
with open('output.txt','w') as result:
    result.write(str(get_at_content(dna2, 4)))

#give an output to the screen
print(open("output.txt").read())
