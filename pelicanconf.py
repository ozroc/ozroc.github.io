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
PLUGINS = ['ipynb.markup', 'share_post']

THEME = 'theme' #'pelican-themes/pelican-bootstrap3'

# Blogroll
LINKS = (("A Telecom's Blog", 'http://bluetc.es/en/sharing-and-engaging/a-telecoms-blog/blogger/listings/pablo-garcia'),
         )

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

MAIL = 'pablo.manuel.garcia@blue-tc.com'

TWITTER_USER = 'PablomgcBlue'

#LINKEDIN_USER = 'in/pablomgc'

ABOUT_IMAGE = "images/about.jpg"

#ABOUT_LINK = ""

ABOUT_TEXT = """
<script type="text/javascript" src="https://platform.linkedin.com/badges/js/profile.js" async defer></script>

<div class="LI-profile-badge"  data-version="v1" data-size="large" data-locale="es_ES" data-type="horizontal" data-theme="light" data-vanity="pablomgc"><a class="LI-simple-link" href='https://es.linkedin.com/in/pablomgc?trk=profile-badge'>Pablo Manuel García Corzo</a></div>
"""

DEFAULT_PAGINATION = 10

DISPLAY_CATEGORIES_ON_MENU = True

DISQUS_SITENAME = 'ozroc'
