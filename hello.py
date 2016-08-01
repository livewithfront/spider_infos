#coding=gbk
import urllib2
from bs4 import BeautifulSoup

response=urllib2.urlopen("http://www.liuyangjob.com/zhaopin/qiye.asp?ComId=16299")
html=response.read()

# print(html)


soup=BeautifulSoup(html)
soup.prettify()
#公司名
company_name=soup.select(".jycomv221 strong ")
print(soup.select(".jycomv221 strong "))
#职位名
job_name=soup.select(".jycomv4227 ul li")
print(job_name)
# for item in items:
#     print(item.innerHTML)

    #1.循环执行爬虫
    #2.单次爬取[获取上次最后爬取时间]
    #3.写数据库










def getInfo():

    return

def dbStructure():

    return

def writeIntoDb():
    return