#!/usr/bin/env python3

"""
This python function that returns the list
of schools having a specifc topic.
"""


def schools_by_topic(mongo_collection, topic):
    """Return a List of schools with a specific topic."""
    return list(mongo_collection.find({"topics": topic}))
