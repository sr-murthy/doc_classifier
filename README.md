Document Classifier
===================

Document classification tool based on a simple keyword frequency-in-columns score.

Currently only financial statements (in CSV format) can be classified. A keyword-based class map for a given document type (stored as a JSON file in `src/static`) is used to create a frequency score for keywords occurring in a user-specified list of columns in the CSV document.

Scoring Formula
---------------

The scoring formula is given by

    ![Scoring formula](static/scoring_formula_indented.gif)

where ![](static/W_12pt.gif) is the set of ![](static/r_12pt.gif) keywords ![](static/keywords.gif) to search for, ![](static/C_12pt.gif) is the set of ![](static/columns.gif) columns in which to perform the keyword search, and ![](static/indicator_function_12pt.gif) is an indicator function for the presence of keywords in column entries ![](static/c_i,j_12pt.gif) given by

    ![Indicator function for keywords in column entries](static/indicator_function_indented.gif)

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
