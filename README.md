# discord_message_downloader

Downloads messages from discord servers.

## Setup

Dependencies: [discord.py](https://github.com/Rapptz/discord.py)
Requires a [discord bot token](https://discordpy.readthedocs.io/en/latest/discord.html) and the read_message_history permission. The token is stored in token.txt and can be set using -t

## Usage

This may run slowly since it takes a while to get the messages (95-100 messages/sec for a few thousand messages+)
```bash
# sets token to discordtokenhere, saves it to discord_token.txt, and starts downloding messages
$ python3 discord_message_downloader -t discordtokenhere -f discord_token.txt

# gets all messages with timestamps and without prompting
$ python3 discord_message_downloader -ta
```

```bash
optional arguments:
  -h, --help            show this help message and exits
  -t T, --token T       Sets the discord token
  -f F, --token-file F  Sets the file to load/write discord token from (defaults to token.txt)
  -s, --timestamp       Add timestamps to messages
  -o, --no-overwrite    Prevents overwriting files (per server, not per channel)
  -a, --get-all         get all messages (prompts per server by default)
  -c, --prompt-channel  Prompts whether to get messages per channel (gets from all channels by default)
```

Messages are saved to server_name/channel_name.txt in the format sender: message (time sender: message if using -s)
