# INI: Introduction to the Bioinformatics Armory

## Problem Description
The task requires counting the occurrences of DNA nucleotides (`A`, `C`, `G`, `T`) in a given genetic sequence. 

## Tool & Approach
Instead of writing a custom loop, this solution utilizes **Biopython** (`Bio.Seq`), which is the industry standard for handling molecular biology data in Python. 

- **Time Complexity:** $O(N)$ where $N$ is the length of the sequence.
- **Space Complexity:** $O(N)$ to load the sequence token into the `Seq` object.

## How to Run
Make sure you have Biopython installed:
```bash
pip install biopython
```

Run the script by piping your Rosalind dataset into it:
```bash
cat rosalind_ini.txt | python IBI.py
```
