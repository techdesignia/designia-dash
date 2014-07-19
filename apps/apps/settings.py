# django template_dirs- text added so WingIDE will recognize this as a django project.
from settings_default import *
try:
    from settings_local import *
except ImportError:
    print "Unable to import settings_local. Using settings_default (aka, Production database)"
