#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import bibtexparser


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

STATIC_PATHS = ['images', 'pdfs', 'widgets']
PAGE_EXCLUDES = ['widgets', '.ipynb_checkpoints']
ARTICLE_EXCLUDES = ['widgets', '.ipynb_checkpoints']
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

TEMPLATE_PAGES = {'publications.html': 'publications.html'}

# Publications


def make_nice_author(author, emphasize='Salmon, J.'):
    split_author = author.split(' and ')
    insert_pos = len(split_author) - 1
    names_split = [au.split(', ') for au in split_author]
    names = ['{}, {}.'.format(n[0], n[1][:1]) for n in names_split]
    if len(split_author) > 1:
        author_edit = ', '.join(names[:insert_pos]) + ' and ' + names[insert_pos]
    else:
        author_edit = names[insert_pos]
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
