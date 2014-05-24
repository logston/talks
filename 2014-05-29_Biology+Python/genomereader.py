import os
SNP_FILE = '/Users/paul/Code/dna_compile/mysnps.txt'
GENOME_DIR = '/Users/paul/Code/dna_compile/GRCh37.p12_Primary_Assembly'
FA_FILE_LINE_LENGTH = 70

def snps(snp_file):
    with open(snp_file) as fd:
        for line in fd:
            if line[0] == '#':
                continue
            line = line.split(b'\t')
            yield (line[1], line[2], line[3].strip())


def genome_lines(genome_dir, snp_file):
    genome_files = {}
    for f in os.listdir(genome_dir):
        if 'chr' in f:
            genome_files[f[3:].strip('.fa')] = os.path.join(genome_dir, f)

    snp_generator = snps(snp_file)
    next_snp = snp_generator.next()
    for f, path in genome_files.items():
        with open(path) as fd:
            pos = 0
            for line in fd:
                if line[0] == '>':
                    continue
                if next_snp:
                    while next_snp[0] == f and pos < next_snp[1] < pos + FA_FILE_LINE_LENGTH: 
                        snp_pos = int(next_snp[1])
                        line_pos = (snp_pos - 1) % FA_FILE_LINE_LENGTH
                        line = line[:line_pos] + next_snp[2][0] + line[line_pos + 1:]
                        next_snp = snp_generator.next()
                pos += FA_FILE_LINE_LENGTH
                yield line.strip()

genome_line_generator = genome_lines(GENOME_DIR, SNP_FILE)
