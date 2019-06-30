import pytz
import requests
from datetime import datetime


def load_attempts():
    query = 'https://devman.org/api/challenges/solution_attempts/'
    pages = requests.get(query).json()['number_of_pages']
    for page in range(1, pages+1):
        payload = {'page': page}
        records = requests.get(query, params=payload).json()['records']
        for record in records:
            username = record['username']
            timestamp = record['timestamp']
            timezone = record['timezone']
            yield username, timestamp, timezone


def get_midnighters():
    midnighters = []
    for record in load_attempts():
        username, timestamp, timezone = record
        record_time = (pytz.timezone(timezone)).localize(datetime.fromtimestamp(timestamp))
        if record_time.hour in range(7) and not username in midnighters:
            midnighters.append(username)
    return midnighters
        

if __name__ == '__main__':
    midnighters = get_midnighters()
    print("These users were noticed in what they study Python at night:")
    for midnighter in midnighters:
        print(midnighter)
