import pytz
import requests


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
    pass

if __name__ == '__main__':
    gen = load_attempts()
    for i in gen:
        print(i)
