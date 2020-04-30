import requests
import json
from config import webhook
from reader import companies

if __name__ == '__main__':

    data = {
        'text': 'Количество вакансий по ключевому слову Data за последнюю неделю - {}'.format(companies),
        'username': 'sergiishevchenko017@gmail.com',
        'icon_emoji': ':robot_face:'
    }

    response = requests.post(webhook, data=json.dumps(data), headers={'Content-Type': 'application/json'})
