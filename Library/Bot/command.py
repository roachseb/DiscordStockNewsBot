import discord
from discord.ext.commands import Bot, Context
import json

from .commands.watchlist.Cwatchlist import Command_Watchlist
from .commands.finnhub.Cfinnhub import Commands_Finnhub


class Commands(): 
    #creates all the wanted events
    def __init__(self,client:Bot):
        self.client = client
        Command_Watchlist(self.client)
        Commands_Finnhub(self.client)

        @client.command()
        async def byeRango(ctx:Context, reason=None):
            rango = await client.fetch_user(216847469542244352)
            await ctx.guild.ban(rango)
            await ctx.send("Don't mess with Seb again")

        @client.command()
        async def okRango(ctx:Context, reason=None):
            rango = await client.fetch_user(216847469542244352)
            guild: discord.Guild = await ctx.guild
            guild.unban(216847469542244352)
            await ctx.send("Don't mess with Seb again")

        @client.command()
        async def M(ctx:Context):
            await ctx.send(f'Rango muted for you, enjoy your peace')



