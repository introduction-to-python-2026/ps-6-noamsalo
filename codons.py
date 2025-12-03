def create_codon_dict(file_path):
    codon_dict = {}

    file = open(file_path, "r")
    rows = file.readlines()
    file.close()

    
    for line in rows:
        parts = line.strip().split('\t')
        codon = parts[0]                     
        amino_acid_abbreviation = parts[2]   
        codon_dict[codon] = amino_acid_abbreviation

    return codon_dict
