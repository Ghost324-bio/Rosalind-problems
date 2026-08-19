import sys
from Bio import Entrez


def count_genbank_records(stream_input):
    """Parses NCBI credentials, executes an E-search query,

    and returns the total count of discovered nucleotide entries.

    :param stream_input: Text stream (sys.stdin) containing query parameters.
    :return: String representing the total number of records.
    """
    # Clean the input stream and filter out empty lines
    lines = [line.strip() for line in stream_input if line.strip()]

    # Elegantly unpack the list into separate variables (Pythonic style)
    genus, start_date, end_date = lines

    # Provide email credentials required by NCBI API to prevent IP blocking
    Entrez.email = "your_mail@example.com"

    # Formulate the search query using NCBI search syntax
    search_query = (f'"{genus}"[Organism] AND "{start_date}"[PDAT] : "{end_date}"[PDAT]')

    # Connect to the database and execute the remote network search
    handle = Entrez.esearch(db="nucleotide", term=search_query)

    # Read and parse the lightweight XML response from NCBI
    record = Entrez.read(handle)

    # Always close the network handle to clean up system resources
    handle.close()

    # Extract the 'Count' field from the parsed dictionary
    total_count = record["Count"]

    return str(total_count)


if __name__ == "__main__":
    # Handle the input and output streams dynamically
    stream_input = sys.stdin
    result = count_genbank_records(stream_input)

    sys.stdout.write(result + "\n")
    sys.stdout.flush()