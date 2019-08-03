import discord
from redbot.core import commands
from redbot.core.bot import Red


class EventManager(commands.Cog):

    def __init__(self, bot: Red):
        self.bot = bot

    @commands.command(pass_context=True)
    async def event(self, ctx):
        await ctx.send("Enter name of the event.")
        name_event = self.bot.wait_for_message(author=ctx.message.author, timeout=30)
        await ctx.send("Enter a quick description of the event.")
        description_event = self.bot.wait_for_message(author=ctx.message.author, timeout=30)
        await ctx.send("Enter the date of the event example (yyyy/mm/dd).")
        date_event = self.bot.wait_for_message(author=ctx.message.author, timeout=30)
        await ctx.send("Enter the time of the event example (00:00). The time should be Coordinated Universal Time (UTC).")
        time_event = self.bot.wait_for_message(author=ctx.message.author, timeout=30)

        embed = discord.Embed(title=name_event, description=description_event, color=0xf2ff00)
        embed.add_field(name="Time", value=time_event, inline = True)
        embed.add_field(name="Date", value=date_event, inline = True)
        embed.set_footer(text="You should get a notification when the event starts.")
        await ctx.send(embed=embed)

        await ctx.send("It looks like this. Should we post this ? (y/n).")
        confirmation_event = self.bot.wait_for_message(author=ctx.message.author, timeout=30)
        await ctx.send(confirmation_event)





def setup(bot):
    bot.add_cog(EventManager(bot))