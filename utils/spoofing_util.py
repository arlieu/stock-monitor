from fake_useragent import UserAgent


def get_users():
    user_agent = UserAgent()
    return [user_agent.random for i in range(20)]


def set_headers(*args):
    """
    As more headers are added to the headers list, the structure of this container will look as follows:
    [
        [{"User-Agent": <USER-AGENT-1>}, ..., {"User-Agent": <USER-AGENT-20>}],
        [{"Referer": <REFERER-1>}, ..., {"Referer": <REFERER-20>}],
        [{}, ..., {}],
    ]
    StockCrawler will get the list of header options and select and mix one header from each nested list randomly into
    each request.
    """
    headers = []
    agent_header = False
    for arg in args:

        if arg == "user-agent".lower():
            agent_header = True

    if agent_header:
        user_agents = get_users()

        for agent in user_agents:
            headers.append({"User-Agent": agent})

    return headers

    # Add headers to spoof in the same pattern as above
