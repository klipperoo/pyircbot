import re
import requests


def unquote(url):
    return re.compile('%([0-9a-fA-F]{2})', re.M).sub(lambda m: chr(int(m.group(1), 16)), url)


def rmUnwanted(string):
    string = string.replace("\n", " ")
    string = string.replace("<b>", "")
    string = string.replace("</b", "")

    return string


def lookup(search):
    search = search.replace(" ", "+")

    url = "https://ajax.googleapis.com/ajax/services/search/web?v=1.0&q="
    url += search

    headers = {'Referer': 'xdesg.net'}

    rJson = requests.get(url, headers=headers).json()[
        'responseData']['results']

    searchResults = []

    for result in rJson:
        searchResults.append({'url': unquote(result['unescapedUrl']),
                              'title': rmUnwanted(result['title'])})

    return searchResults


def google(cmdArg):
    commandname = 'google'
    commands = ["!google", ".google", "@google"]
    output = []
    notfound = "No info found :3"

    s_term = ' '.join(cmdArg[1:])
    print s_term

    s_lookup = lookup(s_term)[0]['url']

    if not s_lookup:
        output.append("[\x033Google\x03]: Top google result for \"\x033%s\x03\": %s" % (
                s_term, s_lookup))
    else:
        output.append(notfound)

    return output



