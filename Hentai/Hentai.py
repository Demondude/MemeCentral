import discord
import nekos
from redbot.core import commands


class Hentai(commands.Cog):

    @commands.command(autohelp=True, usage="<Hentai tag>")
    async def hentai(self, ctx, tag: str):
        """
        All the hentai i can give you. Check the list at 'hentailist'.
        """
        if ctx.channel.is_nsfw():
            try:
                url = nekos.img(tag)
            except nekos.errors.InvalidArgument:
                await ctx.send("That tag does not exist. try typing .hentai")
                pass

            embed = discord.Embed(
                color=await ctx.embed_color()
            )
            embed.set_image(url=url)
            embed.set_footer(text="Thanks Nekos-life!")
            await ctx.send(embed=embed)
        else:
            ctx.send("Wrong channel. Go to nsfw")

    @commands.command()
    async def hentailist(self,ctx):
        """Lists all the hentai tags"""
        await ctx.send("Full list here:")
        await ctx.send("""```feet, yuri, trap, futanari, hololewd, lewdkemo,
solog, feetg, cum, erokemo, les, wallpaper, lewdk,
ngif, meow, tickle, lewd, feed, gecg, eroyuri, eron,
cum_jpg, bj, nsfw_neko_gif, solo, kemonomimi, nsfw_avatar,
gasm, poke, anal, slap, hentai, avatar, erofeet, holo,
keta, blowjob, pussy, tits, holoero, lizard, pussy_jpg,
pwankg, classic, kuni, waifu, pat, kiss, femdom,
neko, spank, cuddle, erok, fox_girl, boobs, random_hentai_gif,
smallboobs, hug, ero```""")


def setup(bot):
    bot.add_cog(Hentai(bot))