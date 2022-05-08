import discord

color = 0xFF6500
key_features = {
    'temp' : 'Temperature',
    'feels_like' : 'Feels Like',
    'temp_min' : 'Minimum Temperature',
    'temp_max' : 'Maximum Temperature'
}

#to delete unwanted data when getting output message``
def parseData(data):
    data = data['main']
    del data['humidity']
    del data['pressure']
    return data

def weatherMessage(data, location):
    location = location.title()
    if data['temp'] > 10.0:
        message = discord.Embed(title=f'{location} Weather',description= f'Here is the weather for {location}.', color = color)

        message.add_field(name = key_features['temp'], value =  'The temperature is ' + str(round(data['temp'],0)) + '. Good weather to go outside')
        return message
    else:
        message = discord.Embed(title=f'{location} Weather',description= f'Here is the weather for {location}.', color = color)

        message.add_field(name = key_features['temp'], value = 'The temperature is ' + str(round(data['temp'], 0)) + '. Kinda cold maybe do some inside activities')
        return message


def errorMessage(location):
    location = location.title()
    return discord.Embed(
        title='Error',
        description=f'There was an error retrieving weather data for {location}.',
        color=color
    )
        
