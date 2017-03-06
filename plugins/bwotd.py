from define import dictdefine
from ud import udLookup

definition = None
word = ""
def bwotd(cmdArg):
    commandname = 'bwotd'
    commands = ["!bwotd", ".bwotd", "@bwotd"]
    output = []
    global definition
    global word

    #bwotd set word ud/def
    #bwotd
    if len(cmdArg) == 4 and cmdArg[1] == 'set':
        word = cmdArg[2]

        if cmdArg[3] == "ud":
            data = udLookup(word)
            definition = data['definition']
            output.append(word+" set as bwotd.")

        elif cmdArg[3] == "def":
            data = dictdefine(word)
            definition = data[0].text
            output.append(word+ " set as bwotd.")
        else:
            output.append("Enter either ud or def.")
    elif definition != None:
        output.append("[\x033bwotd\x03] \x033%s\x03 : %s" % (word,definition))

    else:
        output.append("Set bwotd like \"bwotd set word ud/def\"")

    return output









