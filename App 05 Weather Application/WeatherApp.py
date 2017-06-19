import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport', 'loc, cond, temp, scale')


def main():
    # print the header
    print_the_header()

    # get the zipcode form the user
    user_name = input("May I have your name please: ")
    code = input("Good morning {}, What is the zipcode you want the weather for?".format(user_name))
    print("{} you have requested the weather information for zipcode - {}".format(user_name, code))

    # get_the_userzipcode()
    # get the HTML from Web
    html = get_html_from_web(code)
    # parse the HTML from Web
    report = get_weather_from_html(html)
    # display the forecast
    print("The Weather forecast {} for {} is {} {} with {} conditions".format(
        user_name,
        report.loc,
        report.temp,
        report.scale,
        report.cond))


def print_the_header():
    print("-----------------------------------")
    print("          THE WEATHER APP          ")
    print("-----------------------------------")
    print()


# def get_the_userzipcode():
# user_name = input("May I have your name please: ")
# userzipcode = input("Good morning {}, What is the zipcode you want the weather for?".format(user_name))
# print("{} you have requested the weather information for zipcode - {}".format(user_name, userzipcode))
# print()


def get_html_from_web(zipcode):
    url = "http://www.wunderground.com/weather-forecast/{}".format(zipcode)
    response = requests.get(url)
    print(response.status_code)
    # print(response.text[0:250])
    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, "html.parser")
    # CityCSS = '#location h1'
    # WeatherConditionCSS = '#curCond .wx-value'
    # WeatherTemperatureCSS = '#curTemp .wx-value'
    # WeatherUnitCSS = '#curTemp .wx-unit'
    loc = soup.find(id="location").find('h1').get_text()
    condition = soup.find(id="curCond").find(class_="wx-value").get_text()
    temp = soup.find(id="curTemp").find(class_="wx-value").get_text()
    scale = soup.find(id="curTemp").find(class_="wx-unit").get_text()

    loc = cleanup_text(loc)
    loc = find_city_and_state_from_location(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)
    # return loc, condition, temp, scale
    report = WeatherReport(cond=condition, loc=loc, temp=temp, scale=scale)
    return report


def find_city_and_state_from_location(loc: str):
    parts = loc.split("\n")
    return parts[0].strip()


def cleanup_text(text):
    if not text:
        return text

    text = text.strip()
    return text

if __name__ == "__main__":
    main()
