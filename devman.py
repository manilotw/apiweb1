import requests

def get_weather(place, lang='ru'):
    url_template = f'https://wttr.in/{place}'
    params = {
        'lang': lang,
        'm': '', 
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

def main(place):
    
    weather = get_weather(place)
    if weather:
        print(weather)

if __name__ == '__main__':
    main('svo')
    main('cherepovets')
    main('london')
