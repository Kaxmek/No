from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("21574612")
APP_HASH = os.environ.get("eed89ad66a40eab463cf0e0521a19aa7")
BOT_USERNAME = os.environ.get("gghshshhzbot")
session = os.environ.get("1BJWap1wBuz-trCtHuKFqHfJPS5BHhcPuDjv1zNOQIbaHE01u7VYNQ47he5CzQiyrfUowNVZSwb5MFC4Ev6fMqtBv1rN0bAWpsjuZr4kdopFlWKNeFC1tReJeE8BmAluIZarhiAQMwfZo2-CDEhiGwM2k9QyKhHGugM30jbSgC2B-4DGt0itFfrY8trbPMmTiF-5qBiP9W8Hn2oQJsPGdjWgjEYpTMyq_QY0xj6P3QHKYyaya3DgS7MLZhfM8fwrCOtn1iMUedZcZ1EPpDM4i3nJuX2fKSsGcVzxAoI9Nubwm8525HjHTJQJ4kWmboBguqjiwn6MgE0KwoYAu_cZbcZD7hI6Zqxo=")
SESSION = os.environ.get("1BJWap1wBuz-trCtHuKFqHfJPS5BHhcPuDjv1zNOQIbaHE01u7VYNQ47he5CzQiyrfUowNVZSwb5MFC4Ev6fMqtBv1rN0bAWpsjuZr4kdopFlWKNeFC1tReJeE8BmAluIZarhiAQMwfZo2-CDEhiGwM2k9QyKhHGugM30jbSgC2B-4DGt0itFfrY8trbPMmTiF-5qBiP9W8Hn2oQJsPGdjWgjEYpTMyq_QY0xj6P3QHKYyaya3DgS7MLZhfM8fwrCOtn1iMUedZcZ1EPpDM4i3nJuX2fKSsGcVzxAoI9Nubwm8525HjHTJQJ4kWmboBguqjiwn6MgE0KwoYAu_cZbcZD7hI6Zqxo=")
token = os.environ.get("5999125608:AAGeeUQd5oxMWV40i99tCeAdAto9CykPvLo")
fifthon = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()
