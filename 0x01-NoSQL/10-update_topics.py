#!/usr/bin/env python3
"""sd sd"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """d d f"""
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
