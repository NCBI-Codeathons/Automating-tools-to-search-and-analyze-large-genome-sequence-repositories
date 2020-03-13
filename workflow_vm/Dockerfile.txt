FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y git
RUN git clone https://github.com/nextstrain/ncov.git


RUN apt-get update -qqy --fix-missing

RUN apt-get install -qqy wget zip unzip python python-pip python3 python3-setuptools python3-docutils python3-flask python3-pip libxml2-utils python-pyasn1 python-pyasn1-modules time git gawk bzip2
RUN apt-get install -qqy libbz2-dev lsb-release curl rsync make gcc zlib1g-dev liblzma-dev libcurl4-openssl-dev mc autoconf cmake openjdk-11-jdk libffi-dev libxml2-dev apt-transport-https libssl-dev
RUN apt-get install -qqy r-base bedtools hmmer mcl muscle garli jupyter
RUN apt-get install -qqy virtualenv

RUN pip3 install numpy
RUN pip3 install cython
RUN pip3 install pysam
RUN pip3 install google_compute_engine snakemake psutil lxml HTSeq dedupe RSeQC biopython whatshap

RUN pip install numpy
RUN pip install cython
RUN pip install pysam

RUN wget -q https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.10.2/sratoolkit.2.10.2-ubuntu64.tar.gz
RUN tar xzf sratoolkit.2.10.2-ubuntu64.tar.gz
RUN rm sratoolkit.2.10.2-ubuntu64.tar.gz
RUN mv ./sratoolkit.2.10.2-ubuntu64 /opt
RUN echo -e "export PATH=/opt/sratoolkit.2.10.2-ubuntu64/bin:\$PATH" > /etc/profile.d/sratoolkit.sh
RUN chmod 755 /etc/profile.d/sratoolkit.sh

RUN mkdir /etc/ncbi

RUN wget -q https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.9.2/hisat2-2.1.0-64-ngs.2.9.2.zip
RUN unzip -qq hisat2-2.1.0-64-ngs.2.9.2.zip
RUN rm hisat2-2.1.0-64-ngs.2.9.2.zip
RUN mv ./hisat2 /opt
RUN echo -e "export PATH=/opt/hisat2:\$PATH\nexport HISAT2_HOME=/opt/hisat2" > /etc/profile.d/hisat2.sh
RUN chmod 755 /etc/profile.d/hisat2.sh


RUN wget -q https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2
RUN tar xjf samtools-1.9.tar.bz2
RUN rm samtools-1.9.tar.bz2
RUN cd samtools-1.9
RUN ./configure --without-curses >/dev/null
RUN make --quiet
RUN make --quiet install
RUN cd ..
RUN rm -rf ./samtools-1.9

RUN wget -q https://github.com/samtools/bcftools/releases/download/1.9/bcftools-1.9.tar.bz2
RUN tar xjf bcftools-1.9.tar.bz2
RUN rm bcftools-1.9.tar.bz2
RUN cd bcftools-1.9
RUN ./configure --without-curses >/dev/null
RUN make --quiet
RUN make --quiet install
RUN cd ..
RUN rm -rf ./bcftools-1.9

RUN wget -q https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
RUN chmod 755 Anaconda3-2019.10-Linux-x86_64.sh
RUN ./Anaconda3-2019.10-Linux-x86_64.sh -b -p /opt/anaconda3
RUN rm ./Anaconda3-2019.10-Linux-x86_64.sh
RUN echo -e "export PATH=\$PATH:/opt/anaconda3/bin\nexport JAVA_HOME=/opt/anaconda3" > /etc/profile.d/anaconda3.sh
RUN chmod 755 /etc/profile.d/anaconda3.sh



