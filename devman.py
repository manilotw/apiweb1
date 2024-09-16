import requests

def get_weather(place, lang='ru'):
    url_template = f'https://wttr.in/{place}'
    params = {
        'lang': lang,
        'n': '',  
        'q': '' ,  
        'T': '' ,
        'M': ''
    }
    
    try:
        response = requests.get(url_template, params=params)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"Ошибка при запросе погоды для {place}: {err}")
        return None
    
    return response.text


cities = ['svo', 'cherepovets', 'london']

if __name__ == '__main__':
    for city in cities:
        print(get_weather(city))
