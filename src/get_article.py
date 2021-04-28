import requests
import json
import re
from bs4 import BeautifulSoup

config_file = './data/config/config.ini'
# one week test data
dataset_01 = './data/one_week/20170101.json'
id2url_file = './data/user_infos/id2url.json'
id2content_file = './data/user_infos/id2content.json'

test_local_html = "url.html"

def gen_id2url():
    table = []
    data = {}
    f1 = open(dataset_01, 'r', encoding='utf-8')
    for line in f1:
        table.append(json.loads(line))
        #print(json.loads(line))
    f1.close()

    f2 = open(id2url_file, 'a+', encoding='utf-8')
    for row in table:
        print(row['eventId'])
        #print(row['url'])
        data['eventId'] = row['eventId']
        data['url'] = row['url']
        json_str = json.dumps(data)
        f2.write(json_str + '\n')
        print()
    f2.close


def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 20)
        r.raise_for_status()
        #r.encoding = 'utf-8'
        return r.content
    except requests.exceptions.RequestException as e:
        print(e)
        return None

def removePunctuation(content):
    """
    文本去标点
    """
    punctuation = r"~!@#$%^&*()_+`{}|\[\]\:\";\-\\\='<>?,./，。、《》？；：‘“{【】}|、！@#￥%……&*（）——+=-"
    content = re.sub(r'[{}]+'.format(punctuation), '', content)

    if content.startswith(' ') or content.endswith(' '):
        re.sub(r"^(\s+)|(\s+)$", "", content)

    return content.strip().lower()

def getContent(html, eventId):
    content = ''
    data = {
        'eventId' : eventId,
        'title' : '',
        'content' : ''}
    if not html:
        return data
    soup = BeautifulSoup(html, "html.parser")
    #soup = BeautifulSoup(open(test_local_html, encoding='utf-8'), features='html.parser')
    title = soup.select("h1.title > span.t100")
    if not title:
        return data

    paras = soup.select("div.body > p")
    if not paras:
        return data

    for para in paras:
        if len(para) > 0:
            content += para.get_text()
    #去除标点
    title_str = removePunctuation(title[0].get_text())
    content = removePunctuation(content)
    #将爬取到的文章用字典格式来存
    data['title'] = title_str
    data['content'] = content
    print(data)
    return data

def gen_id2content():
    table = []
    f1 = open(id2url_file, 'r', encoding='utf-8')
    for line in f1:
        table.append(json.loads(line))
        #print(json.loads(line))
    f1.close()

    f2 = open(id2content_file, 'a+', encoding='utf-8')
    for row in table:
        if row['url'] == 'http://adressa.no':
            print('Skip:' + row['url'])
            continue
        html = getHTMLText(row['url'])
        print('Connect:' + row['url'])
        data = getContent(html, row['eventId'])
        json_str = json.dumps(data, ensure_ascii=False)
        print(json_str)
        f2.write(json_str + '\n')
    f2.close

def main():
    #url = "http://news.qq.com/a/20170504/012032.htm"
    #url = "https://www.adressa.no/nyheter/2016/12/31/Se-lesernes-nytt%C3%A5rsbilder-14000400.ece"
    #gen_id2url()
    gen_id2content()
main()
