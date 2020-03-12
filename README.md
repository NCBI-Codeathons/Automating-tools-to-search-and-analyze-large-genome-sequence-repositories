# What does this do?
Labs around the world are sequencing hCoV-19 to monitor how it spreads and evolves. However, most sequences are not immediately publicly availible.  

## Workflow to analyzing publicly available hCoV-19 SRA reads with Nextstrain
1. Identify metadata to match Nexstrain input
2. Download SRA data
3. Align reads to Wuhan reference genome
4. Run Nextstrain for analyses and visualization
## 1. Metadata
Identify hCoV-19 SRA reads and wrangle metadta to create Nextstrain metadata.tsv
metadata.tsv contains: strain	virus	gisaid_epi_isl	genbank_accession	date	region	country	division	division_exposure	location	segment	length	host	age	sex	originating_lab	submitting_lab	authors	url	title
## 2. Download SRA data
download hCoV-19 SRA reads to vm
## 3. Align reads to Wuhan reference genome
with hisat2
## 4. Run Nextstrain for analyses and visualization
run snakemake

# Forthcoming features

# Team

# Architecture

# Dependencies
