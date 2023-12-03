import requests
from datetime import datetime, timedelta

def get_API_holidays():
    url = 'https://www.gov.uk/bank-holidays.json'
    response = requests.get(url)
    all_holidays = response.json()
    return all_holidays["england-and-wales"]["events"]

holidays = get_API_holidays()

for event in holidays:
    print("Title:", event["title"])
    print("Date:", event["date"])
    print("Notes:", event["notes"])
    print("---------")
