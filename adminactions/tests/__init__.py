from django.conf import settings
from .mass_update import *
from .exports import *
from .merge import MergeTest

if getattr(settings, 'ENABLE_SELENIUM', True):
    try:
        import selenium
        from .selenium_tests import *
    except ImportError:
        import warnings

        warnings.warn('Unable load Selenium. Selenium tests will be disabled')

