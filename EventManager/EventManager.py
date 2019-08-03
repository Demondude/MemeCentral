import discord
from redbot.core import commands


class EventManager(commands.Cog):

    @commands.command(pass_context=True)
    async def event(self, ctx):

        def user_check(msg):
            return msg.author == ctx.author

        await ctx.send("Enter a quick description of the event.")
        description_event = await ctx.bot.wait_for("message", check=user_check)
        await ctx.send(description_event.content)


def setup(bot):
    bot.add_cog(EventManager(bot))