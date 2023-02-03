import requests

headers = {
    'Content-Type': 'application/json',
    'X-API-TOKEN': 'hZQ9nUGCh0kA9CcD5a8MKQO10cw5LUWFAqTW',
}

json_data = {
    'from': 'lowly-rail',
    'to': '5592985989263',
    'contents': [
        {
            'type': 'text',
            'text': 'text',
        },
    ],
}

response = requests.post('https://api.zenvia.com/v2/channels/sms/messages', headers=headers, json=json_data)

if response.status_code == 200:
    print("SMS enviado com sucesso!")
else:
    print("Ocorreu um erro ao enviar o SMS.")
