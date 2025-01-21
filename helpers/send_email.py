import os
import requests

def send_email(recipients: list[str], body: str):
    print("Sending email...")
    data = {"key": "value"}
    response = requests.post(
        "https://api.mailgun.net/v3/sandboxe862b47970c4422c9df346a71cd63087.mailgun.org/messages",
        auth=("api", os.getenv("MAILGUN_API_KEY")),
        data={
            "from": "Wishbliss A.I. News Reporter <mailgun@sandboxe862b47970c4422c9df346a71cd63087.mailgun.org>",
            "to": recipients,
            "subject": "Hello",
            "html": body,
        })
    print(response)
