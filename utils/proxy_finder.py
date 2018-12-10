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
    raw_proxy_list = json.loads(response)
    retry_count = 0
    for proxy in raw_proxy_list["data"]:

        if validate_proxy(proxy):
            proxy_list += proxy["ipPort"]
        else:
            retry_count += 1

    retry_proxies = []
    if retry_count:
        retry_proxies = find_proxies(retry_count)

    return proxy_list + retry_proxies


def validate_proxy(proxy):
    url = "https://www.google.com/"
    proxies = {"http": proxy}
    status_code = requests.get(url, proxies=proxies).status_code
    if status_code < 200 or status_code > 299:
        return False

    return True


if __name__ == "__main__":
    proxy_list = find_proxies()
    count = 0
    for proxy in proxy_list:
        if not validate_proxy(proxy):
            count += 1
            print("PROXY %d NOT WORKING" % count)

    print("ALL PROXIES VALID")
