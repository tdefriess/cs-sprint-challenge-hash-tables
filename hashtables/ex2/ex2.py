#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    route = []
    sources = {}
    #build dict
    for ticket in tickets:
        sources[ticket.source] = ticket.destination

    # find starting point
    for source in sources:
        if sources[source] == "NONE":
            route.append(sources["NONE"])

    while len(route) < length:
        route.append(sources[route[len(route) - 1]])
    
    return route
