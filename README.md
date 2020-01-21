Document Classifier
===================

Document classification tool based on a domain-dependent, keywords-based document class map and a simple keyword frequency score.

Currently only financial statements (in CSV format) can be classified. A keyword-based class map for a given document type (stored as a JSON file in `static`) is used to create a frequency score for keywords occurring in a user-specified list of columns in the CSV document.

Scoring & Classification Functions
----------------------------------

The scoring function, for a given CSV document and a list of keywords, is given by

<div style="text-align:center"><img src="static/images/scoring_formula_indented.gif" alt="Scoring formula"/>

where ![](static/images/W_12pt.gif) is the set of ![](static/images/r_12pt.gif) keywords ![](static/images/keywords.gif) to search for, ![](static/images/C_12pt.gif) is the user-defined set of ![](static/images/m_12pt.gif) columns ![](static/images/columns.gif) in which to perform the keyword search (the ![](static/images/j_12pt.gif)-th column containing ![](static/images/m_12pt.gif) strings ![](static/images/column_strings.gif)), and ![](static/images/indicator_function_12pt.gif) is an indicator function for the presence of keywords in the ![](static/images/nm_12pt.gif) column entries ![](static/images/c_j,k_12pt.gif) given by

<div style="text-align:center"><img src="static/images/indicator_function_indented.gif" alt="Indicator function"/>

Note: the scoring function is guaranteed to be a value between 0 and 1 (inclusive) as the frequency score (numerator in the scoring function) can be a maximum of ![](static/images/rmn_12pt.gif).

Given a CSV document ![](static/images/D_12pt.gif) of type ![](static/images/T_12pt.gif), with ![](static/images/small_t_12pt.gif) classes ![](static/images/classes.gif) defined in its class keywords map (a JSON file with keys being the class names/IDs ![](static/images/classes.gif) and values being lists of keywords associated with the classes), and ![](static/images/C_12pt.gif) being the user-defined set of columns in which to perform the keywords search, the classification function is given by

<div style="text-align:center"><img src="static/images/classify_function_indented.gif" alt="Classification function"/>

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
