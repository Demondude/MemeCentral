import discord
from redbot.core import commands
from redbot.core.bot import Red


class EventManager(commands.Cog):

    def __init__(self, bot: Red):
        super().__init__()
        self.bot = bot

    @commands.command(pass_context=True)
    async def event(self, ctx):

        def user_check(msg):
            return msg.author == ctx.author

        await ctx.send("Enter a quick description of the event.")
        description_event = await self.bot.wait_for("message", check=user_check)
        await ctx.send(description_event)


def setup(bot):
    bot.add_cog(EventManager(bot))