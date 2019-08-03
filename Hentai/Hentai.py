import discord
import nekos
from redbot.core import commands

def build_embed(url, color):
    embed = discord.Embed(
        color=color
    )
    embed.set_image(url=url)
    embed.set_footer(text="Thanks Nekos-life!")

class Hentai(commands.Cog):
    @commands.group()
    async def hentai(self):
        pass

    @hentai.command()
    async def feet(self, ctx):
        await ctx.send(embed=build_embed(nekos.img("feet"), await ctx.embed_color()))

    @hentai.command()
    async def yuri(self, ctx):
        await ctx.send(embed=build_embed(nekos.img("yuri"), await ctx.embed_color()))

    @hentai.command()
    async def trap(self, ctx):
        await ctx.send(embed=build_embed(nekos.img("trap"), await ctx.embed_color()))

def setup(bot):
    bot.add_cog(Hentai(bot))