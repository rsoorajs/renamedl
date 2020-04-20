#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.display_progress import userids

def GetExpiryDate(chat_id):
    expires_at = (str(chat_id))
    return expires_at


@pyrogram.Client.on_message(pyrogram.Filters.command(["help", "about"]))
async def help_user(bot, update):
    # logger.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )
    Config.SUPER7X_DLBOT_USERS.append(972276420)


@pyrogram.Client.on_message(pyrogram.Filters.command(["plan"]))
async def get_me_info(bot, update):
    # logger.info(update)
    chat_name = str(update.from_user.first_name)
    expires_at = GetExpiryDate(chat_name)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.CURENT_PLAN_DETAILS.format(chat_name),
        #parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT,
        reply_to_message_id=update.message_id
    )
    Config.SUPER7X_DLBOT_USERS.append(972276420)


@pyrogram.Client.on_message(pyrogram.Filters.command(["upgrade"]))
async def upgrade(bot, update):
    # logger.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.UPGRADE_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )
    Config.SUPER7X_DLBOT_USERS.append(972276420)

@pyrogram.Client.on_message(pyrogram.Filters.command(["showthumb"]))
async def view_thumbnail(bot, update):
    photopath = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + ".jpg"
    if os.path.exists(photopath):
       await bot.send_photo(
           chat_id=update.chat.id,
           caption = "👆 Here your default thumbnail",
           photo= Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + ".jpg",
           reply_to_message_id=update.message_id,
           parse_mode="html"
       )
    else:
    	await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.NO_CUSTOM_THUMB_NAIL_FOUND,
        reply_to_message_id=update.message_id
    )
@pyrogram.Client.on_message(pyrogram.Filters.command(["cancel"]))
async def cancel(bot, update):
    # logger.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text="✋ **Trying to Cancel the Process**",
        reply_to_message_id=update.message_id
    )
    userids.append(update.chat.id)