## Value & Methodology (Why This Approach Matters)

In modern bioinformatics, relying on manual web interface searches (like using the NCBI website via a browser) is inefficient, prone to human error, and completely non-scalable. This solution automates data retrieval directly from the **NCBI GenBank** database using **Biopython’s `Bio.Entrez`** module, establishing a robust programmatic pipeline.

### Engineering & Biological Value:

* **Automated Data Discovery:** Programmatically monitors, filters, and counts submissions for specific taxa over defined historical windows without manual indexing.
* **Network & Memory Efficiency:** Utilizes the `esearch` utility to fetch only the lightweight XML metadata (specifically the `<Count>` tag) rather than downloading heavy, gigabyte-sized genome files. This keeps the local runtime memory footprint strictly at $O(1)$.
* **API Compliance:** Adheres to NCBI’s professional data-access protocols by explicitly declaring user identity (`Entrez.email`), preventing automatic IP blocking or rate-limiting during large-scale operations.
* **Pipeline Integration:** Standardizes input/output flow using `sys.stdin` and `sys.stdout`, allowing this script to be easily integrated into larger automated workflow engines (e.g., Nextflow, Snakemake, or Bash loops).

## How to Run (Usage Guide)

### 1. Prerequisites
Ensure you have Python 3 and the **Biopython** library installed on your machine. If not, install it using your terminal:
```bash
pip install biopython
```

### 2. Prepare the Dataset
Create a text file named `rosalind_gbk.txt` in the same directory as the script. The file must contain exactly three lines formatted as follows:
```text
Genus_Name
YYYY/MM/DD (Start Date)
YYYY/MM/DD (End Date)
```

*Example (`rosalind_gbk.txt`):*
```text
Anthoxanthum
2003/07/25
2005/05/04
```

### 3. Configure Your Credentials
Before executing the script, open `script.py` and replace the placeholder email with your actual email address:
```python
Entrez.email = "your_email@example.com"
```
*Note: This is a strict requirement by NCBI to avoid automated rate-limiting.*

### 4. Execute the Script
Run the script using the system console by piping the input dataset into the program:

**On Windows (Command Prompt / `cmd`):**
```bash
python script.py < rosalind_gbk.txt
```
*Alternatively, using the Windows `type` command:*
```bash
type rosalind_gbk.txt | python script.py
```

**On Linux / macOS:**
```bash
cat rosalind_gbk.txt | python script.py
```

### 5. Output
The script will output a single integer representing the total number of matching nucleotide entries found in GenBank:
```text
4
```text
