import discord
import json
from discord.ext import commands
import re

client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print("Bot is ready")


# Search for the Key in the Message and Replace it with the Value
@client.event
async def on_message(message):
    str = "unchanged"
    if message.author == client.user:
        return
    ctx = await client.get_context(message)
    if message.content.startswith("!add"):
        # get the Ctx of the Message
        await add(ctx)
        return
    if message.content.startswith("!remove"):
        await remove(ctx)
        return
    with open("data.json", "r") as f:
        config = json.load(f)
    # check that the data contin any key

    for key, value in config.items():
        if re.search(key, message.content):
            str = "changed"
            # change the Values of the Message
            message.content = re.sub(key, value, message.content)
    if str == "changed":
        await ctx.send(message.content)
        await message.delete()
        return


# remove the Key from the Json File
@client.command()
async def remove(ctx):
    await ctx.send("What is the Key? That you want to Remove")
    key = await client.wait_for("message", check=lambda m: m.author == ctx.author)
    key = key.content
    with open("data.json", "r") as f:
        data = json.load(f)
    if key in data:
        del data[key]
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
        await ctx.send("Removed {}".format(key))
    else:
        await ctx.send("{} not found".format(key))


async def add(ctx):
    await ctx.send("What is the Key?")
    key = await client.wait_for("message", check=lambda m: m.author == ctx.author)
    key = key.content
    # ask the Value to add
    await ctx.send("What is the Value?")
    value = await client.wait_for("message", check=lambda m: m.author == ctx.author)
    value = value.content
    with open("data.json", "r") as f:
        data = json.load(f)
    data[key] = value
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
    await ctx.send("Added {}".format(key))


client.run("OTQxMzgzNjY0MDYxODA0NjI0.YgVJ2w.9lIQmcYUlrSLycW5hV7tTVSeHMc")
