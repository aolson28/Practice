def DNA_strand(dna):
    c = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
    dna2 = [c.get(i) for i in dna]
    return ''.join(dna2)

# P string
# R string containing opposites A/T and C/G replaced from original string
# E ATCG -> TAGC
# P use dict, create list with each character replaced using get, then join the list
# simpler -> return ''.join(c[i] for i in dna) <- OR -> return ''.join(c[i] for i in dna)dna.translate(str.maketrans("ATCG","TAGC"))