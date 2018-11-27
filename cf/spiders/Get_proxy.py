from lxml import etree
from lxml.etree import HTMLParser
import requests
proxy = [

]
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
}
page = requests.get('http://www.xicidaili.com/nn/1', headers=head)
# print(page.text)
tree = etree.HTML(page.text)
ip = []
for i in tree.xpath('//tr[@class="country"]/td[2]/text()'):
    ip.append(i)
k = 0
for i in tree.xpath('//tr[@class="odd"]/td[3]/text()'):
    ip[k] = ip[k]+i
    print(ip[k])
    k+=1

# message = tree.xpath('//table[@id="ip_list"]')[0]
# print(message.text)



