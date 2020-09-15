import argparse
import datetime
import os

import discord

import utils


async def get_guild_messages(guild, args):
    """Gets all messages from a guild and writes to txt"""
    async def get_channel_messages(channel):
        """get messages from a channel and writes to guildname/channelname.txt"""
        messages = []
        start = datetime.datetime.now()
        print(f"getting messages from {channel.name}...")
        async for message in channel.history(limit=None, oldest_first=True):
            message_content = f"{message.author.display_name}: {message.clean_content}"
            if args.timestamp:
                message_content = f"{utils.ftime(message.created_at)} {message_content}"
            messages.append(message_content)
        print(
            f"Done getting {len(messages)} messages in {(datetime.datetime.now() - start).total_seconds()} seconds")

        # write messages to file
        with open(f"{message_dir}/{channel.name}.txt", mode="w") as message_file:
            message_file.write("\n".join(messages))

    # make folder for messages
    message_dir = os.path.join(os.getcwd(), guild.name)
    try:
        os.mkdir(message_dir)
    except FileExistsError:
        if not args.overwrite:
            print(f"skipping {guild.name}")
            return

    for channel in guild.text_channels:
        if not args.prompt_channel or utils.bool_input(f"Get messages from channel {channel.name}?"):
            try:
                await get_channel_messages(channel)
            except discord.errors.Forbidden:
                print(f"Missing permissions for {channel.name}, skipping")
                continue

# setup
args = utils.parse_args()
token = utils.load_token(args.token_file, args.token)
client = discord.Client()

@client.event
async def on_ready():
    """loads messages"""
    print("connected")
    for guild in client.guilds:
        if args.get_all or utils.bool_input(f"Get messages from server {guild.name}?"):
            await get_guild_messages(guild, args)
    print("done")
    await client.close()


client.run(token)
