from ella.utils.settings import Settings
from django.utils.datetime_safe import datetime

gettext = lambda s: s

# Caching-related
CACHE_TIMEOUT = 10 * 60
CACHE_TIMEOUT_LONG = 60 * 60

DOUBLE_RENDER = False
DOUBLE_RENDER_EXCLUDE_URLS = None

# Box
BOX_INFO = 'ella.core.box.BOX_INFO'
MEDIA_KEY = 'ella.core.box.MEDIA_KEY'

# Publishing configuration
CATEGORY_LISTINGS_PAGINATE_BY = 20
DEFAULT_LISTING_PRIORITY = 0
USE_PRIORITIES = False
LISTING_UNIQUE_DEFAULT_SET = 'unique_set_default'
PUBLISH_FROM_WHEN_EMPTY = datetime(3000, 1, 1)
LISTING_USE_COMMERCIAL_FLAG = False

RELATED_FINDERS = {
    'default': (
        'ella.core.related_finders.directly_related',
        'ella.core.related_finders.related_by_category',
    ),
    'directly': (
        'ella.core.related_finders.directly_related',
    )
}

LISTING_HANDLERS = {
    'default': 'ella.core.managers.ModelListingHandler',
}

# Category settings
CATEGORY_TEMPLATES = (
    ('category.html', gettext('default (category.html)')),
)

# context_processor
MEDIA_URL = ''
STATIC_URL = MEDIA_URL
VERSION = 1
SERVER_INFO = {}

RSS_NUM_IN_FEED = 10
RSS_ENCLOSURE_PHOTO_FORMAT = None
RSS_DESCRIPTION_BOX_TYPE = 'rss_description'

# middlewares
ECACHE_INFO = 'ella.core.middleware.ECACHE_INFO'

# templates
ARCHIVE_TEMPLATE = True

core_settings = Settings('ella.core.conf', '')
