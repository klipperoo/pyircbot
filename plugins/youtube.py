from helper.search import youtube_search

def youtube(cmdArg):
    commandname = 'youtube'
    commands = ['.youtube','!youtube','@youtube','.yt','!yt','@yt']
    output = []

    sQuery = " ".join(cmdArg[1:])
    #print sQuery


    yData = youtube_search(sQuery)
    #print yData
    url =  "https://youtu.be/" + yData['id']['videoId']
    v_title = yData['snippet']['title']
    c_title = yData['snippet']['channelTitle']

    output.append("[\x033Youtube\x03] \x033Title\x03: %s \x033Channel\x03: %s \x033Link\x03: %s"
                  % (v_title, c_title, url))

    return output

