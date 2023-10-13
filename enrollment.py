"""Enrollment analysis:  Summary report of majors enrolled in a class.
CS 210 project, Fall 2022.
Author:  Finn Fujimura
Credits: The Python Standard Library CSV File Reading and Writing
"""
import doctest
import csv
def read_csv_column(path: str, field: str) -> list[str]:
    """Read one column from a CSV file with headers into a list of strings.

    >>> read_csv_column("data/test_roster.csv", "Major")
    ['DSCI', 'CIS', 'BADM', 'BIC', 'CIS', 'GSS']
    """
    with open(path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        columnlist = [row[field] for row in reader]
    return columnlist

def counts(column: list[str]) -> dict[str, int]:
    """Returns a dict with counts of elements in column.

    >>> counts(["dog", "cat", "cat", "rabbit", "dog"])
    {'dog': 2, 'cat': 2, 'rabbit': 1}
    """
    el_counts = {}
    for f in column:
        if f in el_counts:
            el_counts[f] += 1
        else:
            el_counts[f] = 1
    return el_counts
        
def read_csv_dict(path: str, key_field: str, value_field: str) -> dict[str, dict]:
    """Read a CSV with column headers into a dict with selected
    key and value fields.

    >>> read_csv_dict("data/test_programs.csv", key_field="Code", value_field="Program Name")
    {'ABAO': 'Applied Behavior Analysis', 'ACTG': 'Accounting', 'ADBR': 'Advertising and Brand Responsibility'}
    """
    table = {}
    with open(path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            labelkey = row[key_field]
            labelvalue = row[value_field]
            table[labelkey] = labelvalue
    return table

def items_v_k(dict):
    '''Extracts a list of (value, key) pairs from a dictionary
    >>> items_v_k({1: 'Hi', 2: 'Hello', 3: 'Hey'})
    [('Hi', 1), ('Hello', 2), ('Hey', 3)]
    '''
    return [(value, key) for key, value in dict.items()]
def main():
    doctest.testmod()
    majors = read_csv_column("data/roster_selected.csv", "Major")
    counts_by_major = counts(majors)
    program_names = read_csv_dict("data/programs.csv", "Code", "Program Name")
    # Convert to list of (count, code)
    by_count = items_v_k(counts_by_major)
    by_count.sort(reverse=True)  # From largest to smallest
    for count, code in by_count:
        program = program_names[code]
        print(count, program)

if __name__ == "__main__":
    main()

'''Read roster CSV file into a single list with major codes. 
Count elements in list of major codes, keeping a summary in a dict 
   that maps major code to count. 
Sort the (major code, count) elements from the dict, giving a list 
from largest count to smallest. 
Read program CSV file into a dict that maps program codes (the same 
as major codes) into program names. 
For each (major code, count) pair,  
    look up major code to get program name
    print count and program name
    '''