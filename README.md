# blastParser.py
Author: Virág Varga

Date: 25.01.2021

## Description

The program 'blastParser.py' parses NCBI BLASTp results and creates an output file containing selected categories of information for each query sequence.

## Usage

This program can be run from the command line in the following ways:

```./blastParser.py input_file output_file```

OR

```python blastParser.py input_file output_file```

## Results

The output file will contain a tab-delimited results file organized in the following manner:
 - Header line labeling the results columns in the following order: the query sequence name, the target sequence name, the e-value of the match, the identity percent of the match, and the match score.
 - Results lines: The results from the BLASTp organized according to the columns labeled in the header. Query sequences without BLASTp hits will still appear in the query column, but the rest of the row will be blank.

## Support

With questions, please contact the author of this program at:

virag.varga.bioinfo@gmail.com

## Project Status

Current Version: 1.0

While I have no explicit plans for a timeline to continue development of this program, I may return to ensure that this program will also work for other NCBI BLAST results, rather than just the BLASTp it was designed for.

## License

[MIT]
(https://choosealicense.com/licenses/mit/)
