"""
This module handles "/start" command for telegram bot.

Module requirements:
- telegram
- permissions
- user
- translation
"""

import logging
from telegram import Message
from telegram.ext import CommandHandler

from ..users import User
from ..permissions import *
from ..translation import Translation
from ..telegram import command, add_handler

logger = logging.getLogger()

@command('start', [], h='Initial command.')
async def start(message: Message, params: dict) -> None:
    await message.chat.send_message(Translation("Welcome to our bot for cramming chess! To see all the available commands execute /help.").translate(message.from_user.language_code))

    # print(User.searchById(message.from_user.id))
    if User.searchById(message.from_user.id).id == 0:
        logger.info(f'Making new user entry for {message.from_user.id}')
        user = User()
        user.id = message.from_user.id
        user.nickname = message.from_user.full_name
        user.pgroup = 1000

        user.insert_database_entry()

add_handler(CommandHandler(['start'], start))


def command_start_init():
    SUPERADMIN.addRule('CommandInteraction:start', True)
    ADMIN     .addRule('CommandInteraction:start', True)
    DEFAULT   .addRule('CommandInteraction:start', True)
    RESTRICTED.addRule('CommandInteraction:start', True)
    BANNED    .addRule('CommandInteraction:start', True)
