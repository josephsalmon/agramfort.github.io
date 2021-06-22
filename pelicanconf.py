#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import re
import bibtexparser
import pandas as pd

AUTHOR = u'Joseph Salmon'
SITENAME = u'Joseph Salmon'
SITEURL = 'http://josephsalmon.eu'

PATH = 'content'
PAGES = 'pages'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget

SOCIAL = (
    ('github', 'https://github.com/josephsalmon'),
    ('twitter-square', 'https://twitter.com/salmonjsph'),
)

DEFAULT_PAGINATION = 10
PAGE_ORDER_BY = 'sortorder'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "themes/pure-alex"
PROFILE_IMG_URL = '/images/joseph_2018.png'
PROFILE_IMAGE_URL = '/images/joseph_2018.png'
FAVICON = 'images/favicon.ico'
# COVER_IMG_URL = './images/picture2.jpg'

GOOGLE_ANALYTICS = " UA-34336869-1"

# NOT_COURSE_LIST = ["contact", "news", "positions", "shortbio", "software", "team"]

STATIC_PATHS = ['code', 'images', 'enseignement',
                'talks', 'papers']
PAGE_EXCLUDES = ['misc', 'code', 'enseignement', 'talks',
                 'papers', '.ipynb_checkpoints']
ARTICLE_EXCLUDES = ['code', 'enseignement', 'talks', 'papers',
                    '.ipynb_checkpoints']
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = False
DEFAULT_DATE = 'fs'
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'

DEFAULT_PAGINATION = 5
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

PLUGIN_PATHS = ['../pelican-plugins']

# List of pages to appear in html exceptions:
# should be put in content/pages. and also create pure-alex/templates/****.html
TEMPLATE_PAGES = {'publications.html': 'publications.html',
                  'teaching.html': 'teaching.html',
                  'talks.html': 'talks.html',
                  'misc.html': 'misc.html',
                  'HMMA308.html': 'HMMA308.html',
                  'HMMA307.html': 'HMMA307.html',
                  'HMMA237.html': 'HMMA237.html',
                  'HMMA238.html': 'HMMA238.html',
                  'HLMA408.html': 'HLMA408.html',
                  'HLMA310.html': 'HLMA310.html',
                  'STAT593.html': 'STAT593.html',
                  'M2MO.html': 'M2MO.html',
                  'MDI720.html': 'MDI720.html',
                  'SD3.html': 'SD3.html',
                  'SD204.html': 'SD204.html',
                  'M53010.html': 'M53010.html',
                  }

# Publications


def make_link_author_website(author):
    names_url = pd.read_csv('./data/coauthors_url.csv',
                            header='infer')
    url = names_url.loc[names_url.name==author, 'url'].values[0]
    string_author_website = "<a href=" + url + ">" + author + "</a>"
    return string_author_website


def make_nice_author(author, emphasize='Salmon, J.'):
    split_author = author.split(' and ')
    insert_pos = len(split_author) - 1
    names_split = [au.split(', ') for au in split_author]
    names = ['{} {}'.format(n[1], n[0]) for n in names_split]
    names_url = [make_link_author_website(n) for n in names]
    if len(split_author) > 1:
        author_edit = ', '.join(names_url[:insert_pos]) + ' and ' + names_url[insert_pos]
    else:
        author_edit = names_url[insert_pos]
    if emphasize:
        author_edit = author_edit.replace(
            emphasize, '<strong><em>' + emphasize + '</em></strong>')
    return author_edit


def make_nice_title(title):
    title = title.replace('{', '')
    title = title.replace('}', '')
    return title

""" XXX
- make sure not to use unicode or LaTeX code
- only full author records, in "surname, name and" format
"""

def get_bib_entries(bib_fname):
    with open(bib_fname) as bib:
        bib_str = bib.read()

    parser = bibtexparser.bparser.BibTexParser(common_strings=True)
    records = parser.parse(bib_str)
    parser2 = bibtexparser.bparser.BibTexParser(common_strings=True)
    one_records = parser2.parse(bib_str)

    entries = []

    for k, item in enumerate(records.entries):
        one_records.entries = records.entries[k:k + 1]
        item['author'] = make_nice_author(item['author'])
        for key in ['annote', 'owner', 'group', 'topic']:
            if key in item:
                del item[key]

        bibtex_str = bibtexparser.dumps(one_records).strip()

        regex = r"author = {[^}]*}"
        matches = list(re.finditer(regex, bibtex_str, re.MULTILINE))
        assert len(matches) == 1
        match = matches[0]
        start, stop = match.start(), match.end()
        author_str = bibtex_str[start:stop]
        author_str_ok = ''
        splits = author_str.split(', ')
        for k, s in enumerate(splits):
            # if ((k % 2 == 0) and k < (len(splits) - 2)):
            if (k > 0):
                author_str_ok += ' and '
            # else:
                # author_str_ok += ', '
            author_str_ok += s

        bibtex_str_ok = bibtex_str[:start] + author_str_ok + bibtex_str[stop:]
        item['bibtex'] = bibtex_str_ok

        item['title'] = make_nice_title(item['title'])
        item['index'] = k
        if 'url' in item:
            item['link'] = item['url']
        entries.append(item)
    return entries


entries = get_bib_entries('./data/Salmon.bib')
entries.sort(key=lambda record: record['year'], reverse=True)
PUBLICATION_LIST = entries[:]
PUBLICATION_LIST_SHORT = PUBLICATION_LIST[:7]
