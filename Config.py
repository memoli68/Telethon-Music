import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6121315800:AAE62EMYvTfUTRJ0p69pUQS74sevWvjFk-k)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BJWap1wBu8FU1iiDaNgH6fh7azwT7EegVuRQViLwh0Xbsuucb5sthYtXOlyFNvmRquntVEFlfvwEq6ByE9wmm4UZZoDp7Vqj07h_APr7AHXDSV2Ne_PjqesDZT21FDudhlKMcfbJAOLPy5UDXvSdBT9Vj-xU9L5lLiG65vjEOMjuSyBwSPoEz7D5szN5TH5O4CkuT-5B8R8KtZXS5B8NmYEBcgoD0qmJsgBVGjNepXkTXDN-BgpeBs14Z9zEWz03HdRHIk_HzG9B8fJ-DNg5pjgQSQfGS13XyI7eL-EmSFgUuSitFEUZM8XF1tPf5cXxMLxeP47rYlBLUkbWjsA1YRvsbRu07rY=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
