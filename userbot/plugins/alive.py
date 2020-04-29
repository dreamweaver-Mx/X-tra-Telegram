"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "senza nome"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**🎲 __THEKILLERBOB USERBOT STATUS__ 🎲**\n\n"
                     "🔹Tetethon Version: 7.0.1\n🔹Python Version: 3.8.0\n🔸**SUPPORT & UPDATE: @Thekillerbobbot **\n"
                     "🔸**BOT CREATOR:** [TheKillerBob](tg://user?id=528569326) **\n"
                     "🔹**CPU:** Ok \n\n🎲 **__USER DATA__** 🎲\n"
                     f"🔸 **USER:** __{DEFAULTUSER}__\n"
                     "🔸[Shoppy](https://shoppy.gg/@The_Killer_Bob)")
