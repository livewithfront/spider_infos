import urllib
from html.parser import HTMLParser
req = urllib.request.Request("http://www.liuyangjob.com/zhaopin/qiye.asp?ComId=16299")
response = urllib.request.urlopen(req)
html=response.read()
print(html)


class JobItem(Item):
    title=Field()
    emerage=Field()
    working_address=Field()
    sexual=Field()
    need_count=Field()
    money=Field()
