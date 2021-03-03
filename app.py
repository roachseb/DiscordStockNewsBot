import discord
from discord.ext import commands


from Library.Bot.events import Events
from Library.Bot.command import Commands



client = commands.Bot(command_prefix= '*')

events = Events(client)

commands = Commands(client)

client.run('ODE0NDczNDU0Mzg0NDQ3NTM5.YDeXgw.msaY5V_cSF4m3KY2WV0c1FZWQCw')