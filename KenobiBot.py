import TwitterAPI
import YoutubeAPI
import discord
import logging
from discord.ext import commands
import time
import os

token = 'ODEzMzI3NzcyMTUxODQwODE4.YDNsgw.0qXEQZFYUnSsHW4M4vdYONEg2jE'

twitterID = [
    612473, #BBC News
    16343974, #The Telegraph
    7587032, #Sky News
    87818409, #Guardian
    16973333, #Indepedent
]

youtubeID = [
    'UC16niRr50-MSBwiO3YDb3RA', #BBC News
    'UCPgLNge0xqQHWM5B5EFH9Cg', #The Telegraph
    'UCoMdktPbSTixAyNGwb-UYkQ', #Sky News
    'UCIRYBXDze5krPDzAEOxFGVA', #Guardian
    'UCshwRhftzkiov5wKR7M_LsQ', #Indepedent
    'UC6bVUQukuALUH4qXC2HhWMA', #Myself, for testing purposes
]

def sillyLogStuff():
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

sillyLogStuff()
client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def here(ctx):
    TwitterAPI.getTwitter(twitterID) #initialize our list
    YoutubeAPI.getYoutube(youtubeID) #initialize our list
    while(True):
        tweets = TwitterAPI.getTwitter(twitterID)
        for tweet in tweets:
            await ctx.send('https://twitter.com/user/status/{ID}'.format(ID = tweet))
        videos = YoutubeAPI.getYoutube(youtubeID)
        for video in videos:
            await ctx.send('https://www.youtube.com/watch?v={ID}'.format(ID = video))
        print(time.asctime(time.localtime()) + ": \n" + str(tweets) + '\n' + str(videos))
        time.sleep(30)

client.run(token)
