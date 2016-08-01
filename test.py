#coding=utf-8
import AdvancedHTMLParser
ht = '''
<p>测试段落一</p>
<p>测试段落二</p>
<p>测试段落三</p>
<p>测试段落四</p>
'''
parser = AdvancedHTMLParser.AdvancedHTMLParser()
parser.parseStr(ht)

#根据标签名获取元素
items = parser.getElementsByTagName("p")
for item in items:
    print item.innerHTML
#根据类名获取
items = parser.getElementsByClassName("link")
for item in items:
    print item.getElementsByClassName("csdn")[0].innerHTML
#根据id获取