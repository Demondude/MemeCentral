import discord
from discord.ext import commands
import urllib.request, json

class rmeme:

    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rmeme(self):
        """This does stuff!"""
        with urllib.request.urlopen("https://meme-api.herokuapp.com/gimme") as url:
            data = json.loads(url.read().decode())
            title = data["title"]
            url = data["url"]
            sub_reddit = data["subreddit"]
            post_link = data["postLink"]

        embed = discord.Embed(
            title=title,
            description="from: " + sub_reddit + " subreddit",
            colour=discord.Color.blue()
        )
        embed.set_image(url=url)
        embed.set_footer(text=post_link)
        await self.bot.say(embed)


def setup(bot):
    bot.add_cog(rmeme(bot))