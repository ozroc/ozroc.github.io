#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Pablo Manuel Garc\xeda Corzo'
SITENAME = u'The Awesome Adventures of a Drinking Bird'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']

THEME = 'theme'

# Blogroll
LINKS = (("A Telecom's Blog", 'http://bluetc.es/en/sharing-and-engaging/a-telecoms-blog/blogger/listings/pablo-garcia'),
         )

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

MAIL = 'pablo.manuel.garcia@blue-tc.com'

TWITTER_USER = 'PablomgcBlue'

LINKEDIN_USER = 'pablomgc'

ABOUT_IMAGE = "images/about.jpg"

#ABOUT_LINK = ""

ABOUT_TEXT = """As a physicist, I started my career at the Nuclear Physics Group in the Universidad Complutense de Madrid where I became interested in the technical part of the work, linked to computational physics and Linux systems management.
In 2012 I left the academic world and I started working for BlueTC as an external consultant in Ericsson R&D. There I began to develop my activity mainly as a Python developer of automation systems and testing facilities for continuous integration. In December 2014 I joined BlueTC's Solutions area, where I started working on projects related to Openstack, NFV/SDN and integrating analytics solutions with traditional monitoring environments.
"""

DEFAULT_PAGINATION = 10

DISPLAY_CATEGORIES_ON_MENU = True
