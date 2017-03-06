import requests


def udLookup(word, word_number=0):
    url = "http://api.urbandictionary.com/v0/define?term="

    if word == "":
        return None
    else:
        results = requests.get(url + word)

    json_data = results.json()

    if word_number > len(json_data['list']) or len(json_data['list']) == 0:
        return None
    else:
        pass

    # Should we pass this data as a json object?
    return json_data['list'][word_number]


def ud(cmdArg):
    commandname = 'ud'
    commands = ["!ud", "@ud", ".ud"]
    output = []
    notfound = "No info found :3"
    #print "length of cmdArg: %s " % len(cmdArg)
    

    if cmdArg[-1].startswith('#'):
        word = ''.join(cmdArg[1:-1])

        try:
            word_num = int(cmdArg[-1][1:])
            definition = udLookup(word,word_num)
        except:
            definition = udLookup(word)

    else:
        word = ' '.join(cmdArg[1:])

        definition = udLookup(word)

    if definition != None:

        output.append("[\x033UD\x03]: '\x033%s\x03' %s" %
                          (definition['word'], definition['definition']))
        output.append("[\x033Example\x03]: %s" % definition['example'])

    else:
        output.append(notfound)

    return output