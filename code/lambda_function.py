import requests

def lambda_handler(event, context):
    print(event)
    print("Done")
    send_message(event["message"]["from"]["id"], event["message"]["text"])

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
    """
def start_request():
    url = "https://api.telegram.org/bot{token}/{method}".format(
        token="563678020:AAGPx21beePzxBqRFQAnQqEb0gA_LURyfho",
        method="setWebhook"
    )
    data = {
        "url":"https://j3smybyms4.execute-api.eu-central-1.amazonaws.com/Prod/telebot"
    }
    r = requests.post(url, data = data)
    print(r.json())

if __name__ == "__main__":
    start_request()
"""