#!/usr/bin/env python3
'''Tx xz x'''
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    '''P xz x'''
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for x in methods:
        r = len(list(nginx_collection.find({'method': x})))
        print('\tmethod {}: {}'.format(x, r))
    status_checks_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks_count))


def run():
    '''P x x'''
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_request_logs(client.logs.nginx)


if __name__ == '__main__':
    run()
