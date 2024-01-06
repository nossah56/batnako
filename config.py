import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 22575862))

    API_HASH = os.environ.get("API_HASH", "41c5a46067f37f8c2f350f0c244fdf7d")
