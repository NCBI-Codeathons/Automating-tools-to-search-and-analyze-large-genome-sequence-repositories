# Nextstrain analyses with hCoV-19 sequences in the SRA.

## What is this workflow?
Labs around the world are sequencing coronavirus (hCoV-19) to monitor how it spreads and evolves. However, most sequences are not immediately publicly availible. Here we provide a workflow to identfy publicly available hCoV-19 sequences that have been uploaded to the NCBI SRA database. We map SRA reads to the hCoV-19 Whuan reference genome, identify variable sites, create a consensus fasta sequence, and analyse these sequences with [Nextstrain](https://github.com/nextstrain/ncov).

## Workflow to analyze publicly available hCoV-19 SRA reads with Nextstrain
1. Identify hCoV-19 sequences
- using the NCBI SRA Taxonomy Analysis Tool (STAT)
- using whole genome assemblies [here](https://www.ncbi.nlm.nih.gov/core/assets/genbank/files/ncov-sequences.yaml)
2. Extract metadata to match Nexstrain input
3. Download SRA data
4. Run Nextstrain for analyses and visualization


![alt text](https://github.com/NCBI-Codeathons/Automating-tools-to-search-and-analyze-large-genome-sequence-repositories/blob/master/workflow-01.png "Logo Title Text 1")


### 1. Identify hCoV-19 sequences 
The NCBI SRA Taxonomy Analysis Tool (STAT) can identify SRA runs with kmers matching hCoV-19. We identified runs containing >1000 matching kmers. Alternatively, there are full genome assemblies available for hCoV-19 that can be used. Assemblies can be run without generating alignments and consensus sequences (see below). 

### 2. Extract metadata to match Nexstrain input
We created a snakemake that will create `metadata.tsv` containing metadata for SRA runs identified with STAT.
### 3. Download SRA data and generate consensus sequences for each run
The snakemake will also generate `sequences.fasta` by 
- downloading SRA reads
- mapping them to the [Wuhan reference genome](https://www.ncbi.nlm.nih.gov/nuccore/MN908947.3/) (hisat2)
- identifying variable sites
- generate consensus sequences (bcftools)
### 4. Run Nextstrain for analyses and visualization
Finally, we add `metadata.tsv` `sequences.fasta` and run snakemake -p to produce Nextstrain results that can be viewed with
```
auspice view --datasetDir auspice
```

# Team
- Our fearless leader: Vadim Zalunin (vadimzalunin)
- Alison Schaefer (amaiellu)
- Joe McGirr (joemcgirr)

# Forthcoming features
We are automating the process of wrangling metadata for full genome assemblies. 

# Dependencies
See Dockerfile
