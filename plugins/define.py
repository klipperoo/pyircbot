from wordnik import *
from helper import secrets

def dictdefine(word):
    replacedword = word.strip()
    apiUrl = 'http://api.wordnik.com/v4'
    apiKey = secrets.WORDNIKAPIKEY
    client = swagger.ApiClient(apiKey, apiUrl)

    wordApi = WordApi.WordApi(client)
    dictdefined = wordApi.getDefinitions(replacedword)

    return dictdefined


def define(cmdArg):
    commandname = 'define'
    commands = ["!define", "@define", ".define"]
    output = []
    notfound = "No info found :3"


    word = " ".join(cmdArg[1:])

    dcontents = dictdefine(word)

    if dcontents != None:
        output.append("[\x033Definition\x03]: '\x033%s\x03' %s" % (word,dcontents[0].text))

    else:
        output = [notfound]

    return output
