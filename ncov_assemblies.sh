#!/bin/bash

esearch -db nuccore -query 'sars-cov-2[orgn] AND 20000:33000[slen]' | efetch -db nuccore -format fasta > wuhan.fasta