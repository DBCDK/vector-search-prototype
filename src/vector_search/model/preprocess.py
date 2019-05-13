#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- mode: python -*-
"""

===============
Preprocess Text
===============

Preprocesses fulltext

for each fulltext the first n characters are isolated and summation is
created with at most m words (using TextRank - see
https://radimrehurek.com/gensim/summarization/summariser.html)
The summation is then stemmed and normalized.

The output data consists of a map of pids and texts.
"""
import json
import os
import tqdm
from gensim.summarization.summarizer import summarize
import gensim.parsing.preprocessing as pre


FILTERS = [pre.strip_tags,
           pre.strip_punctuation,
           pre.strip_multiple_whitespaces,
           pre.strip_numeric,
           pre.strip_short]


def text_iter(text_dir, limit=None):
    """ yields pairs of pids and text """
    for i, path in tqdm.tqdm(enumerate(os.listdir(text_dir))):
        if limit and i >= limit:
            break
        with open(os.path.join(text_dir, path)) as fh:
            content = fh.read()
            yield path.rsplit('.')[0], content


def extract_sentences(text_gen, max_char=50000, word_count=5000, limit=None):
    """ yields pairs of pids and extracted text """
    for i, (label, text) in enumerate(text_gen):
        if limit and i >= limit:
            break
        try:
            yield label, summarize(text[:max_char], word_count=word_count).replace('\n', ' ')
        except Exception:
            pass


def stem_text(text_gen):
    for label, text in text_gen:
        yield label, " ".join(pre.preprocess_string(text))


def process_text(text_dir, limit=None, max_char=50000, word_count=5000, outfile_prefix='text-data'):
    """ Processes texts and outputs result to file """
    text_gen = text_iter(text_dir, limit=limit)
    text_gen = extract_sentences(text_gen, max_char=max_char, word_count=word_count)
    text_gen = stem_text(text_gen)

    print(f"processing texts (text_dir: {text_dir})")
    data = {label: text for label, text in text_gen}

    filename = f"{outfile_prefix}-{max_char}-{word_count}-{len(data)}.json"

    print(f'Writing result to {filename}')
    with open(filename, 'w') as fh:
        json.dump(data, fh)


def cli():
    """ Commandline interface """
    import argparse
    parser.add_argument('path',
                        help='path of to textfiles')
    parser.add_argument('-l', '--limit', dest='limit', type=int,
                        help='limits number of texts to use', default=None)
    parser.add_argument('-m', '--max-char', dest='max_char', type=int,
                        help='number of char in slice of text to use. default is 50.000', default=50_000)
    parser.add_argument('-w', '--word-count', dest='word_count', type=int,
                        help='number of words retained for each text. default is 5.000', default=5000)
    parser.add_argument('-o', '--outfile-prefix', dest='outfile',
                        help='output file prefix. default is "fuldtekst"', default='fuldtekst')
    args = parser.parse_args()


if __name__ == '__main__':
    cli()
