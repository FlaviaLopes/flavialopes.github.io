# -*- coding: utf-8 -*-

AUTHOR = 'Flávia Lopes'
SITENAME = "Flávia Lopes .Dev"
SITESUBTITLE = 'A personal blog.'
SITEURL = ''
TIMEZONE = "America/Sao_Paulo"
DEFAULT_DATA = '%DD%MM%YYYY'
LANGUAGE = 'pt'
# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True

THEME = 'themes/flavialopes.dev'
HEADER = 'theme/images/avatar.jpg'
SITEICON = 'theme/images/favicon.ico'
#MONTH_ARCHIVE_SAVE_AS = True
#YEAR_ARCHIVE_SAVE_AS = True

# FEED_ATOM
# FEED_RSS
# FEED_ALL_ATOM
# FEED_ALL_RSS
# CATEGORY_FEED_ATOM
# CATEGORY_FEED_RSS
# AUTHOR_FEED_ATOM
# AUTHOR_FEED_RSS
# TAG_FEED_ATOM
# TAG_FEED_RSS
# TRANSLATION_FEED_ATOM
# TRANSLATION_FEED_RSS

GITHUB_URL = 'http://github.com/FlaviaLopes/'
#DISQUS_SITENAME = "blog-notmyidea"
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_PAGINATION = 10

#FEED_ALL_RSS = 'feeds/all.rss.xml'
#CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'
BLOGKEYWORDS = ['Python','Developer', 'Data Science']

COMMENT = True
JIATHIS = True

LINKS = (('Genetic Algorithm with Python', 'https://www.github.com/FlaviaLopes/Genetic-Algorithm'),
         ('Acelera Dev Data Science', "https://www.github.com/FlaviaLopes/AceleraDev-Codenation-Data-Science"),
         ('Eleições 2018', "https://www.github.com/FlaviaLopes/Eleicoes-2018"),)

SOCIAL = (('twitter', 'https://twitter.com/_flavialopes_'),
          ('linkedin', 'https://linkedin.com/in/lopesflavia'),
          ('github', 'https://github.com/FlaviaLopes'),)

# global metadata to all the contents
DEFAULT_METADATA = {'yeah': 'it is'}

# path-specific metadata
#EXTRA_PATH_METADATA = {
#    'extra/robots.txt': {'path': 'robots.txt'},
#    }

# static paths will be copied without parsing their contents
#STATIC_PATHS = [
#    'pictures',
#    'extra/robots.txt',
#    ]

# custom page generated with a jinja2 template
#TEMPLATE_PAGES = {'pages/jinja2_template.html': 'jinja2_template.html'}

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

# foobar will not be used, because it's not in caps. All configuration keys
# have to be in caps
foobar = "barbaz"
