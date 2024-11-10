#!/usr/bin/python3

#define the function with a default list to search for
def aa_percentage(sequence, code=['A','I','L','M','F','W','Y','V']):
    seq_len = len(sequence)
    seq_upper = sequence.upper()
    seq_total = 0
    code_nonredundant = set(code)
    #for each amiino acid in the code list
    for aa in code_nonredundant:
        print("Working on: ", aa)
        code_upper = aa.upper()
        #count the number of instances that amino acid appears in the sequence
        seq_count = seq_upper.count(code_upper)
        seq_perc = (seq_count/seq_len)*100
        if seq_perc == 0:
            print("no", aa, "found")
        #count the total for the list
        seq_total = seq_total+seq_perc
    return seq_total

#assertions to ensure the function is working as expected
#assert round(aa_percentage("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)
#assert round(aa_percentage("MSRSLLLRFLLFLLLLPPLP", "r")) == round(10)
#assert round(aa_percentage("MSRSLLLRFLLFLLLLPPLP", "L")) == round(50)
#assert round(aa_percentage("MSRSLLLRFLLFLLLLPPLP", "Y")) == round(0)
#assert round(aa_percentage("MSRSLLLRFLLFLLLLPPLP", ["M"])) == 5
#assert round(aa_percentage("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])) == 70
#assert round(aa_percentage("MSRSLLLRFLLFLLLLPPLP")) == 65


#call the function and send the output to a file
with open('output.txt','w') as result:
    result.write("The sequence contains " + str(round(aa_percentage("MSRSLLLRFLLFLLLLPPLP","lablab1234"))) + "% of the amino acid(s)")
