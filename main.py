import timer3
import python-telegram-bot
import cryptography
import ptbot
import os
from pytimeparse import parse

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_USER_ID = os.getenv("TELEGRAM_USER_ID")


def reply(time):
    secs = parse(time)
    message_id = bot.send_message(TELEGRAM_USER_ID, "Таймер запущен на {} секунд\n{}".format(secs, render_progressbar(secs, 0)))
    bot.create_countdown(secs, notify_progress, mid=message_id, timer=secs)
    bot.create_timer(secs, notify)


def notify_progress(secs_left, mid, timer):
    bot.update_message(TELEGRAM_USER_ID, mid, "Осталось {} секунды\n{}".format(secs_left, render_progressbar(timer, timer - secs_left)))


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def notify():
    bot.send_message(TELEGRAM_USER_ID, "Время вышло")


bot = ptbot.Bot(TELEGRAM_BOT_TOKEN)
bot.send_message(TELEGRAM_USER_ID, "На сколько запустить таймер?")
bot.wait_for_msg(reply)
