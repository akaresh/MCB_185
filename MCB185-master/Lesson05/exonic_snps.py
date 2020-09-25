#!/usr/bin/env python3

# Write a program that intersects SNPs and coding exons
# snps.txt.gz has all the 23andme snps on chrom 21
# exons.txt.gz has all the coding exons on chrom 21
# Report:
#	number of SNPs
#	number of genes
#	number of exons
#	names of genes with SNPs in them
# Given that there are about 100x more genes in the human genome
#	And 100x more SNPs on the full chip
#	Estimate how long your program would take to run using all available data



import gzip
import sys

#snps.txt.gz
#exons.txt.gz
#match both of them
snps = []
with gzip.open('snps.txt.gz', 'rt') as fp:
    #print(fp.read())
    for line in fp.readlines():
        l = line.split('\t')
        snps.append(l[2])

#print(len(snps[0]), snps[0])

for position_of_snp in snps:
    print(position_of_snp, len(position_of_snp))
#for i in snps:
    #print (i)

exons = {} ### change the way you store
all_genes = []
with gzip.open('exons.txt.gz', 'rt') as ep:
    #print(ep.read())
    for line in ep.readlines():
        l = line.split('\t')
        #exons.append(l)
        exons[l[0]] = [l[2],l[3].replace('\n', '')]
        if l[0] in all_genes:
            pass
        else:
            all_genes.append(l[0])

print(len(exons))
print(exons)


genes_w_snps = 0
gene_list_name = []

for position_of_snp in snps:

    for gene, exon_locations in exons.items():

        print(int(position_of_snp), len(position_of_snp))
        print(exon_locations[0], len(exon_locations[0]))
        print(int(exon_locations[1]), len(exon_locations[1]))
        if int(exon_locations[0]) <= int(position_of_snp):
            print('-----')
        if int(position_of_snp) <= int(exon_locations[1]):
            #gene_list_name.appen('////')
            print('////')
        if int(exon_locations[0]) <= int(position_of_snp) and int(position_of_snp) <= int(exon_locations[1]):

            #print(gene)
            gene_list_name.append(gene)
        #print(gene, exon_locations[0], exon_locations[1])
print(gene_list_name)

"""
print('SNPs:', len(snps))
print('Genes:', len(all_genes))
print('Exons:', len(exons))
print('Genes w/ SNPs:', gens_w_snps)
print('Gene List:', gene_list_name)

SNPs: 8607
Genes: 234
Exons: 2433
Genes w/ SNPs: 54
Gene List: ABCG1, AGPAT3, AIRE, AP000311.1, BACE2, BACH1, BRWD1, C21orf58, C2CD2, CBS, CHAF1B, CLDN17, COL6A1, COL6A2, DNMT3L, DOP1B, DSCAM, FAM243A, GART, IFNAR1, IFNGR2, ITGB2, KRTAP10-5, KRTAP10-7, KRTAP19-3, KRTAP25-1, MCM3AP, MORC3, PAXBP1, PCNT, PDE9A, PDXK, PIGP, PRDM15, PTTG1IP, PWP2, RRP1, RWDD2B, SCAF4, SIK1, SIM2, SLC37A1, SLC5A3, SOD1, SON, SYNJ1, TMPRSS15, TMPRSS2, TMPRSS3, TRAPPC10, TTC3, U2AF1, UMODL1, USP25
Estimated Full Time: 4.76 hours
"""
