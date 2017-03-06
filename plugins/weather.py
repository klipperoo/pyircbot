import requests

def getweather(area):
    area = area.strip()
    area = area.replace(" ", "+")
    area = str(area)
    # TODO find out for what reason canadian zipcodes do not work
    apikey = "386257d13f97374f"
    areaQuery = requests.get(
        "http://autocomplete.wunderground.com/aq?query=%s" % area).json()

    searchData = areaQuery['RESULTS'][0]['l']  # Returns the first result

    jsonData = requests.get(
        "http://api.wunderground.com/api/%s/conditions/%s.json" % (apikey, searchData)).json()

    return jsonData

def weather(cmdArg):
    commandname = 'weather'
    output = []
    trgrlist = ["!weather","@weather", ".weather"]
    notfound = "No info found :3"


    if len(cmdArg) >= 2:
        area = "".join(cmdArg[1:])

        try:
            wData = getweather(area)
            city = wData['current_observation']['display_location']['full']
            cWeather = wData['current_observation']['weather']
            temperature = wData['current_observation']['temperature_string']
            rHumidity = wData['current_observation']['relative_humidity']
            output.append("%s [\x033weather:\x03 %s][\x033temperature:\x03 %s]"
                          "[\x033relative humidity\x03: %s]" % (
                city, cWeather, temperature, rHumidity))

        except:
            output.append(notfound)

    else:
        output.append("Enter zip/City")


    return output