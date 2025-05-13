# s11111_2025.py
# Purpose of the program:
# This Python script generates a random DNA sequence in FASTA format with user-defined parameters.
# It includes user-provided metadata, computes nucleotide statistics, inserts a name into the sequence,
# and saves everything into a properly named FASTA file.

import random

# List of valid DNA nucleotides
NUCLEOTIDES = ['A', 'C', 'G', 'T']

# ORIGINAL:
# sequence = ''.join(random.choices("ACGT", k=length))
# MODIFIED (for readability and clarity):
def generate_dna_sequence(length):
    """Generate a random DNA sequence of a given length."""
    return ''.join(random.choices(NUCLEOTIDES, k=length))

def insert_name(sequence, name):
    """Insert the name at a random position in the sequence."""
    position = random.randint(0, len(sequence))
    return sequence[:position] + name + sequence[position:]

def calculate_statistics(sequence, name):
    """
    Calculate nucleotide percentages and CG/AT ratio,
    ignoring characters from the inserted name.
    """
    filtered_seq = ''.join([base for base in sequence if base in NUCLEOTIDES])
    length = len(filtered_seq)
    stats = {n: round((filtered_seq.count(n) / length) * 100, 1) for n in NUCLEOTIDES}
    cg_ratio = round(((filtered_seq.count('C') + filtered_seq.count('G')) / length) * 100, 1)
    return stats, cg_ratio

def save_fasta_file(filename, header, sequence):
    """Save the sequence and header to a FASTA file."""
    with open(filename, 'w') as f:
        f.write(f">{header}\n")
        f.write(sequence + "\n")

# --- User Interaction ---

# Get user input
length = int(input("Enter the sequence length: "))
sequence_id = input("Enter the sequence ID: ")
description = input("Provide a description of the sequence: ")
user_name = input("Enter your name: ")

# Generate DNA sequence
original_sequence = generate_dna_sequence(length)
final_sequence = insert_name(original_sequence, user_name)

# Compute statistics
stats, cg_ratio = calculate_statistics(final_sequence, user_name)

# Create filename and header
filename = f"{sequence_id}.fasta"
header = f"{sequence_id} {description}"

# Save to file
save_fasta_file(filename, header, final_sequence)

# Print confirmation and statistics
print(f"\nThe sequence was saved to the file {filename}")
print("\nSequence statistics:")
for base in NUCLEOTIDES:
    print(f"{base}: {stats[base]}%")
print(f"%CG: {cg_ratio}")

# --- ADDITIONAL FEATURES ---

# Feature 1: Validate user input
# MODIFIED (justification: adds robustness against incorrect input):
# Original input(...) lines remain, but we add error checking logic
# Commented below to show the change

# ORIGINAL:
# length = int(input("Enter the sequence length: "))
# MODIFIED:
# Ensures that the user enters a positive integer
while True:
    try:
        length = int(input("Enter the sequence length: "))
        if length <= 0:
            print("Length must be a positive integer.")
            continue
        break
    except ValueError:
        print("Please enter a valid integer for the sequence length.")

# Feature 2: Automatically format sequence output in lines of 60 characters (common FASTA style)
# MODIFIED:
def format_sequence(sequence, line_length=60):
    """Split the sequence into lines of fixed length for FASTA formatting."""
    return '\n'.join([sequence[i:i+line_length] for i in range(0, len(sequence), line_length)])

# Replace in save_fasta_file:
# ORIGINAL:
# f.write(sequence + "\n")
# MODIFIED:
# Save the sequence in multiple lines for better readability
# f.write(format_sequence(sequence) + "\n")

# Feature 3: Save statistics to a separate file
# MODIFIED:
def save_statistics(filename, stats, cg_ratio):
    """Save the sequence statistics to a separate file."""
    with open(filename, 'w') as f:
        for base in NUCLEOTIDES:
            f.write(f"{base}: {stats[base]}%\n")
        f.write(f"%CG: {cg_ratio}\n")

# Call to save statistics
stats_filename = f"{sequence_id}_stats.txt"
save_statistics(stats_filename, stats, cg_ratio)

print(f"Statistics were also saved to {stats_filename}")

# --- End of program ---
