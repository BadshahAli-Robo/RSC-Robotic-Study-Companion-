from collections import Counter

def consensus_string(motifs):
    consensus = ""
    k = len(motifs[0])  # length of each string
    for i in range(k):
        # Collect the i-th character from each string
        column = [motif[i] for motif in motifs]
        # Count frequency and get most common
        most_common = Counter(column).most_common(1)[0][0]
        consensus += most_common
    return consensus

# Test
motifs = ['GCTCT', 'TCCGT', 'ACCTA', 'ACGGT']
print("Consensus:", consensus_string(motifs))  # Output: ACCGT
