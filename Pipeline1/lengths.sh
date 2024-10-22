#!/usr/bin/bash

# Define the FASTA file location
fasta_file="/localdisk/home/s2760053/Exercises/Pipeline1/Tcongo/TriTrypDB-46_TcongolenseIL3000_2019_Genome.fasta.gz"

# Initialize a variable to hold the total character count
total_count=0

# Read the FASTA file line by line
while IFS= read -r line; do
    # Check if the line starts with '>'
    if [[ $line == ">"* ]]; then
        # If it's a header, print the current count and reset it
        if [[ $total_count -gt 0 ]]; then
            echo "Characters in the previous sequence: $total_count"
            total_count=0  # Reset the count for the next sequence
        fi
    else
        # Count the number of characters in the current line (sequence)
        # We use ${#line} to get the length of the line
        total_count=$((total_count + ${#line}))
    fi
done < "$fasta_file"

# If there was no header at the end of the file, print the last count
if [[ $total_count -gt 0 ]]; then
    echo "Characters in the last sequence: $total_count"
fi

