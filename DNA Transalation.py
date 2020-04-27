def read_seq(inputFile):
    with open (inputFile, "r") as f:
        seq = f.read()
    seq = seq.replace("\n","")
    seq = seq.replace("\r","")
    return seq

inputFile = "DNA.txt"
f = open(inputFile, "r") # here "r" is short form for reading that means that we are opening file for reading only
seq = f.read()
seq = seq.replace("\n","") # we had copy pasted the text so there is a special symbol occur when we try to read the file so we had replaced that special symbol with nothing.
seq = seq.replace("\r","") # sometimes there is also another charachter in the file which may not be visible, so to be on safe side we also remove that character as well
print(seq)

def translate(seq):
    table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',}

    protein = ""
    # Check the sequence length is divisible by 3
    if len(seq)%3 == 0:
        # Look over the sequence
        for i in range(0,len(seq),3):
            # Extract a single codon
            codon = seq[i:i+3]
            # lookup the codon and store the result
            protein += table[codon]
    return protein
