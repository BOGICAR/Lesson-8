import requests
import argparse
import json
import datetime
import time


def request():
    get_info = requests.get('https://api.exchangerate.host/convert',
                            params={'from': args.currency_from,
                                    'to': args.currency_to,
                                    'amount': args.amount,
                                    'date': args.start_date})
    print(get_info)


def request_1():
    get_info = requests.get('https://api.exchangerate.host/convert',
                            params={'from': 'USD',
                                    'to': 'UAH',
                                    'amount': '100',
                                    'date': '2021-07-20'})
    return get_info.json()


def read_symbols():
    with open('symbols.json', 'r') as file:
        file_symbols = json.load(file)
        symbols = file_symbols['symbols']
    return symbols


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Online currency converter')
    parser.add_argument('currency_from', type=str)
    parser.add_argument('currency_to', type=str)
    parser.add_argument('amount', type=float)
    parser.add_argument('-sd', '--start_date', type=str)
    args = parser.parse_args()
    if args.currency_from not in read_symbols():
        print('Enter the correct currency')
    if args.currency_to not in read_symbols():
        print('Enter the correct currency')


def main():
    x = request_1()
    list_main = []
    date_now = datetime.datetime.now()
    args.start_date = datetime.datetime.strptime(args.start_date, '%Y-%m-%d')
    if date_now < args.start_date:
        args.start_date = date_now
    list_title = ['date', 'from', 'to', 'amount', 'rate', 'result']
    list_main.append(list_title)
    while args.start_date < date_now:
        list_info = [x['date'], x['query']['from'], x['query']['to'],
                     x['query']['amount'], x['info']['rate'], x['result']]
        args.start_date += datetime.timedelta(days=1)
        list_main.append(list_info)
        time.sleep(0.1)
    return list_main


print(main())
