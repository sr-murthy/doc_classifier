__all__ = [
    'classify'
    'get_doc_class_map',
    'score'
]

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
