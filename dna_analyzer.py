# Simple DNA Analyzer

# Read the DNA sequence from user
sequence = input("Enter DNA sequence: ").upper()

# Remove spaces or new lines
sequence = sequence.replace(" ", "").replace("\n", "")

# Count bases
A = sequence.count("A")
T = sequence.count("T")
G = sequence.count("G")
C = sequence.count("C")

# Total length
length = len(sequence)

# GC content
if length > 0:
    gc_content = ((G + C) / length) * 100
else:
    gc_content = 0

# Print results
print("\n--- DNA Analysis ---")
print("Sequence length:", length)
print("A:", A)
print("T:", T)
print("G:", G)
print("C:", C)
print(f"GC Content: {gc_content:.2f}%")
