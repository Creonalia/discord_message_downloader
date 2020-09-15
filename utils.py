import sys
import argparse


def bool_input(prompt):
    """gets y/n input"""
    while True:
        # validate input
        reply = input(f"{prompt} (y/n) ").lower()
        if not reply:
            print("use y or n")
            continue

        # check for y/n
        if reply[0] == "y" or reply[0] == "t":
            return True
        elif reply[0] == "n" or reply[0] == "f":
            return False
        else:
            print("use y or n")


def ftime(time_):
    """formats a datetime"""
    return time_.strftime("%m/%d/%y %H:%M")


def parse_args():
    """"""
    parser = argparse.ArgumentParser(
        description="Downloads messages from discord servers")
    parser.add_argument(
        "-t", "--token", default=None, dest="token", metavar="T",
        help="Sets the discord token",
    )
    parser.add_argument(
        "-f", "--token-file", default="token.txt", dest="token_file", metavar="F",
        help="Sets the file to load/write discord token from (defaults to token.txt)",
    )
    parser.add_argument(
        "-s", "--timestamp", action="store_true", dest="timestamp",
        help="Add timestamps to messages",
    )
    parser.add_argument(
        "-o", "--no-overwrite", action="store_false", dest="overwrite",
        help="Prevents overwriting files (per server, not per channel)",
    )
    parser.add_argument(
        "-a", "--get-all", action="store_true", dest="get_all",
        help="get all messages (prompts per server by default)",
    )
    parser.add_argument(
        "-c", "--prompt-channel", action="store_true", dest="prompt_channel",
        help="Prompts whether to get messages per channel (gets from all channels by default)",
    )

    return parser.parse_args()


def load_token(token_filename="token.txt", new_token=None):
    """writes token to token_filename if given and returns token from token_filename"""
    if new_token:
        with open(token_filename, "w") as token_file:
            token_file.write(new_token)
    try:
        with open(token_filename, "r") as token_file:
            return token_file.read()
    except FileNotFoundError:
        print("No discord token found, use -t to set the token")
        sys.exit()
