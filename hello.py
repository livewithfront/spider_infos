#coding=gbk
import urllib2
from bs4 import BeautifulSoup

response=urllib2.urlopen("http://www.liuyangjob.com/zhaopin/qiye.asp?ComId=16299")
html=response.read()

# print(html)


soup=BeautifulSoup(html)
soup.prettify()
#��˾��
company_name=soup.select(".jycomv221 strong ")
print(soup.select(".jycomv221 strong "))
#ְλ��
job_name=soup.select(".jycomv4227 ul li")
print(job_name)
# for item in items:
#     print(item.innerHTML)

    #1.ѭ��ִ������
    #2.������ȡ[��ȡ�ϴ������ȡʱ��]
    #3.д���ݿ�










def getInfo():

    return

def dbStructure():

    return

def writeIntoDb():
    return