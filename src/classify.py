#!/usr/bin/env python

import argparse
import os
import json

from lib import classify

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-t', '--doc-type',
        required=True,
        help='Document type (at the moment only financial statements are supported)'
    )
    parser.add_argument(
        '-f', '--doc-path',
        type=str,
        required=True,
        help='Document file path (relative or absolute)'
    )
    parser.add_argument(
        '-c', '--search_columns',
        type=str,
        required=True,
        help='Comma-separated string of columns to search for keywords'
    )
    parser.add_argument(
        '-v', '--verbose',
        default=False,
        help="Verbose output",
        action="store_true"
    )

    args = parser.parse_args()
    doc_type = '_'.join(args.doc_type.split())
    doc_fp = args.doc_path
    search_columns = [c.strip() for c in args.search_columns.split(',')]
    verbose = args.verbose
    if not os.path.isabs(doc_fp):
        doc_fp = os.path.abspath(doc_fp)

    classification, score_map = classify(doc_type, doc_fp, search_columns)

    if not verbose:
        print(f'\nClassification: {classification}\n')
    else:
        print(f'\nClassification: {classification}')
        print(f'Keywords score map: {json.dumps(score_map, indent=4)}\n')
