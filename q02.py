import requests
from requests.exceptions import RequestException

def download_urls(urls):
    results = {}
    for url in urls:
        attempt = 0
        success = False
        while attempt < 3 and not success:
            try:
                response = requests.get(url)
                response.raise_for_status()
                success = True
            except RequestException as e:
                attempt += 1
        if success:
            results[url] = response.text
        else:
            results[url] = None
    return results

urls = ["https://google.com","https://amazon.in","https://example.com"]
res = download_urls(urls)

for url in res:
    if res[url]:
        print(url,"Successfully Downloaded.")
    else:
        print(url,"Error: No Content")