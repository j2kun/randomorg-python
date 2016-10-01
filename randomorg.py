import requests

url = 'https://www.random.org/cgi-bin/randbyte/?nbytes=16384&format=f'


def get_random_bytes():
    response = requests.get(url)
    if 'You have used your quota' in response.text or response.status_code != 200:
        raise Exception('Done!')

    random_bytes = response.content
    with open('random.bin', 'ab') as outfile:
        outfile.write(random_bytes)

while True:
    get_random_bytes()
