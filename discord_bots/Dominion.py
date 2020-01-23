# imports
import discord
from discord.ext import commands
import random
import inspect
import asyncio
import importlib
import math
import datetime
from datetime import time, tzinfo, timedelta



client = discord.Client()
description = '''Hello nerds! There are a number of utility commands being showcased here.'''


bot = commands.Bot(command_prefix='>', description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    #print(bot.user.id)
    print('------')

#global var setup
month = 9
year = 2
monthName = "temp"
realtime = datetime.datetime.now(tz=None)

#when month == 12, increase year by 1 and set month to 0
#this is the time engine, this may have to be made a class soon in order to drive the other 100000 functions and events i require in order to run efficiently and to save my SANITY
@bot.command()
async def time(message):

#global var pull
    global month
    global year
    global realtime

    if realtime.hour == 24:
        month += 1
        return month

    if month == 13:
        month = 1
        year += 1
        return month, year

    if month == 1:
        monthName = "January,"
    elif month == 2:
        monthName = "February,"
    elif month == 3:
        monthName = "March,"
    elif month == 4:
        monthName = "April,"
    elif month == 5:
        monthName = "May,"
    elif month == 6:
        monthName = "June,"
    elif month == 7:
        monthName = "July,"
    elif month == 8:
        monthName = "August,"
    elif month == 9:
        monthName = "September,"
    elif month == 10:
        monthName = "October,"
    elif month == 11:
        monthName = "November,"
    elif month == 12:
        monthName = "December,"
    year_number = str(year)

    it_is_text = "It is "
    year_text = " year "
    af_text = " AF"

    await message.channel.send(it_is_text + monthName + year_text + year_number + af_text)






@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command()
async def rate():
    """Rates things on a scale of 0-10!"""
    YourList = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    result = random.choice(YourList)
    await bot.say(result)

    #@bot.command()
    #async def add(left : int, right : int):
    #    """Adds two numbers together."""
    #    await bot.say(left + right)

#@bot.command()
#async def thoughts():
#    """Gives Dominion's thoughts on a matter."""
#    Opinion = (':ok_hand:', '<:notokay:356482747411333160>', 'Hard pass.',
#               '<:vomit:358447414706831370>', 'Excellent.',
#               "TOO BAD, THIS ISN'T AN EXHIBIT", 'Away with that.', 'Cease.',
#               'You need help... <:help:386336801608040449>',
#               'Where is the merge stick...'
#               )
#    result = random.choice(Opinion)
#    await bot.say(result)

#@bot.command(description='Either or!')
#async def choose(*choices : str):
#    """Chooses between choices. Bot can pick 'or'."""
#    await bot.say(random.choice(choices))

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined. @ the person after >joined"""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

#@bot.group(pass_context=True)
#async def cool(ctx):
#    """Says if a user is cool. Format = put name after command"""
#    if ctx.invoked_subcommand is None:
#        await bot.say('No, {0.subcommand_passed} is a nerd'.format(ctx))

#@cool.command(name='bot')
#async def _bot():
#    """Is the bot cool?"""
#    await bot.say('Yes, the bot is amazing!')

#@bot.command()
#async def colour():
#    """Says Dominion's favorite colour based on his mood."""
#    Colours = ('blue', 'red', 'green', 'purple', 'orange', 'yellow', 'white', 'black', 'brown', 'neon blue', 'electric brown', 'royal purple',
#             'puke green', 'highlighter yellow', 'liquor sign orange', 'Thailand district red', 'two leagues from Barcelona, Spain blue',
#             'watermellon green', 'vomit chunky orange', "Reese's peanut butter brown", 'sandwich', 'pineapple pizza yellow', 'vintage red wine red',
#             'a crusty blood red', 'an ugly designer yellow', 'a designer blue', 'a designer black', 'a designer puke green', 'a designer purple', 'a designer pink',
#             'a designer red', 'a designer green', 'a designer orange', 'a designer white', 'lasagna white', 'undercooked brown', 'popcorn magenta', 'a raw red',
#             'vegan red', 'an overcooked cactus green', 'poopy brown', 'deep fried green', 'deep fried brown', 'deep fried purple', 'deep friend yellow','a disgustingly pink, pink'
#               )
#    Colour = random.choice(Colours)
#    Coloor = ('My favourite colour right now is... ')
#    paste = (Coloor + Colour)
#    await bot.say(paste)

#@bot.command()
#async def menu():
#    """Gives you a randomized selection of food."""
#    adjectives = ('awful', 'burnt', 'well-done', 'excellent', 'over-salted', 'bland',
#                  'spicy', 'undercooked', 'yummy', 'satisfying', 'exciting',
#                  'disgusting', 'deep fried'
#                  )
#    mains = ('steak', 'lamb shank', 'pork loin', 'spinach & ricotta canneloni', 'shit sandwich',
#             'lasagna', 'mediterranean chicken', 'veggie burger',
#             'cheese tortellini', 'chicken pesto pasta', 'wish soup'
#             'chilli', 'ribs', 'lemon pepper tuna')
#    sweets = ('cookie', 'mars bar', 'skittles', 'smokey bacon crisps',
#              'popcorn', 'dried prunes', 'crackers', 'cheese curls',
#              'granola bar', 'pound cake', 'nuts', 'lollipops'
#              )
#    drinks = ('water', 'flavoured water', 'salt water', 'bleach scented soda', 'soda water', 'orangeade', 'cola',
#              'fruit juice', 'cherryade', 'appleade', 'lemonade', 'milkshake',
#              'smoothie', 'hotdog water'
#              )

#    adj = random.choice(adjectives)
#    main = random.choice(mains)
#    sweet = random.choice(sweets)
#    drink = random.choice(drinks)

#    rationsresult = 'Your order contains a unique ' + adj +' '+ main +', '+ sweet +' and '+ drink + '. Top nosh!'

#    await bot.say(rationsresult)



#@bot.command()
#async def repeat(ctx, times: int, content='repeating...'):
#    """You're all terrible people."""
#    for i in range(times):
#        await ctx.send(content)


bot.run('NDY1NjY1MDIwODQwMTE2MjI0.Xid75A.Hdm06ldR_8Qa1sEjk79BicrU4uY')
