import datetime
import locale
from os import name
import requests, json

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

class SystemInfo:

    def __init__():
        pass


    @staticmethod    
    def get_time():

        now = datetime.datetime.now()
        answer = 'São {} horas e {} minutos.'.format(now.hour, now.minute)
        
        return answer


    @staticmethod
    def get_date():

        try:
            locale.setlocale(locale.LC_ALL, 'pt_BR')
        except:
            locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil')
        now = datetime.datetime.now()
        answer = 'Hoje é dia {} de {} de {}'.format(now.day, now.strftime("%B"), now.year)
        
        return answer

    @staticmethod
    def get_weather(city):   

        URL = BASE_URL + "q=" + city + "&appid=" + "cdcb436b563e29634f88faf531a90905" 
        response = requests.get(URL)

        if response.status_code == 200:
            data = response.json()
            main = data['main']

            temperature = main['temp']
            aux = float(temperature) -  273.15
            temperature2 = "{:.0f}".format(aux)

            humidity = main['humidity']
            pressure = main['pressure']
            report = data['weather']

            answer= 'Está fazendo {} graus em {}'.format(temperature2, city)
            return answer

        else:

            return " Não consegui encontrar essa cidade"
            

