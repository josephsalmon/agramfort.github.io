#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import bibtexparser
import pandas as pd

AUTHOR = u'Joseph Salmon'
SITENAME = u'Joseph Salmon'
SITEURL = ''

PATH = 'content'

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
PROFILE_IMG_URL = '/images/photo3.png'
PROFILE_IMAGE_URL = '/images/photo3.png'
FAVICON = 'images/favicon.ico'
# COVER_IMG_URL = './images/picture2.jpg'

GOOGLE_ANALYTICS = " UA-34336869-1"

# NOT_COURSE_LIST = ["contact", "news", "positions", "shortbio", "software", "team"]

STATIC_PATHS = ['code', 'images', 'enseignement', 'talks', 'papers', 'pdfs']
PAGE_EXCLUDES = ['code', 'enseignement', 'talks', 'papers', '.ipynb_checkpoints']
ARTICLE_EXCLUDES = ['code', 'enseignement', 'talks', 'papers', '.ipynb_checkpoints']
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
DEFAULT_DATE = 'fs'
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'

DEFAULT_PAGINATION = 5
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

PLUGIN_PATHS = ['../pelican-plugins']

# List of pages to appear in html exceptions:
TEMPLATE_PAGES = {'publications.html': 'publications.html',
                  'teaching.html': 'teaching.html',
                  'talks.html': 'talks.html',
                  'SD204.html': 'SD204.html',
                  'HLMA310.html': 'HLMA310.html',
                  'HMMA308.html': 'HMMA308.html',
                  'STAT593.html': 'STAT593.html',
                  'M2MO.html': 'M2MO.html',
                  'MDI720.html': 'MDI720.html',
                  'SD3.html': 'SD3.html',
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

with open('./data/Salmon.bib') as bib:
    bib_str = bib.read()

records = bibtexparser.loads(bib_str)

one_records = bibtexparser.loads(bib_str)
for k, item in enumerate(records.entries):
    one_records.entries = records.entries[k:k + 1]
    print(item['author'])
    item['author'] = make_nice_author(item['author'])
    for key in ['annote', 'owner', 'group', 'topic']:
        if key in item:
            del item[key]
    item['bibtex'] = bibtexparser.dumps(one_records).strip()
    item['title'] = make_nice_title(item['title'])
    item['index'] = k

records.entries.sort(key=lambda record: record['year'], reverse=True)

PUBLICATION_LIST = records.entries[:]
PUBLICATION_LIST_SHORT = PUBLICATION_LIST[:7]
