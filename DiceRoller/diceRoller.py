from random import randint

async def rollDiceVerbose(number_of_dice, size_of_dice):
    outstring = ''
    total_roll = 0
    for x in range(number_of_dice):
        roll = randint(1, size_of_dice)
        outstring = outstring + "\t\tRoll #" + str(x+1) + ": " + str(roll) + "\n"
        total_roll+=roll
    outstring = outstring + "\nTotal Roll: {}".format(total_roll)
    return outstring, total_roll

async def rollDice(number_of_dice, size_of_dice):
    total_roll = 0
    for x in range(number_of_dice):
        roll = randint(1, size_of_dice)
        total_roll+=roll
    outstring = "\nTotal Roll: {}".format(total_roll)

    return outstring, total_roll

