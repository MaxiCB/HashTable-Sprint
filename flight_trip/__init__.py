#  Hint:  You may not need all of these.  Remove the unused functions.
from typing import List
from hashtable import HashTable


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets: List[Ticket], length: int):
    cache = {}
    for i in tickets:
        cache[i.source] = i.destination

    route = []
    for key, value in cache.items():
        if key == "NONE":
            route.append(value)

    complete = False
    while not complete:
        previous_stop = route[-1]

        if previous_stop in cache.keys():
            route.append(cache[previous_stop])

        if previous_stop == "NONE":
            complete = True

    return route[:length]
