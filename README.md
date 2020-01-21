Document Classifier
===================

Document classification tool based on a simple keyword frequency-in-columns score.

Currently only financial statements (in CSV format) can be classified. A keyword-based class map for a given document type (stored as a JSON file in `src/static`) is used to create a frequency score for keywords occurring in a user-specified list of columns in the CSV document.

Scoring Formula
---------------

The scoring formula is given by

<div style="text-align:center"><img src="src/static/scoring_formula_indented.gif" alt="Scoring formula"/>

where ![](src/static/w_12pt.gif) is the set of ![](src/static/r_12pt.gif) keywords ![](src/static/keywords.gif) to search for, ![](src/static/C_12pt.gif) is the set of ![](src/static/m_12pt.gif) columns ![](src/static/columns.gif) in which to perform the keyword search (the ![](src/static/j_12pt.gif)-th column containing ![](src/static/m_12pt.gif) strings ![](src/static/column_strings.gif)), and ![](src/static/indicator_function_12pt.gif) is an indicator function for the presence of keywords in the ![](src/static/nm_12pt.gif) column entries ![](src/static/c_j,k_12pt.gif) given by

<div style="text-align:center"><img src="src/static/indicator_function_indented.gif" alt="Indicator function"/>

Usage examples.

    [path/to/doc_classifier/src]$ ./classifier.py -t 'financial statements' -f ../sample_data/income_statement/microsoft.csv

    Classification: income

    [path/to/doc_classifier/src]$ ./classifier.py -t 'financial statements' -f ../sample_data/income_statement/microsoft.csv --verbose

    Classification: income
    Keywords score map: {
        "income": 0.03428571428571429,
        "cash flow": 0.013333333333333334,
        "balance sheet": 0.0
    }
