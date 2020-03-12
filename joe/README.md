# running test assemblies with Nextstrain
## 1. make 5 test fastas from one assembly

```
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/009/937/885/GCA_009937885.1_ASM993788v1/GCA_009937885.1_ASM993788v1_genomic.fna.gz

sed 's/^>.*$/>new_name/' GCA_009937885.1_ASM993788v1_genomic.fasta > fasta.test1

```
## 2. make random deletions in test fastas with nano to simulate variation

```
cat fasta.test1 fasta.test2 fasta.test3 fasta.test4 fasta.test5 > /home/joemcgirr/ncov-master/ncov-master/data/sequences.fasta
```

## 3. put `metadata.tsv` and `sequences.fasta` in /data
## 4. run `snakemake -p`
## 5. visualize results
```
sudo docker run --privileged -v /var/run/docker.sock:/var/run/docker.sock -p 4000:4000 -v $PWD:/workdir -w /workdir -it nextstrain/base bash
nextstrain view auspice/
```

