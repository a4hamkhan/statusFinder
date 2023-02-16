import requests
import argparse
import json


def get_status_code(url):
    try:
        response = requests.get(url, timeout=10)
        return response.status_code
    except requests.exceptions.RequestException:
        return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', type=str, help='The URL to check')
    parser.add_argument('--json', action='store_true', help='Output the result in JSON format')
    args = parser.parse_args()

    url = args.url if args.url.startswith('http') else f'http://{args.url}'

    status_code = get_status_code(url)

    if args.json:
        result = {'url': url, 'status_code': status_code}
        print(json.dumps(result))
    else:
        print(f'{url} : {status_code}')
