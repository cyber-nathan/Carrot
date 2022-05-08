from bs4 import SoupStrainer
import discord, random, datetime, asyncio, requests
# from discord.ext.commands import Bot, has_permissions
from discord.ext import commands
from weather import*
import json


channel_name = 'general'

# for weather api
apiKey = "d61d4956b6f09f9f02e1ccdaeb7d0d1e"

# bot token: To serve the bot locally, enter the Discord Bot Token below.
TOKEN = ''



# database for facts, quotes, etc.
fitness_facts = ['The human body has 650 muscles','The only exercise you should hold your breath for is underwater swimming', 'The heart is the strongest muscle in the body','Nearly 50% of all young people ages 12-21 are not vigorously active on a daily basis.', 'Working out can improve the look of your skin!', 'Working out can improve your performance in bed.', 'Excercise can help your bowel movements.', 'Regular excercise can help reduce symptoms of anxiety.'  ]
mental_health_quotes = ['You don’t have to control your thoughts. You just have to stop letting them control you.','Take your time healing, as long as you want. Nobody else knows what you’ve been through. How could they know how long it will take to heal you?', 'One small crack does not mean that you are broken, it means that you were put to the test and you didn’t fall apart.', 'The bravest thing I ever did was continuing my life when I wanted to die.', 'If you can’t fly, run. If you can’t run, walk. If you can’t walk, crawl, but by all means, keep moving.', 'Tough times never last, but tough people do!', 'If there is no struggle, there is no progress.', 'You don’t have to control your thoughts. You just have to stop letting them control you.']
positive_affirmations = ['Challenges help me grow', 'I am enough', 'I deserve to be happy', 'I am proud of myself', 'I believe in myself', 'I am confident in my abilities', 'I can do anything I put my mind to', 'No matter how hard it is, I can do it", "I have the power to make my dreams come true', 'I am going to take control of my happiness', 'Happiness comes from within me", "I am thankful for today', 'Everyday is a fresh start', 'I can. I will. End of story.']
fitness_vid = ['https://www.youtube.com/watch?v=fcN37TxBE_s', 'https://youtu.be/8aXwejFPDTw', 'https://youtu.be/M0uO8X3_tEA']
daily_challenges = ['Pushups', 'Jumping Jacks', 'Triceps Dips', 'Squats', 'Sit-ups', 'Lunges', 'Burpes', 'Bicycle Crunch', 'Toe Taps', 'Glute Bridge', 'Leg Lift', 'Superman']
fit_gif = ['https://tenor.com/view/sexy-girl-sexy-girl-gym-beautiful-gif-15431867', 'https://tenor.com/view/spongebob-squarepants-chest-bust-rip-shirt-buff-gif-13924759', 'https://tenor.com/view/work-out-excercise-spongebob-crossfit-zumba-gif-13093532', 'https://tenor.com/view/workout-treadmill-hard-work-fitness-gym-buddy-gif-17076804', 'https://tenor.com/view/workout-gym-funny-exercise-gif-12757833', 'https://tenor.com/view/curls-gym-work-out-stewie-griffin-weights-gif-14965303', 'https://tenor.com/view/gif-gif-5012174', 'https://tenor.com/view/gym-fail-leg-day-fat-treadmill-lazy-gif-16136370', 'https://tenor.com/view/fail-work-out-gif-10437039', 'https://tenor.com/view/dog-exercise-gym-animal-pet-gif-18568414', 'https://tenor.com/view/ballet-flexible-gym-buddies-lifting-feet-random-clips-gif-14002287'] 


command_prefix = '!'
weather_command = 'w.'
client = commands.Bot(command_prefix = command_prefix)




# comes online
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await daily_fitness_fact()
    await daily_quote()
    await positive_affirmation()
    await daily_fitness_video()
    await daily_challenge()
    await daily_poll()
    

# weather
@client.event
async def on_message(message):
    if message.author != client.user and message.content.startswith(weather_command):
        location = message.content.replace(weather_command, '').lower()
        if len(location) >=1:
            url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={apiKey}&units=metric'
            data = requests.get(url).content

            try:
                data = json.loads(requests.get(url).content)
                data = parseData(data)
                await message.channel.send(embed=weatherMessage(data, location))
            except KeyError:
                await message.channel.send(embed=errorMessage(location))
    await client.process_commands(message)


#easter eggs
@client.command(pass_context=True)
async def gym(ctx):
    await ctx.send(fit_gif[random.randint(0, len(fit_gif) - 1)])
@client.command(pass_context=True)
async def monk(ctx):
    await ctx.send(f'<:monkey:972333038421823518>')
@client.command(pass_context=True)
async def fire(ctx):
    await ctx.send(f'<:fire:972331474986631178>')
@client.command(pass_context=True)
async def water(ctx):
    await ctx.send(f'<:droplet:972559908383891456>')
@client.command(pass_context=True)
async def earth(ctx):
    await ctx.send(f'<:earth_americas:972562245592678451>')
@client.command(pass_context=True)
async def air(ctx):
    await ctx.send(f'<:cloud_tornado:972562512157499463>')


#daily fitness quotes
async def daily_fitness_fact():
    now = datetime.datetime.now()
    then = now+datetime.timedelta(days = 1) 
    then.replace(hour = 8, minute = 0)
    wait_time = (then-now).total_seconds()
    await asyncio.sleep(wait_time)

    channel = client.get_channel(972298031527518210)

    await channel.send('<:muscle:972325161992859688> ' + 'Daily Fitness Fact: ' + fitness_facts[random.randint(0, len(fitness_facts) - 1)] + ' <:muscle:972325161992859688>')

#mental health quotes
async def daily_quote():
    now = datetime.datetime.now()
    then = now+datetime.timedelta(days = 1) 
    then.replace(hour = 9, minute = 0)
    wait_time = (then-now).total_seconds()
    await asyncio.sleep(wait_time)

    channel = client.get_channel(972298031527518210)

    await channel.send('<:books:972330104686518312> ' + 'Daily Quote: ' + mental_health_quotes[random.randint(0, len(mental_health_quotes) - 1)] + ' <:books:972330104686518312>')    
    
#motivational reminders
async def positive_affirmation():
    now = datetime.datetime.now()
    then = now+datetime.timedelta(days = 1) 
    then.replace(hour = 10, minute = 0)
    wait_time = (then-now).total_seconds()
    await asyncio.sleep(wait_time)

    channel = client.get_channel(972298031527518210)

    await channel.send('<:cherry_blossom:972332732908716082> ' + 'Daily Positive Affirmation: ' + positive_affirmations[random.randint(0, len(positive_affirmations) - 1)] + ' <:cherry_blossom:972332732908716082>')    
    

#daily fitness video   
async def daily_fitness_video():
    now = datetime.datetime.now()
    then = now+datetime.timedelta(days = 1) 
    then.replace(hour = 18, minute = 00)
    wait_time = (then-now).total_seconds()
    await asyncio.sleep(wait_time)

    channel = client.get_channel(972298031527518210)

    await channel.send('<:cinema:972332249267703848> ' + 'Daily Fitness video: ' + fitness_vid[random.randint(0, len(fitness_vid) - 1)] + ' <:cinema:972332249267703848>')

#daily challenge
async def daily_challenge():
    now = datetime.datetime.now()
    then = now+datetime.timedelta(days = 1) 
    then.replace(hour = 11, minute = 0)
    wait_time = (then-now).total_seconds()
    await asyncio.sleep(wait_time)

    channel = client.get_channel(972298031527518210)

    await channel.send('<:woman_lifting_weights:972332461235273769> ' + 'Daily challenge: ' + str(random.randint(10, 50)) + ' ' + daily_challenges[random.randint(0, len(daily_challenges) - 1)] + ' <:man_lifting_weights:972332623932305408>')



# poll command
@client.command(pass_context=True)
async def poll(ctx, *, message):
    emb = discord.Embed(title = ' POLL ', description = f'{message}')
    msg = await ctx.channel.send(embed = emb)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎') 

# daily poll  
async def daily_poll():
    now = datetime.datetime.now()
    then = now+datetime.timedelta(days = 1) 
    then.replace(hour = 9, minute = 0)
    wait_time = (then-now).total_seconds()
    await asyncio.sleep(wait_time)

    channel = client.get_channel(972298031527518210)

    emb = discord.Embed(title = ':rotating_light:' + 'DAILY POLL ' + ':rotating_light:', description = f'How are you TODAY?')
    msg = await channel.send(embed = emb)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')




#goal list
todo = []

@client.command()
async def goals(ctx):   
    embed=discord.Embed(title='Server Goals',
    color=0xFF5733)
    if len(todo) != 0:
        for i in range(len(todo)):
            embed.add_field(name = '..................................', value = str(i+1) + '. ' + todo[i], inline = False )
         
        await ctx.send(embed=embed)
    else:
         embed.add_field(name = '..................................', value = "No goals in goal list" )
         await ctx.send(embed=embed)


@client.command()
async def addgoal(ctx, *args):
    message = ''
    for words in args:
        message += words+' '
    await ctx.channel.send(message + 'has been added to goals')
    todo.append(message)

@client.command()
async def removegoal(ctx, *args):
    message = ''
    for words in args:
        message += words+ ' '
    await ctx.channel.send('Goal number ' + message + 'has been removed from goals ')
    print(message)
    todo.pop(int(message)-1)
    

  


# Mental Health Resources/Hotlines
@client.command()
async def resources(ctx, user:discord.Member, *, message = None):
    message = 'Mental Health Resources and Hotlines'
    warningMessage = '*Call 911 or go to your nearest hospital or emergency department if you are in an emergency, immediate danger, or medical distress.*'
    embed = discord.Embed(title = message, description = warningMessage, color=discord.Color.purple())
    embed.add_field(name = 'Canada Suicide Prevention Service(24/7):', value = 'Call: 1-833-456-4566 ', inline = False)
    embed.add_field(name = 'Kids Help Phone ', value = 'Call: 1-800-668-6868 ', inline = False)
    embed.add_field(name = "Crisis Text Line", value = "[Website](https://www.crisistextline.org/) OR Text HOME to 741741 to connect with a Crisis Counselor" , inline = False)
    embed.add_field(name = 'Anonymously Vent', value = "[website](https://muttr.com/)", inline = False)
    embed.add_field(name = 'Tips To Boost Mental Health', value = '[Website](https://www.mhanational.org/31-tips-boost-your-mental-health)')
    await user.send(embed = embed)



#command for ping
@client.command(pass_context=True)
async def ping(ctx):
    await ctx.send(f'🏓Pong! {round(client.latency * 1000)}ms')


 

client.run(TOKEN)