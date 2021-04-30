import discord
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument

Token = ''

bot = commands.Bot(command_prefix='!!')

@bot.command(name="hey")
async def hello(ctx):
    await ctx.send('Hello {}'.format(ctx.author.mention))

@bot.command(name="Embedd")
async def embedMe(ctx):
    message = discord.Embed(title="This is embed!", color=0x00ff00)
    message.add_field(name="This is the name!",value="Hello World!", inline=False)
    message.add_field(name='\u200b', value="Look, no subheader here.")
    message.add_field(name="Inline is true", value="hello")

    await ctx.send(embed=message)

@bot.command(name='stats')
async def stats(ctx):
    message = discord.Embed(title="{}'s Stats:".format(ctx.author), color=0x00ff00)
    message.add_field(name='Current Server:', value=ctx.guild, inline=False)
    message.add_field(name="Current Channel:", value=ctx.channel, inline=False)
    message.set_image(url=ctx.author.avatar_url)
    message.set_footer(text=ctx.author.joined_at)

    await ctx.send(embed=message)


@bot.command(name='markup')
async def marked(ctx, words):
    await ctx.send("```py\n{}\n```".format(words))

@marked.error
async def disney(ctx, error):
    if isinstance(error, MissingRequiredArgument):
        await ctx.send("Hey! Missing Arguments!")

bot.run(Token)
