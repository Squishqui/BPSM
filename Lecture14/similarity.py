#!/usr/bin/python3

#call the list and split the 4 sequences into separate variables
original_list = ['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']
list_range = list(range(0,len(original_list)))

#for each sequence in the range
for xaxis in list_range:
    first_query = list(original_list[xaxis])
    #print(first_query)
    
    #for each base in current sequence
    for yaxis in list_range:
        
        #do not compare the sequence to itself
        if xaxis == yaxis:
            continue
        identities = 0
        next_query = list(original_list[yaxis])
        
        #count differences between bases
        for base in list(range(0,len(first_query))):
            if first_query[base] == next_query[base]:
                identities += 1
                #print("Index " + str(base) + ":" + str(first_query[base]) + "," + str(next_query[base]) + "...")


# Calculate and print similarity percentage
        similarity = int(100 * (identities / len(first_query)))
        print(f"{identities} identities between {original_list[xaxis]} and {original_list[yaxis]}")
        print(f"\t{similarity} percent similarity between {original_list[xaxis]} and {original_list[yaxis]}")


#for seq in original_list:
#    print("The original string is " + str(seq))
#    res = []
#    res[:] = seq
    #print("The bases are " + str(res))
#    for i in res
