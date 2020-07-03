# PeakMatcher
A tool for matching peaks across genome assemblies using read alignments.

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

## Usage

1. Use `match_peaks_to_reads` to find reads that overlap the peaks in the L3 alignment
2. Use `match_reads_to_peaks` to check if reads are aligned to L5 and if they overlap with peaks called for L5


```
$ samtools view genome1.filtered.bam | match_peaks_to_reads --peaks-fl genome1_peaks.narrowPeak --reads-fl genome1_peaks.reads
$ samtools view genome2.filtered.bam | match_reads_to_peaks --peak-reads-fl genome1_peaks.reads --peaks-fl genome2_peaks.narrowPeak
```

