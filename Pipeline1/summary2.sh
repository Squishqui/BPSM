#!/usr/bin/bash

# Step 2: Assess quality of raw sequence data using FastQC

# Ask for the directory with FastQ data
echo "Enter the directory containing the FASTQ files:"
read directory

# Specify output directory for FastQC results
output_dir="${directory}/fastqc_results"
mkdir -p "$output_dir"

# Summarize the results
echo "Summarizing QC results..."
echo "QC Summary" > "${directory}/qcsummary.txt"
for folder in "${directory}"/*_fastqc; do
    pass_count=$(awk 'BEGIN{FS="\t"; pass=0} $1 == "PASS" {pass++} END {print pass}' "${folder}/summary.txt")
    warn_count=$(awk 'BEGIN{FS="\t"; warn=0} $1 == "WARN" {warn++} END {print warn}' "${folder}/summary.txt")
    fail_count=$(awk 'BEGIN{FS="\t"; fail=0} $1 == "FAIL" {fail++} END {print fail}' "${folder}/summary.txt")

    # Write results to qcsummary.txt
    echo "$(basename "$folder"): PASS=${pass_count}, WARN=${warn_count}, FAIL=${fail_count}" >> "${directory}/qcsummary.txt"
    
    if [[ $fail_count -gt 0 ]]; then
        echo "$(basename "$folder") contains FAIL results." >> "${directory}/qcsummary.txt"
    else
        echo "$(basename "$folder") passed the QC test." >> "${directory}/qcsummary.txt"
    fi
done

echo "QC results summarized in ${directory}/qcsummary.txt."
