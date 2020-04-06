# -*- coding: utf-8 -*-

AUTHOR = 'Flávia Lopes'
SITENAME = "Flávia Lopes .Dev"
SITESUBTITLE = 'A personal blog.'
SITEDESCRIPTION = ''
BLOGKEYWORDS = ['Python','Developer', 'Data Science']
SITEURL = ''
TIMEZONE = "America/Sao_Paulo"

# Utiliza a data que estiver em metadata
#DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
LOCALE = 'C'
DEFAULT_LANG = 'pt-BR'

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True

PATH = 'blog_content/content'
ARTICLE_PATH = ['posts']
PAGE_PATHS = ['pages']
THEME = 'blog_themes/flavialopes.dev'
OUTPUT_PATH = 'blog_content/output'
STATIC_PATHS = [
    #'extra/robots.txt',
    'images',
    'notebooks',
    'pdfs',
    'pages']

DEFAULT_CATEGORY = 'python'

ARTICLE_URL = 'posts/{date:%Y}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%d}/{slug}.html'
ARTICLE_LANG_URL =  'posts/{date:%Y}/{date:%d}/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = 'posts/{date:%Y}/{date:%d}/{slug}-{lang}.html'
DRAFT_URL = 'drafts/{date:%Y}/{date:%d}/{slug}.html'
DRAFT_SAVE_AS = 'drafts/{date:%Y}/{date:%d}/{slug}.html'
DRAFT_LANG_URL = 'drafts/{date:%Y}/{date:%d}/{slug}-{lang}.html'
DRAFT_LANG_SAVE_AS = 'drafts/{date:%Y}/{date:%d}/{slug}-{lang}.html'

#verificar esta
#STATIC_CREATE_LINKS = False
#STATIC_CHECK_IF_MODIFIED = False
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives']



LOG_FILTER = []
# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}


# to call a static file: ![Alt Text]({filename}/images/han.jpg)
# static paths will be copied without parsing their contents



PLUGIN_PATHS = ["../blog_source/_plugins"]

# plugin author_images gera a imagem ou avatar pra cada autor.
PLUGINS = ['author_images', 'readtime', 'related_posts', 'share_post', 'thumbnailer',
           'autopages', 'better_figures_and_images', 'subcategory']

#author_images plugin
AUTHOR_AVATARS = 'images/author_avatars'
AUTHOR_IMAGES = 'images/author_images'

#related_posts plugin
RELATED_POSTS_MAX = 4
RELATED_POSTS_SKIP_SAME_CATEGORY = False

#thumbnailer plugin
IMAGE_PATH = 'images'
THUMBNAIL_DIR = 'images'
THUMBNAIL_KEEP_NAME = True
# wxh - will resize to exactly wxh
# wx? - will resize so that the width is the specified size, and the height will scale to retain aspect ratio
# ?xh - same as wx? but will height being a set size
# s is a shorthand for wxh where w=h
THUMBNAIL_SIZES = {
    'thumbnail_cover': '?x100',
    'thumbnail_post': '?x250'
}

#autopages plugin
AUTHOR_PAGE_PATH = 'pages/authors'
CATEGORY_PAGE_PATH = 'pages/categories'
TAG_PAGE_PATH = 'pages/tags'

#better_figures_and_images plugin
RESPONSIVE_IMAGES = True

#subcategories plugin
PATH_METADATA = 'posts/(?P<subcategory_path>.*)/.*'

# path-specific metadata
#EXTRA_PATH_METADATA = {
#    'extra/robots.txt': {'path': 'robots.txt'},
#    }

# Quando True as categorias são geradas conforme a organização das pastas
USE_FOLDER_AS_CATEGORY = True
SUMMARY_MAX_LENGTH = 40

GITHUB_URL = 'http://github.com/FlaviaLopes/'
REVERSE_CATEGORY_ORDER = True
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

FILENAME_METADATA = r'(?P<date>\d{2}-\d{2}-\d{4}).*'



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




# foobar will not be used, because it's not in caps. All configuration keys
# have to be in caps
foobar = "barbaz"