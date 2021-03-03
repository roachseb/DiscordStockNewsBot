import discord
import pandas
from discord.ext.commands import Bot, Context
from datetime import datetime

import finnhub
import json



class Commands_Finnhub(): 
    #creates all the wanted events
    def __init__(self,client:Bot):
        self.finnhub_client = finnhub.Client(api_key="c0t7gbn48v6r4maem16g")


        @client.command(pass_context=True)
        async def BasicFinancial(ctx:Context, ticker:str, metric:str):
            # Basic financials
            await ctx.send(pandas.DataFrame(self.finnhub_client.company_basic_financials(ticker,metric)) )


        @client.command(pass_context=True)
        async def CompanyNews(ctx:Context, ticker:str, from_:str,to_:str):
            # Company News
            await ctx.send( self.finnhub_client.company_news(ticker,from_,to_)) 

        @client.command(pass_context=True)
        async def StockCandles(ctx:Context, ticker:str,resolution:str,_from:str,_to:str):
            
            await ctx.send( pandas.DataFrame(self.finnhub_client.stock_candles(ticker,resolution,_from,_to) )) 

        @client.command(pass_context=True)
        async def Pattern(ctx:Context, ticker:str,resolution:str):
            data = self.finnhub_client.pattern_recognition(ticker,resolution)
            for point in data["points"]:
                for key in point:
                    if "time" in key or "Time" in key or "date" in key:
                        point[key] = str(datetime.fromtimestamp(point[key]))
                await ctx.send( json.dumps(point,indent=4) ) 


        @client.command(pass_context=True)
        async def NewSentiment(ctx:Context, ticker:str):
            await ctx.send( json.dumps(self.finnhub_client.news_sentiment(ticker),indent=4)) 

        @client.command(pass_context=True)
        async def PriceTarget(ctx:Context, ticker:str):
            await ctx.send( pandas.DataFrame(self.finnhub_client.price_target(ticker) )) 

        @client.command(pass_context=True)
        async def AggInd(ctx:Context, ticker:str,resolution:str):
            await ctx.send( json.dumps(self.finnhub_client.aggregate_indicator(ticker,resolution),indent=4))


        @client.command(pass_context=True)
        async def Quote(ctx:Context, ticker:str):
            #c : current price
            #h : high price
            #l : low price
            #o : open price
            #pc : previous close
            #t : time-date
            res = {}
            renamekey = {"c":"current price","h":"high price","l":"low price","o":"open price","pc":"previous close","t":"time-date",}
            data:dict= self.finnhub_client.quote(ticker)

            for key in data:
                print(key)
                res[renamekey[key]] = data[key]
                

            await ctx.send(res)

