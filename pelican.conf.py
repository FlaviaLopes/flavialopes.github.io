# -*- coding: utf-8 -*-

AUTHOR = 'Flávia Lopes'
SITENAME = "Flávia Lopes .Dev"
SITESUBTITLE = 'A personal blog.'
SITEDESCRIPTION = ''
BLOGKEYWORDS = ['Python','Developer', 'Data Science']
SITEURL = ''
TIMEZONE = "America/Sao_Paulo"

# Utiliza a data que estiver em metadata
DEFAULT_DATE = 'fs'
DEFAULT_LANG = 'pt-BR'

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True

THEME = 'blog_themes/flavialopes.dev'
#THEME_STATIC_DIR = 'blog_themes/flavialopes.dev/static'
OUTPUT = 'blog_content/output'
PATH = 'blog_content/content'

# to call a static file: ![Alt Text]({filename}/images/han.jpg)
# static paths will be copied without parsing their contents
STATIC_PATHS = [
    #'extra/robots.txt',
    'images',
    'notebooks',
    'pdfs']


PLUGIN_PATHS = ["../blog_source/pelican-plugins"]

# plugin author_images gera a imagem ou avatar pra cada autor.
PLUGINS = ['author_images', 'readtime']

AUTHOR_AVATARS = 'images/author_avatars'
AUTHOR_IMAGES = 'images/author_images'

# path-specific metadata
#EXTRA_PATH_METADATA = {
#    'extra/robots.txt': {'path': 'robots.txt'},
#    }

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'

# Quando True as categorias são geradas conforme a organização das pastas
USE_FOLDER_AS_CATEGORY = False
SUMMARY_MAX_LENGTH = 40

GITHUB_URL = 'http://github.com/FlaviaLopes/'
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_PAGINATION = 10

DISPLAY_PAGES_ON_MENU = True
COMMENT = True
JIATHIS = True

PROJECTS = (('Genetic Algorithm with Python', 'https://www.github.com/FlaviaLopes/Genetic-Algorithm'),
         ('Acelera Dev Data Science', "https://www.github.com/FlaviaLopes/AceleraDev-Codenation-Data-Science"),
         ('Eleições 2018', "https://www.github.com/FlaviaLopes/Eleicoes-2018"),)

SOCIAL = (('twitter', 'https://twitter.com/_flavialopes_'),
          ('linkedin', 'https://linkedin.com/in/lopesflavia'),
          ('github', 'https://github.com/FlaviaLopes'),
          ('instagram', 'https://instagram.com/lopesflavia'),
          ('facebook', 'https://facebook.com/flavialopesads'),)

# global metadata to all the contents
DEFAULT_METADATA = {
    'status': 'draft',
    'favicon': 'images/favicon.ico',
    'avatarblog': 'images/avatar.jpg'
}
# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

#FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'
#DOWNLOAD_METADATA = '(?P<>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'

#If you want to exclude any pages from being linked to or listed
# in the menu then add a status: hidden attribute to its metadata.

#HEADER = 'blog_themes/flavialopes.dev/static/images/author_avatars/avatar.jpg'
#SITEICON = 'theme/images/favicon.ico'
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


#FEED_ALL_RSS = 'feeds/all.rss.xml'
#CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'

# custom page generated with a jinja2 template
#TEMPLATE_PAGES = {'pages/jinja2_template.html': 'jinja2_template.html'}



# foobar will not be used, because it's not in caps. All configuration keys
# have to be in caps
foobar = "barbaz"
