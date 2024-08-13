#!/usr/bin/env python3

"""
This python function returns all students sorted
by average score.
"""


def top_students(mongo_collection):
    """Return students sorted by averge score."""
    letTheSortingBegin = [
        {
            "$project": {
                "name": 1,
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ]

    return list(mongo_collection.aggregate(letTheSortingBegin))
