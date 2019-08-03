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
    @commands.group(autohelp=True)
    async def hentai(self):
        """All the hentai i can give you."""
        pass

    @hentai.command(name="feet")
    async def feet(self, ctx):
        """Feet pictures."""
        await ctx.send(embed=build_embed(nekos.img("feet"), await ctx.embed_color()))

    @hentai.command(name="yuri")
    async def yuri(self, ctx):
        """Yuri pictures."""
        await ctx.send(embed=build_embed(nekos.img("yuri"), await ctx.embed_color()))

    @hentai.commandname(name="trap")
    async def trap(self, ctx):
        """trap pictures."""
        await ctx.send(embed=build_embed(nekos.img("trap"), await ctx.embed_color()))

def setup(bot):
    bot.add_cog(Hentai(bot))