#!/usr/bin/env python3
from Bio import Entrez, SeqIO
from Bio.Seq import Seq
import statistics

# Set your email for NCBI access
Entrez.email = "e.g.cragg@sms.ed.ac.uk"
Entrez_api_key = "5150280144c8068543fe3ccb82f021fa1c08"

def fetch_protein_records(gene_name, taxonomic_group, max_records=500):
    """
    Fetches protein records from NCBI for a given gene name and taxonomic group.
    
    Parameters:
        gene_name (str): The name of the gene (e.g., "COX1").
        taxonomic_group (str): The taxonomic group to search within (e.g., "Mammals").
        max_records (int): Maximum number of records to fetch. Default is 500.
        
    Returns:
        list: A list of SeqRecord objects containing the protein records.
    """
    # Search query in the NCBI Protein database
    search_query = f"{gene_name}[Gene] AND {taxonomic_group}[Organism]"
    
    print(f"Searching NCBI Protein database for '{gene_name}' in '{taxonomic_group}'...")
    handle = Entrez.esearch(db="protein", term=search_query, retmax=max_records)
    search_results = Entrez.read(handle)
    handle.close()
    
    protein_ids = search_results["IdList"]
    print(f"Found {len(protein_ids)} records. Fetching data...")

    if not protein_ids:
        print("No records found for the given query.")
        return []

    # Fetch records using the IDs
    handle = Entrez.efetch(db="protein", id=protein_ids, rettype="gb", retmode="text")
    protein_records = list(SeqIO.parse(handle, "genbank"))
    handle.close()
    
    return protein_records

def analyze_protein_lengths(protein_records):
    """
    Analyzes the lengths of protein records.
    
    Parameters:
        protein_records (list): List of SeqRecord objects.
        
    Returns:
        tuple: A tuple containing the count of records and their average length.
    """
    lengths = [len(record.seq) for record in protein_records]
    count = len(lengths)
    average_length = statistics.mean(lengths) if lengths else 0
    
    return count, average_length

def retrieve_and_analyze_gene(gene_name, taxonomic_group, max_records=500):
    """
    Retrieves protein records for a specified gene and taxonomic group, 
    and calculates the number of records and their average length.
    
    Parameters:
        gene_name (str): The name of the gene (e.g., "COX1").
        taxonomic_group (str): The taxonomic group (e.g., "Mammals").
        max_records (int): Maximum number of records to fetch. Default is 500.
    
    Returns:
        dict: A dictionary containing useful statistics and information.
    """
    # Fetch protein records
    protein_records = fetch_protein_records(gene_name, taxonomic_group, max_records)

    if not protein_records:
        return {"Message": "No records found.", "Count": 0, "Average Length": 0}

    # Analyze protein lengths
    count, avg_length = analyze_protein_lengths(protein_records)

    # Extract additional useful information
    species = set(record.annotations.get("organism", "Unknown") for record in protein_records)
    accession_ids = [record.id for record in protein_records]

    # Summary dictionary
    summary = {
        "Gene": gene_name,
        "Taxonomic Group": taxonomic_group,
        "Record Count": count,
        "Average Length": avg_length,
        "Unique Species Count": len(species),
        "Example Species": list(species)[:5],  # First 5 species
        "Accession IDs (first 5)": accession_ids[:5]  # First 5 accession IDs
    }
    
    return summary

# Example usage for COX1 in mammals
gene_name = "COX1"
taxonomic_group = "Mammals"



# Run the retrieval and analysis function
results = retrieve_and_analyze_gene(gene_name, taxonomic_group)
    
# Display the results
print("\n--- Protein Record Analysis Results ---")
for key, value in results.items():
    print(f"{key}: {value}")

