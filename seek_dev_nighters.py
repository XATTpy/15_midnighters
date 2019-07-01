from pytz import timezone
import requests
from datetime import datetime, time


def load_attempts():
    url = 'https://devman.org/api/challenges/solution_attempts/'
    page = 1
    while True:
        payload = {'page': page}
        request = requests.get(url, params=payload).json()
        for record in request['records']:
            username = record['username']
            timestamp = record['timestamp']
            timezone = record['timezone']
            yield username, timestamp, timezone
        number_of_pages = request['number_of_pages']
        page += 1
        if page == number_of_pages:
            break


def get_midnighters(records):
    midnighters = []
    for record in records:
        username, timestamp, tz = record
        record_time = datetime.fromtimestamp(timestamp, timezone(tz))
        if record_time.hour in range(7) and not username in midnighters:
            midnighters.append(username)
    return midnighters
        

if __name__ == '__main__':
    records = load_attempts()
    midnighters = get_midnighters(records)
    print('These users were noticed in what they study Python at night:')
    for midnighter in midnighters:
        print(midnighter)
