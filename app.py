import discord
from discord.ext import commands


from Library.Bot.events import Events
from Library.Bot.command import Commands
from Library.ConfigLoader.configloader import Configs


conf = Configs()
client = commands.Bot(command_prefix= conf.BOT_COMMAND_PREFIX)
events = Events(client)
commands = Commands(client)
client.run(conf.BOT_TOKEN)