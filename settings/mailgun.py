import requests

def send_email(api_key, domain, from_email, to_email, subject, message):
    return requests.post(
        f"https://api.mailgun.net/v3/{domain}/messages",
        auth=("api", api_key),
        data={"from": from_email,
              "to": to_email,
              "subject": subject,
              "text": message})
