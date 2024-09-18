import requests


def get_weather(place, lang='ru'):
    url_template = f'https://wttr.in/{place}'
    params = {
        'lang': lang,
        'n': '',
        'q': '',
        'T': '',
        'M': ''
    }
    response = requests.get(url_template, params=params)
    response.raise_for_status()  # Если ошибка, она будет поднята
    return response.text


if __name__ == '__main__':
    cities = ['svo', 'cherepovets', 'london']
    for city in cities:
        try:
            weather = get_weather(city)
            print(weather)
        except requests.exceptions.HTTPError as err:
            print(f"Ошибка при запросе погоды для {city}: {err}")
        except requests.exceptions.RequestException as err:
            print(f"Ошибка при выполнении запроса для {city}: {err}")
