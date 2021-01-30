#!/bin/python
"""
Title: blastParser.py
Date: 2021-01-25
Authors: Virág Varga

Description:
	This program parses BLASTp results and creates an output file containing selected
	 	categories of information for each query sequence.

List of functions:
	No functions are defined in this script.

List of standard and non-standard modules used:
	sys
	re

Procedure:
	1. Assigning command line arguments and output file name; loading modules.
	2. Creating a dictionary containing the pertinent results of the BLASTp file.
	3. Writing out the results to a file.

Known bugs and limitations:
	- This BLAST Parser is made specifically to suit the formatting of the NCBI BLASTp output files.
	- There is no quality-checking integrated into the code.

Usage
	./blastParser.py input_file output_file
	OR
	python blastParser.py input_file output_file

This script was written for Python 3.8.6, in Spyder 4.
"""

#Part 1: Setup

#allow the program to be executed from the command line
import sys
#allow use of regex matching
import re

#assign command line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]


#Part 2: Parse through the file to create dictionaries with the desired information
#Part 3: Write out the results to the output file

#create empty dictionary to contain the data that will be written out
target_dict = {}

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
	#open the input BLASTp result file for reading
	#open the output file for writing
	for line in infile:
		#read through the file line by line
		seq_id = "none"
		#create empty variable for target ids
		seq_list = [None] * 3
		#empty list seq_list will hold the alignment data associated with each query-target match
		#with each iteration of the loop, this list is overwritten
		if line.startswith('Query='):
			#identify lines that start with "Query=" - these lines will contain the query sequences
			query_id = line.split()[1]
			#the line with the query id is 'split' - separated into a list based on the locations of spaces
			#the item with index 1 in that list is the query sequence name
			#the query sequence name is placed into the variable query_id
		elif line.startswith(">"):
			#identify lines that start with ">" character - these contain target sequence names
			seq_id = line.strip()[1:]
			#the "\n" character is removed, and all but the first character (">") are put into variable seq_id
			query2seq = query_id + "\t" + seq_id
			#variable query2seq contains a string with the query_id and seq_id separated by a tab ("\t")
			next(infile)
			next(infile)
			#2 lines are skipped, before 3rd line is assigned to variable line1
			line1 = next(infile)
			#line1 contains the first line of query-target BLASTp statistics
			line1 = re.sub('[(),]', '', line1)
			#regex is used to remove '(', ')' and ',' characters from line1
			line1 = line1.split()
			#elements of line2 are separated into a list based on the locations of spaces
			seq_list[2] = line1[4]
			#the score value is input into list seq_list
			seq_list[0] = line1[7]
			#the e-value is input into list seq_list
			line2 = next(infile)
			#line2 contains the second line of query-target BLASTp statistics
			line2 = re.sub('[(),%]', '', line2)
			#regex is used to remove '(', ')', ',' and '%'' characters from line2
			line2 = line2.split()
			#elements of line2 are separated into a list based on the locations of spaces
			seq_list[1] = line2[3]
			#the identity % is input into list seq_list
			target_dict[query2seq] = seq_list
			#the query2seq variable is used as the key to the target_dict dictionary
			#the associated value is the contents of list seq_list
		elif line.startswith("***** No hits found *****"):
			#for queries with no BLASTp hits
			empty_list = ['none']
			#a list empty_list containing only the string "none" is created
			#this becomes the value associated with this entry into dictionary target_dict
			target_dict[query_id] = empty_list
	outfile.write("#query" + "\t" + "target" + "\t" + "e-value" + "\t" + "identity(%)" + "\t" + "score" + "\n")
	#the header line is prepared and written out to the output file
	for targetKey in target_dict:
		#iterate through the target_dict dictionary using its keys
		if target_dict[targetKey] == ['none']:
			#pick out query ids with no target matches
			outfile.write('{}\t\t\t\t\n'.format(targetKey))
			#the query id is written out, followed by tabs (to keep column formatting) and a newline character ("\n")
		else:
			outfile.write('{}\t{}\t{}\t{}\n'.format(targetKey, target_dict[targetKey][0], target_dict[targetKey][1], target_dict[targetKey][2]))
			#results are written out to the output file with appropriate formatting
