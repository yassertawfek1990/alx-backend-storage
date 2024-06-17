#!/usr/bin/env python3
"""acd d"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_logs = client.logs.nginx
    d = nginx_logs.count_documents({})
    g = nginx_logs.count_documents({'method': 'GET'})
    p = nginx_logs.count_documents({'method': 'POST'})
    pu = nginx_logs.count_documents({'method': 'PUT'})
    pa = nginx_logs.count_documents({'method': 'PATCH'})
    d = nginx_logs.count_documents({'method': 'DELETE'})
    gs = nginx_logs.count_documents({'method': 'GET',
                                             'path': '/status'})
    print("{} logs".format(d))
    print("Methods:")
    print("\tmethod GET: {}".format(g))
    print("\tmethod POST: {}".format(p))
    print("\tmethod PUT: {}".format(pu))
    print("\tmethod PATCH: {}".format(pa))
    print("\tmethod DELETE: {}".format(d))
    print("{} status check".format(gs))
