"""
Copyright 2020 Ronald J. Nowling

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from setuptools import setup

setup(name="peakmatcher",
      version=0.1,
      description="Match DNA enrichment assays peaks across genome assemblies",
      author="Ronald J. Nowling",
      author_email="rnowling@gmail.com",
      license="Apache License, Version 2.0",
      zip_safe=False,
      install_requires = ["intervaltree"],
      scripts=["bin/match_peaks_to_reads", "bin/match_reads_to_peaks", "bin/compare_peaks_within_genome", "bin/peaks_in_region"])

