# PeakMatcher
Many early draft genome assemblies are incomplete or fragmented (not assembled to chromosome scale).  Researchers often resequence genomes and generate new updated assemblies.  For example, my search for ["improved genome assembly"](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C50&q=improved+genome+assembly&btnG=&oq=improved+genome+) on Google Scholar returns several pages of papers documenting new genome assemblies of everything from insects, fish, plants, reptiles, and birds.

Processing of data from DNA enrichment assays such as ChIP-Seq and ATAC-Seq is intimitedly tied to the genome assembly.  Sequencing data are aligned to the genome; overlapping reads form "peaks" that indicate areas of activity within the genome.  When assemblies are updated, these data need to be reprocessed and re-analyzed.  It is not, however, feasible or even reasonable to completely redo all validation work such as wet-lab experiments.

PeakMatcher is a tool for matching up peaks called for the same DNA enrichment assay data across two genome assemblies.  PeakMatcher takes peak lists and read alignments for both genome assemblies as input and outputs a text file containing peak-peak pairs.

PeakMatcher exploits the association of peaks with their underlying sequencing data.  A given peak is formed by a set of overlapping reads.  It is highly likely that these same reads would align together on both genomes.  PeakMatcher finds the reads overlapping each peak in both genomes and uses the common reads to perform an inner-join of the peaks.

## Dependencies
PeakMatcher is developed with Python 3 and depends on the [intervaltree](https://github.com/chaimleib/intervaltree) library.

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

## Usage: Comparing Peaks Across Genomes

When calling peaks for an updated genome, we need a way to validate the peaks between the two genome versions.  PeakMatcher includes a pair of scripts that uses the peak reads aligned to both genomes to match up peaks and calculate precision and recall.

1. Use `match_peaks_to_reads` to find reads that overlap the peaks in the L3 alignment
2. Use `match_reads_to_peaks` to check if reads are aligned to L5 and if they overlap with peaks called for L5


```
$ samtools view genome1.filtered.bam | match_peaks_to_reads --peaks-fl genome1_peaks.narrowPeak --reads-fl genome1_peaks.reads
$ samtools view genome2.filtered.bam | match_reads_to_peaks --peak-reads-fl genome1_peaks.reads --peaks-fl genome2_peaks.narrowPeak --matched-peaks-fl matched_peaks.tsv --unmatched-peaks-fl unmatched_peaks.tsv
```

The output is stored in two files.  The list of matched peaks are stored in `matched_peaks.tsv`, while the list of peaks from genome 2 that were not able to be matched are stored in `unmatched_peaks.tsv`.

## Citing This Software
If you use PeakMatcher, please cite our paper:

Nowling, R.J., Behura, S.K., Halfon, M.S. et al. [PeakMatcher facilitates updated _Aedes aegypti_ embryonic _cis_-regulatory element map](https://hereditasjournal.biomedcentral.com/articles/10.1186/s41065-021-00172-2). _Hereditas_ 158, 7 (2021). https://doi.org/10.1186/s41065-021-00172-2
