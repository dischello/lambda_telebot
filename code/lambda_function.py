import requests

def lambda_handler(event, context):

    data=event
    print(data.json())
    send_message(data["message"]["from"]["id"], data["message"]["text"])

def send_message(chat_id, text):
    url = "https://api.telegram.org/bot{token}/{method}".format(
        token="563678020:AAGPx21beePzxBqRFQAnQqEb0gA_LURyfho",
        method="sendMessage"
    )
    data = {
        "chat_id": chat_id,
        "text": text
    }
    r = requests.post(url, data = data)
    print(r.json())

def start_request():
    url = "https://api.telegram.org/bot{token}/{method}".format(
        token="563678020:AAGPx21beePzxBqRFQAnQqEb0gA_LURyfho",
        method="setWebhook"
    )
    data = {
        "url":"https://gob02sosh2.execute-api.eu-central-1.amazonaws.com/Prod/telebot"
    }
    r = requests.post(url, data = data)
    print(r.json())

if __name__ == "__main__":
    start_request()
