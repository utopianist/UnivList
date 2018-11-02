import bs4
import requests
from bs4 import BeautifulSoup

def getHTML(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parseHTML(html, ulist):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            ulist.append([tr('td')[0].string, tr('td')[1].string, tr('td')[3].string])

def printUlist(ulist, num):
    tplp = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplp.format("排名", "学校", "评分", chr(12288)))#采用中文字符的空格填充chr(12288)
    for i in range(num):
        u = ulist[i]
        print(tplp.format(u[0], u[1], u[2], chr(12288)))


def main():
    ulist = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTML(url)
    parseHTML(html, ulist)
    printUlist(ulist, 20)

main()
