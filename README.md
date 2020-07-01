# PeakMatcher
A tool for matching peaks across genome assemblies using read alignments.

## Dependencies
PeakMatcher is developed with Python 3.

## Installation

```bash
$ pip install -m .
```

## Development

It is easiest to use PeakMatcher in a Python [virtual environment](https://docs.python.org/3/library/venv.html).  You can create a virtual environment like so:

```bash
$ python -m venv environment_directory
```

To activate the virtual environment:

```bash
$ source environment_directory/bin/activate
```

With [developer mode](https://setuptools.readthedocs.io/en/latest/setuptools.html#development-mode), you can then make the peakmatcher package available in your environment directly from the local git repository so that any changes are reflected in real time:

```bash
$ python setup.py develop
```

To deactivate the virtual environment, run:

```bash
$ deactivate
```

## Usage

1. Use `match_peaks_to_reads` to find reads that overlap the peaks in the L3 alignment
2. Use `match_reads_to_peaks` to check if reads are aligned to L5 and if they overlap with peaks called for L5


```
$ match_peaks_to_reads --peaks-fl ../Aedes_exp2_peaks.txt --bam-fl ../peak-calling-L3-aln-mapq10/05_alignments/SRR2530418.filtered.bam --reads-fl Aedes_exp2_peaks.reads
$ samtools view ../peak-calling-L5-aln-mapq10/data/filtered_reads/SRR2530418.filtered.bam | match_reads_to_peaks --peak-reads-fl Aedes_exp2_peaks.reads --peaks-fl ../peak-calling-L5-aln-mapq10/06_called_peaks_molly_L3genome_size/AaegL3_faire_seq_peaks.narrowPeak
```

