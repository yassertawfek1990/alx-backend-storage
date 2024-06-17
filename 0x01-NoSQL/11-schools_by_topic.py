#!/usr/bin/env python3
"""df fd"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """sd sfc"""
    return mongo_collection.find({"topics": topic})
