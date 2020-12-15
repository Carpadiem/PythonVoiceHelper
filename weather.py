import urllib.request

# city = ''
#
# def ret_weather(city_translated):
#     city = str("https://yandex.ru/pogoda/" + city_translated)
#     return city


city = ''


def main_site():
    global fp
    fp = urllib.request.urlopen(city)
    global mybytes
    mybytes = fp.read()

    global mystr
    mystr = mybytes.decode("utf8")
    fp.close()


def temp_online():
    main_site()
    temp_index = '"temp__value">'
    temp = mystr[(mystr.find(temp_index) + 14):(mystr.find(temp_index) + 14) + 3]
    print("Температура: ", temp)


# temp_online()


def weather_online():
    main_site()
    weather_index = '/><div class="link__feelings fact__feelings"><div class="link__condition day-anchor i-bem" data-bem=\'{"day-anchor":{"anchor":'
    weather = (mystr[(mystr.find(weather_index) + 131):((mystr.find(weather_index) + 131) + 30)])
    weather = weather[:(weather.find("<"))]
    print(weather)


# weather_online()
