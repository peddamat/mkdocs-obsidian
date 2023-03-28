# import os
# import sys
# from timeit import default_timer as timer
# from datetime import datetime, timedelta

# from mkdocs import utils as mkdocs_utils
# from mkdocs.config import config_options, Config
# from mkdocs.plugins import BasePlugin
# from mkdocs.structure.files import Files

# import logging
# import mkdocs.utils
# log = logging.getLogger(f"mkdocs.plugins.{__name__}")
# log.addFilter(mkdocs.utils.warning_filter)

import logging, re
import mkdocs.plugins

log = logging.getLogger('mkdocs')

# Rewrite using `python-slugify`
def on_files(files, config):
    for f in files:
        if f.is_documentation_page() or f.is_media_file():
            f.abs_dest_path = f.abs_dest_path.replace(" - ", "-").lower()
            f.abs_dest_path = f.abs_dest_path.replace(" ", "-").lower()
            f.abs_dest_path = f.abs_dest_path.replace("(", "").lower()
            f.abs_dest_path = f.abs_dest_path.replace(")", "").lower()
            f.dest_path = f.dest_path.replace(" - ", "-").lower()
            f.dest_path = f.dest_path.replace(" ", "-").lower()
            f.dest_path = f.dest_path.replace("(", "").lower()
            f.dest_path = f.dest_path.replace(")", "").lower()
            f.url = f.dest_path.replace("%20", "-").lower()

    return files