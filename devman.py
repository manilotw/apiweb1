import requests
params= {
    'lang':'ru'
}
def weather(place,lang='ru'):
    url_template = f'https://wttr.in/{place}'
    response = requests.get(url_template,params=params)
    
    return(response.text)

print(weather('svo'))


