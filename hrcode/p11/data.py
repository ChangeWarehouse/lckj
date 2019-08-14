#coding=utf-8
import  xml.dom.minidom

#打开xml文档
dom = xml.dom.minidom.parse('data.xml')

#得到文档元素对象
obj = dom.documentElement
print(obj.nodeName)
print(obj.nodeValue)
print(obj.nodeType)
print(obj.ELEMENT_NODE)