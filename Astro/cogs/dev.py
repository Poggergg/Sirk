from multiprocessing.connection import Client
import discord
from discord import Embed
from discord.ext import commands
from discord.ext.commands import bot
from discord.shard import ShardInfo
from discord.user import User
from discord.utils import get
from datetime import datetime
import os
import collections
import time, datetime
from disputils import BotEmbedPaginator, BotConfirmation, BotMultipleChoice

class dev(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command()
    async def leaveguild(self, ctx):
        '''Leave the current server.'''
        embed=discord.Embed(title='Goodbye', color=0x7289DA)
        await ctx.send(embed=embed)
        await ctx.guild.leave()
    
    @commands.is_owner()
    @commands.command()
    async def status(self, ctx, type, *, status=None):
        '''Change the Bot Status'''
        if type == "playing":
            await self.bot.change_presence(activity=discord.Game(name=f"{status}"))
            await ctx.send(f'<:online:758139458767290421> Changed status to `Playing {status}`')
        elif type == "listening":
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{status}"))
            await ctx.send(f'<:online:758139458767290421> Changed status to `Listening to {status}`')
        elif type == "watching":
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{status}"))
            await ctx.send(f'<:online:758139458767290421> Changed status to `Watching {status}`')
        elif type == "bot":
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name=f"{len(self.bot.users)} users"))
            await ctx.send(f'<:online:758139458767290421> Changed status to `Watching {len(self.bot.users)} users`')
        else:
            await ctx.send("Type needs to be either `playing|listening|watching|bot`")

    @commands.is_owner()
    @commands.command()
    async def dm(self , ctx, user : discord.Member, *, content):
        '''Dm a Member'''
        embed = discord.Embed(color=0x7289DA)
        embed.set_author(name=f"Sent from {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="Message:", value=f'{content}')
        embed.set_footer(text="To reply type 'astro contact <message>'")
        await user.send(embed=embed)
        await ctx.send(f"<:check:758363543002808371> Message sent to {user}")
   
    @commands.is_owner()
    @commands.command()
    async def say(self, ctx, *, content):
        await ctx.send(content)
        
def setup(bot):
    bot.add_cog(dev(bot))