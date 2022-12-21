import asyncio
import time

import discord
from discord.ext import commands

from creds import token

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
new_year_at = 1672520401


@bot.event
async def on_ready():
    channel = bot.get_channel(887949127357452309)
    message = await channel.fetch_message(926791899619131463)

    while True:
        await asyncio.sleep(5)
        now = time.time()
        if new_year_at < now:
            await message.edit(content="**С Новым годом!!! 🥧 🎆 🌠**")
        else:
            left = new_year_at - now
            days, hours, minutes, seconds = _get_left_time(left)
            await message.edit(
                content=(
                    "**До 2023 года осталось {} {} {} {}!**".format(
                        _get_verb(days, "день", "дня", "дней"),
                        _get_verb(hours, "час", "часа", "часов"),
                        _get_verb(minutes, "минута", "минуты", "минут"),
                        _get_verb(seconds, "секунда", "секунды", "секунд"),
                    )
                )
            )


def _get_verb(value, v1, v2, v3):
    if value == 1:
        return f"1 {v1}"
    elif 1 < value % 10 < 5 and value not in (11, 12, 13, 14):
        return f"{value} {v2}"
    else:
        return f"{value} {v3}"


def _get_left_time(left):
    days, seconds = divmod(left, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return int(days), int(hours), int(minutes), int(seconds)


bot.run(token)
