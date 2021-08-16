import datetime
import locale


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
        print(now.strftime("%B"))
        
        return answer