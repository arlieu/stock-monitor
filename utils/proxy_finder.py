import requests
import json


def find_proxies(count=1):
    proxy_list = []
    uri = "http://pubproxy.com/api/proxy"
    level = "level=elite"
    speed = "speed=1"
    limit = "limit=%d" % count
    query = "?%s&%s&%s" % (level, speed, limit)

    full_request = uri + query

    response = requests.get(full_request).text
    for proxy in response["data"]:
        proxy_list += proxy["ipPort"]

    return proxy_list


def validate_proxy(proxy):
    url = "https://www.google.com/"
    proxies = {"http": proxy}
    status_code = requests.get(url, proxies=proxies).status_code
    if status_code < 200 or status_code > 299:
        return False

    return True

if __name__ == "__main__":
    proxyList = find_proxies()
    count = 0
    for proxy in proxyList:
        if not validate_proxy(proxy):
            count += 1
            print("PROXY %d NOT WORKING" % count)