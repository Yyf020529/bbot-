import re

def extract_urls(text):
    url_pattern = re.compile(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    )
    urls = re.findall(url_pattern, text)
    return urls

# 从文件中读取文本
with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 提取URL
urls = extract_urls(text)

# 将URL结果保存到result.txt文件中
with open('result.txt', 'w', encoding='utf-8') as file:
    for url in urls:
        file.write(url + '\n')
