#!/usr/bin/env python3
"""Updates the topics of a school document"""

def update_topics(mongo_collection, name, topics):
    """Update all topics of a school based on name"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
