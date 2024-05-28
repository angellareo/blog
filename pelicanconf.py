AUTHOR = "Angel Lareo"
SITENAME = "Disceres"
# SITESUBTITLE = "A personal blog."
SITEURL = "https://angellareo.github.io/blog"
TIMEZONE = 'Europe/Madrid'
DEFAULT_LANG = 'es'

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = False

GITHUB_URL = "http://github.com/angellareo/"
# DISQUS_SITENAME = "blog-notmyidea"
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_PAGINATION = 6 
#DEFAULT_DATE = (2012, 3, 2, 14, 1, 1)

#FEED_ALL_RSS = "feeds/all.rss.xml"
#CATEGORY_FEED_RSS = "feeds/{slug}.rss.xml"

LINKS = (
#    ("Biologeek", "http://biologeek.org"),
#    ("Filyb", "http://filyb.info/"),
#    ("Libert-fr", "http://www.libert-fr.com"),
#    ("N1k0", "http://prendreuncafe.com/blog/"),
#    ("Tarek Ziadé", "http://ziade.org/blog"),
#    ("Zubin Mithra", "http://zubin71.wordpress.com/"),
)

SOCIAL = (
    ("twitter", "http://twitter.com/ALFXogo"),
#    ("lastfm", "http://lastfm.com/user/akounet"),
    ("github", "http://github.com/angellareo"),
)

PROFILE_IMAGE = 'avatar.png'

# global metadata to all the contents
DEFAULT_METADATA = {"yeah": "it is"}

# path-specific metadata
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
}

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    "images",
    "extra/robots.txt",
]

# custom page generated with a jinja2 template
# TEMPLATE_PAGES = {"pages/jinja2_template.html": "jinja2_template.html"}

# there is no other HTML content
READERS = {"html": None}

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {"linenos": "table"}

# foobar will not be used, because it's not in caps. All configuration keys
# have to be in caps
foobar = "barbaz"

THEME = 'themes/okulto'
OUTPUT_PATH = 'output'
PATH = 'content'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'

# Custom Home page
DIRECT_TEMPLATES = (('index', 'blog', 'tags', 'categories', 'archives'))
PAGINATED_DIRECT_TEMPLATES = (('blog',))
TEMPLATE_PAGES = {'home.html': 'index.html',}
MENUITEMS = {
    ('Blog', 'blog.html')
}
