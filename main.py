import discord
import re
from random import randint
from config import *

client = discord.Client()
testmode = False



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    command_match_obj = re.match('^\$roll ([1-9][0-9]{0,4}(d[1-9][0-9]{0,4}|[4-9]))$', message.content)
    verb_command_match_obj = re.match('^\$roll ([1-9][0-9]{0,4}(d[1-9][0-9]{0,4}|[4-9]))( [vV])$', message.content)

    if message.author == client.user:
        return

    if verb_command_match_obj:
        command_list = message.content.split()
        verbose_mode = command_list[2]
        command = command_list[1]
        command = command.split("d")
        dice_number = int(command[0])
        dice_size = int(command[1])
        await rollDiceVerb(dice_number, dice_size, message.channel)
    elif command_match_obj:
        command_list = message.content.split()
        command = command_list[1]
        command = command.split("d")
        dice_number = int(command[0])
        dice_size = int(command[1])
        await rollDice(dice_number, dice_size, message.channel)
    elif message.content.startswith("$roll"):
        await message.channel.send("Command syntax: \'$roll [1-9999]d[4-9999] <vV>\'")
        #if message.content.startswith('$roll'):
            #   dice_command = message.conent.split()[1]

      #  await message.channel.send('hello!')

async def rollDiceVerb(dice_number, dice_size, channel):
    total_roll = 0
    for x in range(dice_number):
        roll = randint(1, dice_size)
        await channel.send("\t\tRoll #" + str(x+1) + ": " + str(roll) + "\n")
        total_roll+=roll

    await channel.send("\nTotal Roll: " + str(total_roll))
    return

async def rollDice(dice_number, dice_size, channel):
    total_roll = 0
    for x in range(dice_number):
        roll = randint(1, dice_size)
        total_roll+=roll

    await channel.send("\nTotal Roll: " + str(total_roll))
    return



client.run(token)
