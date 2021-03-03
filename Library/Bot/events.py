import discord
from discord.ext.commands import Bot, Context, ConversionError



class Events(): 
    #creates all the wanted events
    def __init__(self,client:Bot):

        @client.event
        async def on_ready():
            print("Bot Is Ready")

        @client.event
        async def on_member_join(member):
            print(f"{member} has join a server.")

        @client.event
        async def on_member_remove(member):
            print(f"{member} has left a server.")

        @client.event
        async def on_command_error(ctx:Context ,error:ConversionError):
            await ctx.send(error)
