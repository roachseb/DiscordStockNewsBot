import discord
from discord.ext.commands import Bot, Context
import json



class Functions_Watchlist(): 
    #creates all the wanted events
    def __init__(self):
        self.json_file = "Data/watchlists.json"
    
    def create(self,watchlist:str):
        try:
            data = self.get()
            data[watchlist] = []
            self.save(data)
            return 0
        except Exception:
            return -1

    def add(self,watchlist:str,ticker:str):
        try:
            data = self.get()
            data[watchlist] = data[watchlist] + [ticker]
            self.save(data)
            return 0
        except KeyError as ke:
            raise KeyError
            print("{} was not found as a watchlist".format(watchlist), ke)
        except Exception as e:
            raise Exception
            print(e)
            return -1

    def remove(self,watchlist:str,ticket:str):
        try:
            data = self.get()
            data[watchlist] = data[watchlist] - [ticket]
            self.save(data)
            return 0
        except Exception:
            return -1

    def delete(self,watchlist:str):
        try:
            data = self.get()
            del(data[watchlist])
            self.save(data)
            return 0
        except Exception:
            return -1

    def deleteall(self):
        try:
            self.save({})
            return 0
        except Exception:
            return -1

    def get(self):
        try:
            with open(self.json_file,'r') as f:
                data:dict = json.load(f)
            return data
        except Exception:
            return -1

    def save(self,data:object):
        try:
            with open(self.json_file,'w') as f:
                #dumps data into json
                json.dump(data,f,indent=4,sort_keys=True)
            return 0
        except Exception:
            return -1
        
    def prettyprint(self):
        try:
            return json.dumps(self.get(),indent=4,sort_keys=True)
        except Exception:
            return -1
