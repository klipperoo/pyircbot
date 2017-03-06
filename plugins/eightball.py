import random


def eightball(cmdArg):


    cmdName = "8ball"
    trgrlist = ["!8ball", "@8ball", ".8ball"]

    basicResponseList = ["It is certain", "It is decidedly so", "Without a doubt",
                    "Yes definitely", "You may rely on it", "As I see it, yes",
                    "Most Likely", "Outlook good", "Yes", "Signs point to yes",
                    "Reply hazy try again", "Ask again later", "Better not tell you now",
                    "Cannot predict now", "Concentrate and try again", "Don't count on it",
                    "My reply is no", "My Sources say no", "Outlook not so good", "Very Doubtful"]

    chanceResponseList = ["Shut up retard", "Get fucked lmao", "Fucking Idiot", "Kill yourself btw  "]
    output = []
    quote = " ".join(cmdArg[1:])

    if random.randint(0, 100) < 30:
        # len(chanceResponselist)/len(basicResponseList)  * 15
        # Actual percentage we are using
        response = basicResponseList + chanceResponseList

        output.append("The magic 8 ball says in response to \"\x033%s\x03\": \x033%s\x03 " %
                      (quote, response[random.randint(0, len(response)-1)]))

    else:
        output.append("The magic 8 ball says in response to \"\x033%s\x03\": \x033%s\x03 " %
                        (quote, basicResponseList[random.randint(0, len(basicResponseList))-1]))

    return output
