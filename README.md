**DNA Sequence Analyzer (Beginner Bioinformatics Project)**

This project is a simple DNA Sequence Analyzer written in Python.
It takes a DNA sequence as input and calculates:
   Total sequence length
   Count of each nucleotide (A, T, G, C)
   GC Content (%)
This is a beginner-friendly bioinformatics tool useful for learning sequence analysis, genomics basics, and Python programming.

📌 **Features**

✔ Reads DNA sequence from a FASTA/text file or direct input
✔ Counts nucleotides: A, T, G, C
✔ Calculates sequence length
✔ Computes GC content
✔ Gives clean, easy-to-understand output

 **Example Output**
--- DNA Analysis ---
Sequence length: 85966
A: 26419
T: 25421
G: 16883
C: 17243
GC Content: 39.70%

 **How to Run the Code**

Install Python (3.x)

Save your DNA sequence in a file (e.g., sequence.txt)
OR paste your sequence directly when asked

Run the script:

python dna_analyzer.py


Input your sequence when prompted or load the file.

📁 **Project Structure**
📦 DNA-Sequence-Analyzer
 ┣ 📄 dna_analyzer.py
 ┣ 📄 README.md
 ┗ 📄 sample_sequence.txt 

🧬 **Code Used in This Project**
def analyze_dna(sequence):
    sequence = sequence.upper()
    length = len(sequence)
    a = sequence.count('A')
    t = sequence.count('T')
    g = sequence.count('G')
    c = sequence.count('C')
    
    gc_content = ((g + c) / length) * 100
    
    print("--- DNA Analysis ---")
    print(f"Sequence length: {length}")
    print(f"A: {a}")
    print(f"T: {t}")
    print(f"G: {g}")
    print(f"C: {c}")
    print(f"GC Content: {gc_content:.2f}%")

# Input from user
dna_input = input("Enter DNA sequence: ")
analyze_dna(dna_input)

🎯 **Why This Project Is Useful**

Great starter project for bioinformatics students

Helps understand nucleotide composition & GC content

Enhances Python skills with string processing

Forms the base for advanced tools:

ORF finder

Mutation scanner

FASTA parser

Genome feature extractor

_**Author**_

Namrata Vishwakarma
Bioengineering | VIT Bhopal
Interested in Bioinformatics, Genomics & AI in Biology
