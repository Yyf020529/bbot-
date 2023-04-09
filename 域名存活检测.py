import requests
from concurrent.futures import ThreadPoolExecutor

def check_url_thread(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"{url} is alive.")
            return url
        else:
            print(f"{url} is not alive, status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"{url} is not alive, error: {e}")

def main_thread(urls):
    with ThreadPoolExecutor() as executor:
        alive_urls = list(filter(None, executor.map(check_url_thread, urls)))
    return alive_urls

# 从文件中读取URL
with open('result.txt', 'r', encoding='utf-8') as file:
    urls = [line.strip() for line in file.readlines()]

# 检查URL是否存活
alive_urls = main_thread(urls)

# 将存活的URL保存到alive_urls.txt文件中
with open('alive_urls.txt', 'w', encoding='utf-8') as file:
    for url in alive_urls:
        file.write(url + '\n')
