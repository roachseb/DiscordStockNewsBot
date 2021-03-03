import discord
from discord.ext.commands import Bot, Context
import json
from.Fwatchlist import Functions_Watchlist

class Command_Watchlist(): 
    #creates all the wanted events
    def __init__(self,client:Bot):
        #import functions
        self.functions = Functions_Watchlist()

        @client.command(pass_context=True)
        async def WatchlistCreate(ctx:Context,watchlist:str):
            self.functions.create(watchlist)
            await ctx.send("Created Watchlist : {}".format(watchlist))
            

        @client.command(pass_context=True)
        async def WatchlistAdd(ctx:Context,watchlist:str,ticker:str):
            ''' Inputs: ctx <discord.Conterxt>
                        watchlist: name of watchlist <str>
                        ticker: ticker of a stock <str>
                Output: None 
                Command that allows the Discord Bot to add a ticker to a watchlist       
            '''
            #Creation of server object for server info
            server:Guild = ctx.guild
            try:
                self.functions.add(watchlist,ticker)
                await ctx.send("Added {} to watchlist {} ".format(ticker,watchlist))
            except KeyError as ke:
                await ctx.send("{} watchlist was not found".format(watchlist))
            

        @client.command(pass_context=True)
        async def WatchlistRemove(ctx:Context,watchlist:str,ticker:str):
            ''' Inputs: ctx <discord.Conterxt>
                        watchlist: name of watchlist <str>
                Output: None 
                Command removes watchlists       
            '''
            try:
                self.functions.remove(watchlist,ticker)
            except KeyError as ke:
                await ctx.send("{} watchlist was not found".format(watchlist))
            
        @client.command(pass_context=True)
        async def WatchlistDelete(ctx:Context,watchlist:str):
            try:
                self.functions.delete(watchlist)
            except KeyError as ke:
                await ctx.send("{} watchlist was not found".format(watchlist))
            

        @client.command(pass_context=True)
        async def WatchlistDeleteAll(ctx:Context):
            ''' Inputs: ctx <discord.Conterxt>
                Output: None 
                Command clears watchlist.json     
            '''
            try:
                self.functions.deleteall()
                ctx.send("Deleted all the watchlists")
            except KeyError as ke:
                await ctx.send("{} watchlist was not found".format(watchlist))
            

        @client.command(pass_context=True)
        async def Watchlists(ctx:Context):
            ''' Inputs: ctx <discord.Conterxt>
                Output: None 
                Command returns the current watchlists info   
            '''
            await ctx.send("{}".format(self.functions.prettyprint()))
            


