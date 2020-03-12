# Nextstrain analyses with hCoV-19 sequences in the SRA.

## The Omen workflow: combining augur, auspice, and SRA
## What is this workflow?
Labs around the world are sequencing coronavirus (hCoV-19) to monitor how it spreads and evolves. However, most sequences are not immediately publicly availible. Here we provide a workflow to identfy publicly available hCoV-19 sequences that have been uploaded to the NCBI SRA database. We map SRA reads to the hCoV-19 Whuan reference genome, identify variable sites, create a consensus fasta sequence, and analyse these sequences with [Nextstrain](https://github.com/nextstrain/ncov).

## Workflow to analyze publicly available hCoV-19 SRA reads with Nextstrain
1. Identify hCoV-19 sequences using the NCBI SRA Taxonomy Analysis Tool (STAT) 
2. Extract metadata to match Nexstrain input
3. Download SRA data and generate consensus sequences for each run
4. Run Nextstrain for analyses and visualization


![alt text](https://github.com/NCBI-Codeathons/Automating-tools-to-search-and-analyze-large-genome-sequence-repositories/blob/master/workflow.png "Logo Title Text 1")


### 1. Identify hCoV-19 sequences using the NCBI SRA Taxonomy Analysis Tool (STAT)
Vadim Identify hCoV-19 SRA reads with STAT
### 2. Extract metadata to match Nexstrain input
Alison metadata wrangling
### 3. Download SRA data and generate consensus sequences for each run
Alison snakemake. 
a. download SRA reads
b. map to Wuhan reference genome
c. identify variable sites
d. generate consensus sequence
### 4. Run Nextstrain for analyses and visualization
snakemake in the cloud

# Team
Our fearless leader: Vadim Zalunin (vadimzalunin)

Alison Schaefer (amaiellu)

Joe McGirr (joemcgirr)

# Forthcoming features

# Architecture

# Dependencies
