import requests

def getWeather(key):
    ##getting latitude and longitude from a phone is unfeasible, however, let's pretend I did that
    lat=40
    lon=80
    #get weather
    weatherReport=requests.get("https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={key}") #oof it wants money for this
    #format weather report
    print(weatherReport.json())
    try:
        hourlyWeather=weatherReport[hourly[weather[main]]]
    except KeyError:
        print("The necessary key does not exist")
        sys.exit()
    weatherReport="In an hour, it will be " + hourlyWeather
    return weatherReport

def main(key):
    weatherReport=getWeather(key)
    #send to phone
    requests.post('https://ntfy.sh/xweatgery', weatherReport)

if __name__ == "__main__":
    main(key)




