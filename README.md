Document Classifier
===================

Document classification tool based on a document type-dependent keywords class map and a simple normalised keyword frequency-in-columns score.

Currently only financial statements (in CSV format) can be classified. A keyword-based class map for a given document type (stored as a JSON file in `src/static`) is used to create a frequency score for keywords occurring in a user-specified list of columns in the CSV document.

Scoring & Classification Functions
----------------------------------

The scoring function, for a given CSV document and a list of keywords, is given by

<div style="text-align:center"><img src="src/static/scoring_formula_indented.gif" alt="Scoring formula"/>

where ![](src/static/w_12pt.gif) is the set of ![](src/static/r_12pt.gif) keywords ![](src/static/keywords.gif) to search for, ![](src/static/C_12pt.gif) is the user-defined set of ![](src/static/m_12pt.gif) columns ![](src/static/columns.gif) in which to perform the keyword search (the ![](src/static/j_12pt.gif)-th column containing ![](src/static/m_12pt.gif) strings ![](src/static/column_strings.gif)), and ![](src/static/indicator_function_12pt.gif) is an indicator function for the presence of keywords in the ![](src/static/nm_12pt.gif) column entries ![](src/static/c_j,k_12pt.gif) given by

<div style="text-align:center"><img src="src/static/indicator_function_indented.gif" alt="Indicator function"/>

Note: the scoring function is guaranteed to be a value between 0 and 1 (inclusive) as the frequency score (numerator in the scoring function) can be a maximum of ![](src/static/rmn_12pt.gif).

Given a CSV document ![](src/static/D_12pt.gif) of type ![](src/static/T_12pt.gif), with ![](src/static/small_t_12pt.gif) classes ![](src/static/classes.gif) defined in its class keywords map (a JSON file with keys being the class names/IDs ![](src/static/classes.gif) and values being lists of keywords associated with the classes), and ![](src/static/C_12pt.gif) being the user-defined set of columns in which to perform the keywords search, the classification function is given by

<div style="text-align:center"><img src="src/static/classify_function_indented.gif" alt="Classification function"/>

Usage
-----

Here's a simple example of classifying a sample income statement with only a single keywords-search column .

    [path/to/doc_classifier/src]$ ./classify.py -t 'financial statements' -f ../sample_data/income_statement/microsoft.csv --verbose

    Classification: income
    Keywords score map: {
        "income": 0.03428571428571429,
        "cash flow": 0.013333333333333334,
        "balance sheet": 0.0
    }

This is an example of classifying a sample income statement with multiple keywords-search columns.

    [/path/to/doc_classifier/src]$ ./classify.py -t 'financial statements' -f ../sample_data/income_statement/microsoft2.csv  -c 'line item 1, line item 2' --verbose

    Classification: income
    Keywords score map: {
        "income": 0.025714285714285714,
        "cash flow": 0.006666666666666667,
        "balance sheet": 0.0
    }
