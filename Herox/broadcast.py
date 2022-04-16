import os
from pyrogram import filters, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from . import bot 
from Herox.broadcast import STARTED, FINISH, ERROR
fron config import SUDO_USERS



STARTED = 'Black Magic Begins...'
FINISH = 'done, {} users were removed from group'
ERROR = 'something Went Wrong Please Try Again.\n\n**{}** !'


@bot.on_message(filters.group & filters.command("randi"))
def main(_, msg: Message):
    chat = msg.chat
    me = chat.get_member(bot.get_me().id)
    if chat.get_member(msg.from_user.id).can_manage_chat and me.can_restrict_members and me.can_delete_messages:
        try:
            msg.reply(STARTED.format(chat.members_count))
            count_kicks = 0
            for member in chat.iter_members():
                if not member.can_manage_chat:
                    bot.ban_chat_member(chat_id=msg.chat.id, user_id=member.user.id)
                    count_kicks += 1
            msg.reply(FINISH.format(count_kicks))
        except Exception as e:
            msg.reply(ERROR.format(str(e)))
    else:
        msg.reply("i need to be admin In This Group To Perform This Action!")
