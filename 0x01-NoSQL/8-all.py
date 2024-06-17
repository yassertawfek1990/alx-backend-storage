#!/usr/bin/env python3
"""ds s"""
import pymongo


def list_all(mongo_collection):
    """ d s"""
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
