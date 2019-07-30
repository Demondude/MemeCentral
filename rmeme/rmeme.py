import discord
from redbot.core import commands
import urllib.request, json

class rmeme(commands.Cog):

    @commands.command()
    async def rmeme(self, ctx):
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
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(rmeme(bot))