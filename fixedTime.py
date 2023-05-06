from time import gmtime, strftime


def formattedCurrentTime():
    currentTime = gmtime()
    formattedTime = strftime("%Y-%m-%d", currentTime)
    return formattedTime
