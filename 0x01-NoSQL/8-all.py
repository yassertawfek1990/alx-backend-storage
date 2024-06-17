#!/usr/bin/env python3
"""d f d"""
import pymongo


def list_all(mongo_collection):
    """l d v"""
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
