#!/usr/bin/env python

__all__ = [
    'classify'
    'get_doc_class_map',
    'score'
]

import argparse
import io
import json
import os

from collections import OrderedDict
from itertools import product

import pandas as pd


def get_doc_class_map(doc_type):

    with io.open(os.path.abspath(os.path.join('static', f'{doc_type}.json')), 'r', encoding='utf-8') as f:
        return json.load(f)


def score(line_items, keywords):

    return sum(
        1 if keyword in item.lower()
        else 0
        for keyword, item in product(keywords, line_items)
    ) / (len(keywords) * len(line_items))


def classify(doc_type, doc_fp, search_columns):

    df = pd.read_csv(doc_fp)
    df.columns = df.columns.str.lower()
    if 'name' in df.columns:
        df.rename(columns={'name': col_name for col_name in search_columns}, inplace=True)
    df.dropna(axis=0, subset=search_columns, inplace=True)
    line_items = df.loc[:, search_columns].values.ravel('F').tolist()
    class_map = get_doc_class_map(doc_type)
    scores = sorted(
        [(k, score(line_items, v)) for k, v in class_map.items()],
        key=lambda t: t[1],
        reverse=True
    )

    return scores[0][0], OrderedDict(scores)


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
