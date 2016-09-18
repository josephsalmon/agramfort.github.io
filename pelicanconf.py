#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Alexandre Gramfort'
SITENAME = u'Alexandre Gramfort'
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
    ('github', 'https://github.com/agramfort/'),
    ('twitter-square', 'https://twitter.com/agramfort'),
    ('ai-google-scholar-square', 'https://scholar.google.com/citations?user=fhxshS0AAAAJ')
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# THEME = 'themes/pelican-blue'
# THEME = "themes/pure-single"
THEME = "themes/pure"
# COVER_IMG_URL = './images/cajal.jpg'
PROFILE_IMG_URL = './images/picture2.jpg'
# COVER_IMG_URL = './images/picture2.jpg'
PROFILE_IMAGE_URL = './images/picture2.jpg'

GOOGLE_ANALYTICS = "UA-112258-9"

STATIC_PATHS = ['images', 'pdfs', 'widgets']
PAGE_EXCLUDES = ['widgets', '.ipynb_checkpoints']
ARTICLE_EXCLUDES = ['widgets', '.ipynb_checkpoints']
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
DEFAULT_DATE = 'fs'
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'

DEFAULT_PAGINATION = 5
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

PLUGIN_PATHS = ['../pelican-plugins']

