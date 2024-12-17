#!/usr/bin/python3
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

def calculate_content(sequence, window_size, content_type="AT", region_length=None):
    """
    Calculate the fraction of AT or GC content in sliding windows over the genome sequence.

    Parameters:
        sequence (str): DNA sequence as a single string.
        window_size (int): Size of the sliding window.
        content_type (str): Type of content to calculate ('AT' or 'GC'). Default is 'AT'.
        region_length (int): Portion of genome to analyze. Default is the entire sequence.
    
    Returns:
        list: List of content fractions for each window.
    """
    if region_length is None or region_length > len(sequence):
        region_length = len(sequence)
        
    content_fractions = []  # List to hold calculated content fractions
    for start in range(region_length - window_size):
        window = sequence[start:start + window_size]
        if content_type == "AT":
            fraction = (window.count('A') + window.count('T')) / window_size
        elif content_type == "GC":
            fraction = (window.count('G') + window.count('C')) / window_size
        else:
            raise ValueError("Invalid content_type. Choose 'AT' or 'GC'.")
        content_fractions.append(fraction)
    return content_fractions

def plot_content(content_fractions, content_type, window_size, region_length, output_file):
    """
    Plot and save the AT or GC content.

    Parameters:
        content_fractions (list): List of content fractions.
        content_type (str): Type of content ('AT' or 'GC').
        window_size (int): Window size used for the analysis.
        region_length (int): Portion of genome analyzed.
        output_file (str): Name of the file to save the plot.
    """
    plt.figure(figsize=(20, 10))
    plt.plot(content_fractions, label=f"{content_type} content", linewidth=3, color="purple")
    plt.ylabel('Fraction of bases')
    plt.xlabel('Position on genome')
    plt.title(f"{content_type} content, {window_size}bp windows of the E.coli genome (0 to {region_length} bases)")
    plt.legend()
    plt.savefig(output_file, transparent=True)
    plt.show()

def main():
    # Default parameters
    ecoli_file = "ecoli.txt"
    window_size = 1000
    content_type = "AT"
    region_length = 100000

    # Load and process the genome sequence
    if not os.path.exists(ecoli_file):
        print(f"Error: {ecoli_file} does not exist.")
        sys.exit(1)

    ecoli_sequence = open(ecoli_file).read().replace('\n', '').upper()
    
    # Ask for user inputs interactively
    try:
        window_size = int(input("Enter the window size (default 1000): ") or 1000)
        content_type = input("Enter content type ('AT' or 'GC', default 'AT'): ").upper() or "AT"
        region_length = int(input("Enter the portion of genome to analyze (default 100000): ") or 100000)

        if content_type not in ["AT", "GC"]:
            raise ValueError("Content type must be 'AT' or 'GC'.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        sys.exit(1)

    print(f"Processing {content_type} content with window size {window_size} for first {region_length} bases...")

    # Calculate content
    content_fractions = calculate_content(ecoli_sequence, window_size, content_type, region_length)

    # Generate and save the plot
    output_file = f"Chart_{content_type}_content_{region_length}bp.png"
    plot_content(content_fractions, content_type, window_size, region_length, output_file)
    print(f"Plot saved as {output_file}")

main()

