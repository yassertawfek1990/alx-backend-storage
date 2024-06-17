#!/usr/bin/env python3
"""S dfv df"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """ds fs"""
    return mongo_collection.insert_one(kwargs).inserted_id
