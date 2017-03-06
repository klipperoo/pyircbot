from datetime import date


def dtc(cmdArg):
    commandname = 'dtc'
    commands = [".dtc", "@dtc", "!dtc"]
    output = []
    today = date.today()
    christmas = date(today.year, 12, 25)

    if christmas < today:
        christmas = christmas.replace(year=today.year + 1)

    tUntilChristmas = abs(christmas - today)

    output.append("%i days until Christmas!" % tUntilChristmas.days)

    return output


