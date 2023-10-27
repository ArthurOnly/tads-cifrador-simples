"""
This module is used to override the settings for local development.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# CORS

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = False

# Media

MEDIA_URL = "/storage/"
MEDIA_ROOT = os.path.join(BASE_DIR, "")
