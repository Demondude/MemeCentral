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
    @commands.command(autohelp=True, usage="<Hentai tag>")
    async def hentai(self, ctx, tag: str):
        """All the hentai i can give you."""
        if tag == "":
            await ctx.send("""```
                feet, trap, futanari, hololewd, lewdkemo, solog
                feetg, cum, erokemo, les, wallpaper, lewdk
                ngif, meow, tickle, lewd, feed, gecg, eroyuri, eron
                cum_jpg, bj, nsfw_neko_gif, solo, kemonomimi, nsfw_avatar
                gasm, poke, anal, slap, hentai, avatar, erofeet, holo
                keta, blowjob, pussy, tits, holoero, lizard, pussy_jpg
                pwankg, classic, kuni, waifu, pat, kiss, femdom
                neko, spank, cuddle, erok, fox_girl, boobs, random_hentai_gif
                smallboobs, hug, ero```"""
                           )
        else:
            try:
                await ctx.send(embed=build_embed(nekos.img(tag), await ctx.embed_color()))
            except nekos.errors.InvalidArgument:
                await ctx.send("That tag does not exist. try typing .hentai")


def setup(bot):
    bot.add_cog(Hentai(bot))